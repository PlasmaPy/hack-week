import astropy.units as u
import numpy as np
from astropy.constants.si import e
from plasmapy.utils.decorators import validate_quantities
from plasmapy.particles import particle_input
from plasmapy.particles import Particle

@validate_quantities
@particle_input
def gyroradius(
    particle: Particle,
    B: u.T,
    Vperp: u.m / u.s,
) -> u.m:
    '''calculate gyro radius'''
    return particle.mass*np.abs(Vperp)/(B*particle.charge)