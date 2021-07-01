-- Gkyl ------------------------------------------------------------------------
local Plasma = require("App.PlasmaOnCartGrid").VlasovMaxwell()

--------------------------------------------------
--  Initial Condition Parameters --
--------------------------------------------------
-- Constants.
local chargeElc = -1.0
local massElc = 1.0
local epsilon0 = 1.0
local mu0 = 1.0

-- R is ratio of vth to ud.
local ud = 0.3
local R  = 0.333333333333333

-- Initial plasma conditions.
local nElc10 = 0.5
local nElc20 = 0.5
local uxElc10 = 0.0
local uyElc10 = ud
local uxElc20 = 0.0
local uyElc20 = -ud
local TElc10 = massElc*(R*ud)^2
local TElc20 = massElc*(R*ud)^2

local k0 = 1.0
local theta = 45.0/180.0*math.pi --0deg is pure Weibel, 90deg is pure Two Stream.
local kx = k0*math.cos(theta)
local ky = k0*math.sin(theta)
local perturb_n = 1e-8
local alpha = 1.18281106421231 --ratio of E_y/E_x. 

local vthElc10 = math.sqrt(TElc10/massElc)
local vthElc20 = math.sqrt(TElc20/massElc)

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

local tEnd = 1.0 -- Time normalized to inverse electron plasma frequency.
local nFrame = 1 -- Total number of frames.

-- Maxwellian in 2x2v
local function maxwellian2D(n, vx, vy, ux, uy, vth)
   local v2 = (vx - ux)^2 + (vy - uy)^2
   return n/(2*math.pi*vth^2)*math.exp(-v2/(2*vth^2))
end

vlasovApp = Plasma.App {
   --------------------------------------------------------------------------------
   -- Common
   --------------------------------------------------------------------------------
   logToFile = true,
   tEnd = tEnd,            -- End time
   nFrame = nFrame,        -- Number of output frames
   lower = {0.0,0.0},      -- Lower boundary of configuration space
   upper = {Lx,Ly},        -- Upper boundary of configuration space
   cells = {Nx,Ny},        -- Configuration space cells
   basis = "serendipity",  -- One of "serendipity", "maximal-order", or "tensor"
   polyOrder = polyOrder,  -- Polynomial order
   timeStepper = "rk3",    -- One of "rk2", "rk3", or "rk3s4"
   -- MPI decomposition for configuration space
   decompCuts = {Ncx,Ncy}, -- Cuts in each configuration direction
   useShared = false,      -- If using shared memory
   -- Boundary conditions for configuration space
   periodicDirs = {1,2},   -- periodic directions (both x and y)
   --------------------------------------------------------------------------------
   -- Electrons
   --------------------------------------------------------------------------------
   elc = Plasma.Species {
      charge = chargeElc, mass = massElc,
      -- Velocity space grid
      lower = {-Vmax, -Vmax},
      upper = {Vmax, Vmax},
      cells = {Nvx, Nvy},
      -- Initial conditions
      init = function (t, xn)
         local x, y, vx, vy = xn[1], xn[2], xn[3], xn[4]
         local fv = maxwellian2D(nElc10, vx, vy, uxElc10, uyElc10, vthElc10) +
            maxwellian2D(nElc20, vx, vy, uxElc20, uyElc20, vthElc20)
         return (1.0+perturb_n*math.cos(kx*x+ky*y))*fv
         end,
      evolve = true,
      diagnosticMoments = { "M1i" },
      -- new diagnostic syntax 
      -- diagnostics = { "M1i" },
   },
   --------------------------------------------------------------------------------
   -- Field solver
   --------------------------------------------------------------------------------
   field = Plasma.Field {
      epsilon0 = epsilon0, mu0 = mu0,
      init = function (t, xn)
         local x, y = xn[1], xn[2]
         local E_x  = -perturb_n*math.sin(kx*x+ky*y)/(kx+ky*alpha)
         local E_y  = alpha*E_x
         local B_z  = kx*E_y-ky*E_x
         return E_x, E_y, 0.0, 0.0, 0.0, B_z
      end,
      evolve = true, 
   },
}
--------------------------------------------------------------------------------
-- Run application
--------------------------------------------------------------------------------
vlasovApp:run()