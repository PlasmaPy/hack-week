import numpy as np 
import astropy.units as u 
from astropy.constants.si import eps0 

# Frequency of Diocotron modes associated with non-neutral single species plasmas
def Approx_diocotron_frequency(B: u.T, density: (u.kg/u.m**3), mass: u.kg, charge: u.C) -> u.rad/u.s:
    # Best thing to do is to use existing functions (plasma frequency, cyclotron frequency) but
    # since this is a demo I'm just going to write out the math
    w_pe_sq = density*charge/(epsn0*mass**2)
    w_ce =   charge*B/mass
    return np.pi*w_pe_sq/w_ce