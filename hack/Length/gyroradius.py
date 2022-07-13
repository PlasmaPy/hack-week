import astropy.units as u
import numpy as np
from astropy.constants.si import e

def gyroradius(
    mass: u.kg,
    B: u.T,
    Vperp: u.m / u.s = np.nan * u.m / u.s,
) -> u.m:
    '''calculate gyro radius'''
    return mass*Vperp/(B*e)