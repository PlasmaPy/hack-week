#Author: John Kappel

from re import M
import numpy.np
import astropy.units as u
from astropy.constants.si import e
from astropy.constants.si import k_B


"""
Parameters -
    T - Temperature
    T_E - Electron Temperature
    n_e - Electron number density
#################################

Consants -
    e - The electron charge 
    k_B - Boltzmann Constant


"""

def Landau_length(T: u.T) -> u.m:
    return e**2/ (k_B * T)