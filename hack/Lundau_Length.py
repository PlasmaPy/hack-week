#Author: John Kappel


import numpy as np
import warnings
from plasmapy.utils.decorators import validate_quantities
from plasmapy.particles import particle_input, Particle



import astropy.units as u
from astropy.constants.si import e
from astropy.constants.si import k_B
from astropy.constants import eps0

@particle_input(require={'charged'})
@validate_quantities(
    T={
        "equivalencies": u.temperature_energy(),
        "none_shall_pass": True,
    },
    validations_on_return={"equivalencies": u.temperature_energy()},
)

def Landau_length(particle: Particle, T: u.K) -> u.m:
    r"""Calculate the classical distance of minimum approach if two particles with elementary charge head towards each other head on at a velocity typical of the temperature.
    Parameters
    --------------
    q1 :``
    T : `~astropy.units.Qunatity`
       Temperature.
    Returns
    --------------
    length_l : `astropy,units.Qunaitity`
        The Landau length in meters

    Raises
    --------
    `TypeError`
        The arguments are of an incorrect type.
    `~astropy.units.UnitConversioinError`

        The arguments do not have appropriate units.

    `ValueError`
        If any of the argument contains invalid values.
    Warns
    ------
    : `~astropy.units.UnitsWarning`
       If units are not provided, SI units are assumed.

    Notes
    ------


    
    Examples
    ---------
    >>>from astropy import units as u
    >>>Landau_length(particle ="e+", T = 300 * u.K)
    <Quantity 5.57003e-08 m>
    
    """
    return ((particle.charge**2)/ (4 * np.pi * eps0 * k_B * T))

