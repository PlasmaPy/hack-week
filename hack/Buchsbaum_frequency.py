from plasmapy.formulary.frequencies import gyrofrequency, plasmafrequency
import numpy as np
from plasmapy.particles import Particle

"""

Buchsbaum_frequency(omega_p1, omega_c1, omega_p2, omega_c2):
    return (omega_p1 ** 2 * omega_c2 **2 + omega_p2 ** 2 * omega_c1 **2) / ( omega_p1 **2 + omega_p2 **2)
"""
def Buchsbaum_frequency(B: Unit('T'), particle1: Particle, signed1=False, Z1=None, particle2: Particle, signed2=False,
    Z2=None, to_hz=False):
r"""
Calculate the particle gyrofrequency in units of radians per second.
**Aliases:** `omega_bb_`, `omega_ii_`, `omega_bi_`
Parameters
----------
B : `~astropy.units.Quantity`
    The magnetic field magnitude in units convertible to tesla.
particle : `~plasmapy.particles.particle_class.Particle`
    Representation of the particle species (e.g., 'p' for protons, 'D+'
    for deuterium, or 'He-4 +1' for singly ionized helium-4). If no
    charge state information is provided, then the particles are assumed
    to be singly charged.
signed : `bool`, optional
    A gyrofrequency can be defined as signed (negative for electron,
    positive for ion). Default is `False` (unsigned, i.e. always
    positive).
Z : `float` or `~astropy.units.Quantity`, optional
    The average ionization (arithmetic mean) for a plasma where
    a macroscopic description is valid. If this quantity is not
    given then the charge number of the ion
    is used. This is effectively an average gyrofrequency for the
    plasma where multiple charge states are present, and should
    not be interpreted as the gyrofrequency for any single particle.
    If not provided, it defaults to the charge number of the ``particle``.
Returns
-------
omega_BB : `~astropy.units.Quantity`
    The Buchsbaum frquency of the plasma in units of radians per second.

    Notes
    -----
    
In a magnetized plasma, the presence of two ion species allows the perpendicular
component of the cold-plasma dielectric coefficient
math:: \epsilon_{\perp} to vanish at an angular frequency referred to as the 
Buchsbaum frequency[1], or called the bi-ion frequency, or ion-ion hybrid frequency[2].
This frequency can be defined as:
math::
\omega_{BB}^2 \equiv \frac{\omega_{p1}^{2}\Omega_{c2}^{2} + \omega_{p2}^{2}\Omega_{c1}^{2}}{\omega_{p2}^{2}+\omega_{p2}^{2}}



[1] S. J. Buchsbaum, Phys. Fluids 3, 418 (1960); Resonance in a Plasma with Two Ion Species; https://doi.org/10.1063/1.1706052
[2] S. T. Vincena, et al.: https://doi.org/10.1063/1.4775777


    """

return (omega_p1**2 * omega_C2**2 + omega_p2**2 * omega_C1**2) / ( omega_p1**2 + omega_p2**2)

omega_bb_ = Buchsbaum_frequency
"""Alias to `~plasmapy.formulary.frequencies.Buchsbaum_frequency`."""

omega_ii_ = Buchsbaum_frequency
"""Alias to `~plasmapy.formulary.frequencies.Buchsbaum_frequency`."""

omega_bi_ = Buchsbaum_frequency
"""Alias to `~plasmapy.formulary.frequencies.Buchsbaum_frequency`."""