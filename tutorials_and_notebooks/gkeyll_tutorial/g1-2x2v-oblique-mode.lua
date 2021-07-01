-- Gkyl ------------------------------------------------------------------------
--
--    _______     ___
-- + 6 @ |||| # P ||| +
--------------------------------------------------------------------------------

local Grid = require "Grid"
local DataStruct = require "DataStruct"
local DecompRegionCalc = require "Lib.CartDecomp"
local Time = require "Lib.Time"
local Basis = require "Basis"
local EqVlasov = require "Eq.Vlasov"
local EqMaxwell = require "Eq.PerfMaxwell"
local Updater = require "Updater"
local ffi = require "ffi"

-- Function for writing information to .log file.
local Logger = require "Lib.Logger"
local logger = Logger {
   logToFile = True
}
local log = function(...)
   logger(string.format(...))
   logger("\n")
end

--------------------------------------------------
--  Initial Condition Parameters --
--------------------------------------------------
-- Constants.
local chargeElc = -1.0
local massElc = 1.0
local epsilon0 = 1.0

-- R is ratio of vth to ud.
local ud = 0.3
local R  = 0.333333333333333

-- Initial plasma conditions.
local nElc1 = 0.5
local nElc2 = 0.5
local uxElc1 = 0.0
local uyElc1 = ud
local uxElc2 = 0.0
local uyElc2 = -ud
local TElc1 = massElc*(R*ud)^2
local TElc2 = massElc*(R*ud)^2

local k0 = 1.0
local theta = 45.0/180.0*math.pi --0deg is pure Weibel, 90deg is pure Two Stream.
local kx = k0*math.cos(theta)
local ky = k0*math.sin(theta)
local perturb_n = 1e-8
local alpha = 1.18281106421231 --ratio of E_y/E_x. 

local vthElc1 = math.sqrt(TElc1/massElc)
local vthElc2 = math.sqrt(TElc2/massElc)

local Nx = 24 -- Number of configuration space point in x.
local Ny = 24 -- Number of configuration space point in y.
local Nvx = 24 -- Number of velocity space point in vx.
local Nvy = 24 -- Number of velocity space point in vy.
local Lx = 2*math.pi/kx -- domain size in x.
local Ly = 2*math.pi/ky -- domain size in y.
local Vmax = 0.9 -- Upper bound of velocity grid (3x initial drift velocity, 0.9 speed of light).

local Ncx = 1 -- Number of MPI processes in x.
local Ncy = 1 -- Number of MPI processes in y.

local polyOrder = 2 -- polynomial order.
local cflNum = 1.0/(2*polyOrder+1) -- CFL multiplicative factor.

-- I/O control.
local step   = 1
local tCurr  = 0.0
local tEnd = 1.0 -- Time normalized to inverse electron plasma frequency.
-- Find time intervals to write out data.
local nFrame = 1
local frame = 1
local tFrame = (tEnd-tCurr)/nFrame
local nextIOt = tFrame
--------------------------------------------------

--------------------------------------------------
--  Grid and Decomposition Setup --
--------------------------------------------------
-- Decomposition object for phase space grid. 
local decompPhase = DecompRegionCalc.CartProd {
   cuts = {Ncx, Ncy, 1, 1},
   useShared = false,
}
-- Decomposition object for configuration space grid. 
local decompConfig = DecompRegionCalc.CartProd {
   cuts = {Ncx, Ncy},
   useShared = false,
}

-- Cartesian rectangular grid for phase space.
local phaseGrid = Grid.RectCart {
   lower = {0.0, 0.0, -Vmax, -Vmax},
   upper = {Lx, Ly, Vmax, Vmax},
   cells = {Nx, Ny, Nvx, Nvy},
   periodicDirs = {1, 2},
   decomposition = decompPhase,
}
-- Cartesian rectangular grid for configuration space.
local confGrid = Grid.RectCart {
   lower = { phaseGrid:lower(1), phaseGrid:lower(2) },
   upper = { phaseGrid:upper(1), phaseGrid:upper(2) },
   cells = { phaseGrid:numCells(1), phaseGrid:numCells(2) },
   periodicDirs = {1, 2},
   decomposition = decompConfig,
}
local cdim = confGrid:ndim()
local vdim = phaseGrid:ndim()-confGrid:ndim()
--------------------------------------------------

--------------------------------------------------
--  Basis functions --
--------------------------------------------------
local phaseBasis = Basis.CartModalSerendipity { ndim = phaseGrid:ndim(), polyOrder = polyOrder }
local confBasis  = Basis.CartModalSerendipity { ndim = confGrid:ndim(), polyOrder = polyOrder }
--------------------------------------------------

--------------------------------------------------
--  Cartesian Fields --
--------------------------------------------------

-- NOTE: These first two CartFields (distribution function and em fields) are written out.
-- So, we also give them the metadata of polynomial order and basis type for easy plotting.

local distf = DataStruct.Field {
   onGrid        = phaseGrid,
   numComponents = phaseBasis:numBasis(),
   ghost         = {1, 1},
   metaData = {
      polyOrder = phaseBasis:polyOrder(),
      basisType = phaseBasis:id()
   },
}

-- EM fields.
local em = DataStruct.Field {
   onGrid        = confGrid,
   numComponents = 8*confBasis:numBasis(),
   ghost         = {1, 1},
   metaData = {
      polyOrder = phaseBasis:polyOrder(),
      basisType = phaseBasis:id()
   },
}

-- Momentum (1st moment).
local momDens = DataStruct.Field {
   onGrid        = confGrid,
   numComponents = confBasis:numBasis()*vdim,
   ghost         = {1, 1},
   metaData = {
      polyOrder = phaseBasis:polyOrder(),
      basisType = phaseBasis:id()
   },
}

-- Total EM field (to obtain charge/mass * electromagnetic fields).
local totalEmField = DataStruct.Field {
   onGrid        = confGrid,
   numComponents = 8*confBasis:numBasis(),
   ghost         = {1, 1},
}
--------------------------------------------------

--------------------------------------------------
-- Extra fields for RK stepping --
--------------------------------------------------
local distf1 = DataStruct.Field {
   onGrid        = phaseGrid,
   numComponents = phaseBasis:numBasis(),
   ghost         = {1, 1},
}
local distfNew = DataStruct.Field {
   onGrid        = phaseGrid,
   numComponents = phaseBasis:numBasis(),
   ghost         = {1, 1},
}

local em1 = DataStruct.Field {
   onGrid        = confGrid,
   numComponents = 8*confBasis:numBasis(),
   ghost         = {1, 1},
}
local emNew = DataStruct.Field {
   onGrid        = confGrid,
   numComponents = 8*confBasis:numBasis(),
   ghost         = {1, 1},
}
--------------------------------------------------

--------------------------------------------------
-- CFL arrays for computing size of time-step --
--------------------------------------------------
local cflRateByCell = DataStruct.Field {
   onGrid        = phaseGrid,
   numComponents = 1,
   ghost         = {1, 1},
}
local dtGlobal = ffi.new("double[2]")

local cflRateByCellMaxwell = DataStruct.Field {
   onGrid        = confGrid,
   numComponents = 1,
   ghost         = {1, 1},
}
local dtGlobalMaxwell = ffi.new("double[2]")
--------------------------------------------------

--------------------------------------------------
-- Updaters --
--------------------------------------------------
VlasovCalc = EqVlasov {
   onGrid = phaseGrid,
   phaseBasis = phaseBasis,
   confBasis = confBasis,
   charge = chargeElc,
   mass = massElc,
   hasElectricField = true,
   hasMagneticField = true,
}
-- Specify the directions for zero-flux directions in velocity space.
local zfd = { }
for d = 1, vdim do zfd[d] = cdim+d end

MaxwellCalc = EqMaxwell {
   lightSpeed = 1.0,
   elcErrorSpeedFactor = 0.0,
   mgnErrorSpeedFactor = 0.0,
   basis = confBasis,
}

VlasovSlvr = Updater.HyperDisCont {
   onGrid = phaseGrid,
   basis = phaseBasis,
   cfl = cflNum,
   equation = VlasovCalc,
   zeroFluxDirections = zfd,
}

MaxwellSlvr = Updater.HyperDisCont {
   onGrid = confGrid,
   basis = confBasis,
   cfl = cflNum,
   equation = MaxwellCalc,
}

momDensityCalc = Updater.DistFuncMomentCalc {
   onGrid = phaseGrid,
   phaseBasis = phaseBasis,
   confBasis = confBasis,
   moment = "M1i",
}
--------------------------------------------------

--------------------------------------------------
-- Initial conditions -- 
--------------------------------------------------
-- Maxwellian in 2x2v
local function maxwellian2D(n, vx, vy, ux, uy, vth)
   local v2 = (vx - ux)^2 + (vy - uy)^2
   return n/(2*math.pi*vth^2)*math.exp(-v2/(2*vth^2))
end

function fInitial(x,y,vx,vy)
   local fv = maxwellian2D(nElc1, vx, vy, uxElc1, uyElc1, vthElc1)+maxwellian2D(nElc2, vx, vy, uxElc2, uyElc2, vthElc2)
   return (1.0+perturb_n*math.cos(kx*x+ky*y))*fv
end

function emInitial(x,y)
   local E_x = -perturb_n*math.sin(kx*x+ky*y)/(kx+ky*alpha)
   local E_y = alpha*E_x
   local B_z = kx*E_y-ky*E_x
   return E_x, E_y, 0.0, 0.0, 0.0, B_z, 0.0, 0.0
end

-- Updater to initialize distribution function.
local initF = Updater.ProjectOnBasis {
   onGrid = phaseGrid,
   basis = phaseBasis,
   projectOnGhosts = true,
   evaluate = function (t, xn)
      return fInitial(xn[1],xn[2],xn[3],xn[4])
   end
}
-- Updater to initialize electromagnetic fields.
local initFields = Updater.ProjectOnBasis {
   onGrid = confGrid,
   basis = confBasis,
   projectOnGhosts = true,
   evaluate = function (t, xn)
      return emInitial(xn[1],xn[2])
   end
}

initF:advance(0.0, {}, {distf})
-- Compute initial momentum.
momDensityCalc:advance(0.0, {distf}, {momDens})

initFields:advance(0.0, {}, {em})

-- Synchronize distribution function and EM fields across ghost cells.
distf:sync()
em:sync()
--------------------------------------------------

--------------------------------------------------
-- Helper functions for main simulation -- 
--------------------------------------------------
-- Function to combine and accumulate forward Euler time-step.
local function combine(outIdx, a, aIdx, ...)
   local args = {...} -- Package up rest of args as table.
   local nFlds = #args/2
   outIdx:combine(a, aIdx)
   for i = 1, nFlds do -- Accumulate rest of the fields.
      outIdx:accumulate(args[2*i-1], args[2*i])
   end
end

-- Function to take a single forward-euler time-step.
local function forwardEuler(tCurr, dt, fIn, emIn, fOut, emOut)
   -- Clear CFL before taking time-step.
   cflRateByCell:clear(0.0)
   cflRateByCellMaxwell:clear(0.0)
   -- Clear totalEmField and accumulate charge/mass electromagnetic field.
   totalEmField:clear(0.0)
   local qbym = chargeElc/massElc
   totalEmField:accumulate(qbym, emIn)

   -- Compute momentum from distribution function.
   momDensityCalc:advance(0.0, {fIn}, {momDens})

   -- Compute RHS of Vlasov equation.
   VlasovSlvr:setDtAndCflRate(dtGlobal[0], cflRateByCell)
   VlasovSlvr:advance(tCurr, {fIn, totalEmField}, {fOut})

   -- Compute RHS of Maxwell's equations.
   MaxwellSlvr:setDtAndCflRate(dtGlobalMaxwell[0], cflRateByCellMaxwell)
   MaxwellSlvr:advance(tCurr, {emIn}, {emOut})

   -- Accumulate current onto RHS of electric field.
   -- Third input is the component offset.
   -- The offset is zero for accumulating the current onto the electric field.
   emOut:accumulateOffset(-chargeElc/epsilon0, momDens, 0)

   -- Get the size of the time-step (only do this for the first RK step)
   local dtSuggested = tEnd - tCurr + 1e-20
   if dt == nil then
      dtSuggested = math.min(cflNum/cflRateByCell:reduce('max')[1], dtSuggested)
      dtSuggested = math.min(cflNum/cflRateByCellMaxwell:reduce('max')[1], dtSuggested)
      dtGlobal[0] = dtSuggested
   else
      dtSuggested = dt
   end

   -- Increment solution f^{n+1} = f^n + dtSuggested*fRHS.
   combine(fOut, dtSuggested, fOut, 1.0, fIn)
   combine(emOut, dtSuggested, emOut, 1.0, emIn)
   -- Synchronize ghost cells across MPI processes.
   fOut:sync()
   emOut:sync()

   return dtSuggested
end

-- Function to advance solution using SSP-RK3 scheme.
local function rk3(tCurr)
   -- RK stage 1
   local dt = forwardEuler(tCurr, nil, distf, em, distf1, em1)

   -- RK stage 2
   forwardEuler(tCurr+dt, dt, distf1, em1, distfNew, emNew)
   distf1:combine(3.0/4.0, distf, 1.0/4.0, distfNew)
   em1:combine(3.0/4.0, em, 1.0/4.0, emNew)

   -- RK stage 3
   forwardEuler(tCurr+dt/2, dt, distf1, em1, distfNew, emNew)
   distf1:combine(1.0/3.0, distf, 2.0/3.0, distfNew)
   distf:copy(distf1)
   em1:combine(1.0/3.0, em, 2.0/3.0, emNew)
   em:copy(em1)

   -- return size of the time-step so we know what time we have evolved to
   return dt 
end

-- Function to write out fields.
local function writeFields(frameNum, tCurr)
   momDensityCalc:advance(tCurr, {distf}, {momDens})

   distf:write(string.format("distf_%d.bp", frameNum), tCurr)
   momDens:write(string.format("momDens_%d.bp", frameNum), tCurr)
   em:write(string.format("field_%d.bp", frameNum), tCurr)
end
--------------------------------------------------

-- Write out initial conditions.
writeFields(0, tCurr)

--------------------------------------------------
-- Main simulation loop -- 
--------------------------------------------------
local tmSimStart = Time.clock()
while tCurr<tEnd do
   -- Take a time-step.
   local dt = rk3(tCurr)
   -- Write out data (based on time)
   if (tCurr+dt > nextIOt or tCurr+dt >= tEnd) then
      log(string.format("Writing data at time %g (frame %d) ...\n", tCurr+dt, frame))
      writeFields(frame, tCurr+dt)
      frame = frame + 1
      nextIOt = nextIOt + tFrame
   end
   tCurr = tCurr + dt
   step = step + 1
   if (tCurr >= tEnd) then
      break
   end
end -- end of time-step loop
local tmSimEnd = Time.clock()
print(string.format("Total time for simulation %g\n", tmSimEnd - tmSimStart))