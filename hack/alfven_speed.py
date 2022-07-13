# -*- coding: utf-8 -*-
"""
Created on Wed Jul 13 11:17:51 2022

@author: xuans
"""
import astropy.units as u
from astropy.constants.si import mu0
import numpy as np

def Alfven_speed(B: u.T, density: (u.kg / u.m**3)) -> u.m/u.s:
    
    return np.abs(B) / np.sqrt(mu0 * density)

