import numpy as np
import astropy.units as u
from astropy.constants.si import mu0

def Alven_speed(B: u.T, density: u.kg/u.m**-3) -> u.m / u.s:
    return abs(B)/np.sqrt(density * mu0)

