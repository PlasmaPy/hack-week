# -*- coding: utf-8 -*-
"""
Created on Wed Jul 13 14:17:54 2022

@author: Cameron
"""
import astropy.units as u
import numpy as np
from astropy.constants.si import k_B, mu0

def Alfven_speed(B: u.T, density:(u.kg / u.m**3)) -> u.m / u.s:
    return np.abs(B) / np.sqrt(mu0 * density)
