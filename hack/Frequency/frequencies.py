import numpy as np
import astropy.units as u
from astropy.constants.si import eps0


def Cylotron_frequency(B: u.T, mass: u.kg, charge: u.C) -> u.rad/u.s:
    """
        Cylotron frequency
    """
    return charge*B/mass


def Plasma_frequency(density: (u.kg/u.m**3), mass: u.kg, charge: u.C) -> u.rad/u.s:
    """
        Plasma frequency
    """
    return np.sqrt(density*charge**2/(eps0*mass))


def Approx_diocotron_frequency(B: u.T, density: (u.kg/u.m**3), mass: u.kg, charge: u.C) -> u.rad/u.s:
    """ 
        Frequency of Diocotron modes associated with non-neutral single species plasmas
        Best thing to do is to use existing functions (plasma frequency, cyclotron frequency) but
        since this is a demo I'm just going to write out the mat
    """
    w_pe_sq = Plasma_frequency(density, mass, charge)
    w_ce = Cylotron_frequency(B, mass, charge)
    return np.pi*w_pe_sq/w_ce
