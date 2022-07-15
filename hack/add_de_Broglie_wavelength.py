# -*- coding: utf-8 -*-
"""
Created on Thu Jul 14 11:19:59 2022

@author: xuans
"""

import numpy as np

import astropy.units as u

from astropy.constants.si import k_B, h, m_e

from plasmapy.utils.decorators import validate_quantities

@validate_quantities(
    T_e={'can_be_negative': False, 'equivalencies': u.temperature_energy()}    
)
def de_Broglie_wavelength(T_e: u.K) -> u.m:
    constants = np.sqrt(h**2 / (2 * np.pi * m_e * k_B))
    return constants * 1/np.sqrt(T_e)

lambda_e = de_Broglie_wavelength
