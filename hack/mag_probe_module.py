# -*- coding: utf-8 -*-
"""
Created on Fri Jul 15 08:15:38 2022

@author: xuans
"""

'''An initial attempt to implement a magnetic pickup probe module.'''

import astropy.units as u

import numpy as np

from plasmapy.utils.decorators import validate_quantities

@validate_quantities(
    validations_on_return=u.T
)
def probe_to_field(raw: u.V, turns, area: u.m**2, t_step: u.s) -> u.T:
    '''Taking, as input, raw voltage from magnetic probe 
    (and number of coil turns) and convert it to magnetic field measurement 
    at that location.
    
    We assume [raw] is an np.array of voltages. Turns is the number of turns
    in the pick-up coil. Area is the area of a single turn in the pick-up coil.
    t_step is the time step between consecutive voltage measurements,
    assumed to be uniform given a fixed sampling frequency.
    
    The output voltage depends on the rate of change of the magnetic flux.
    
    The induced voltage in a circuit is proportional to the rate of change
    over time of the magnetic flux through that circuit.
    
    emf is measured in volts. We are given volts.
    
    emf = - N dPhi_N/ dt 
    
    phi_B = surf_integral{B(t) dot dA}
    
    To simplify, we assume we are computing the probe-aligned B field.
    So phi_B_surf = B(t)_surf * A = B(t)_surf * turns * area 
    '''
    
    # we assume instantaneous measurement of 0 to raw.
    #raw = - turns * area * B_probe / t_step
    
    B_probe = []
    
    # now expand to an array of voltages with fixed time step time traces
    for i, v in enumerate(raw):
        mag_field = ((raw[i] - raw[i-1]) * t_step) / (turns * area)
        B_probe.append(mag_field)
    
    #B_probe = np.array(B_probe)
    
    
    # include manual casting to Tesla as workaround
    return B_probe#.to(u.T)


# provide synthetic signal - sine function TODO.
measured_volts = np.linspace(0, 10, 2) * u.mV
print(measured_volts)
#for i in range(len(measured_volts)):
#     measured_volts[i] = measured_volts[i] * u.V
print(measured_volts)

measured_field = probe_to_field(measured_volts, 10, 0.1*0.1 * u.m**2, 0.01 * u.s)

print(measured_field)    
    
    
    
