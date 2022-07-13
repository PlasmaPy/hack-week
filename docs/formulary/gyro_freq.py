import astropy.units as u
import numpy as np

def gyrofrequency(
        B: u.T,
        Z_e,
        m: u.kg,
) -> u.rad / u.s:
    return (Z_e * np.abs(B) / m).to(1/u.s) * u.rad