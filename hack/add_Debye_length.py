# -*- coding: utf-8 -*-
"""
Created on Wed Jul 13 12:36:48 2022

@author: xuans
"""
import astropy.units as u
import numpy as np

from astropy.constants.si import c, e, eps0, k_B

def Debye_length(T_e: u.K, n_e: u.m**-3) -> u.m:
    
    return np.sqrt(eps0 * k_B * T_e / (n_e * e**2))
