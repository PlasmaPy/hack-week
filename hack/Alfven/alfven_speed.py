import numpy as np 
import astropy.units as u 
from astropy.constants.si import k_B, mu0

def Alfven_speed(B: u.T, density: (u.kg/u.m**3) -> u.m/u.s:
    return np.abs(B)/np.sqrt(mu0*density)