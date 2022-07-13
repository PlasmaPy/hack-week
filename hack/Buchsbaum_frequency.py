from plasmapy.formulary.frequencies import gyrofrequency, plasmafrequency
import numpy as np
from plasmapy.particles import Particle

def Buchsbaum_frequency(B: Unit('T'), n1: u.m**-3, n2: u.m**-3, particle1: Particle, particle2: Particle, Z1=None,
    Z2=None, to_hz=False):
    r"""
    Calculate the Buchsbaum frequency in units of radians per second.
    **Aliases:** `omega_bb_`, `omega_ii_`, `omega_bi_`
    Parameters
    ----------
    B : `~astropy.units.Quantity`
        The magnetic field magnitude in units convertible to tesla.
    particle1 : `~plasmapy.particles.particle_class.Particle`
        Representation of the first particle species (e.g., 'p' for protons, 'D+'
        for deuterium, or 'He-4 +1' for singly ionized helium-4). If no
        charge state information is provided, then species-1 is assumed
        to be singly charged.
    particle2 : `~plasmapy.particles.particle_class.Particle`
        Representation of the first particle species (e.g., 'p' for protons, 'D+'
        for deuterium, or 'He-4 +1' for singly ionized helium-4). If no
        charge state information is provided, then species-2 is assumed
        to be singly charged.
    Z1 : `float` or `~astropy.units.Quantity`, optional
        The charge state for ion species #1. If not provided, it defaults to the charge number of the ``particle1``.
    Z2 : `float` or `~astropy.units.Quantity`, optional
        The charge state for ion species #2. If not provided, it defaults to the charge number of the ``particle2``.

    Returns
    -------
    omega_BB : `~astropy.units.Quantity`
        The Buchsbaum frquency of the plasma in units of radians per second.

        Notes
        -----

    In a magnetized plasma, the presence of two ion species allows the perpendicular
    component of the cold-plasma dielectric coefficient
    math:: \epsilon_{\perp} to vanish at an angular frequency referred to as the
    Buchsbaum frequency[1], also called the bi-ion frequency or ion-ion hybrid frequency[2].
    This frequency can be defined as:
    math::
    \omega_{BB}^2 \equiv \frac{\omega_{p1}^{2}\Omega_{c2}^{2} + \omega_{p2}^{2}\Omega_{c1}^{2}}{\omega_{p2}^{2}+\omega_{p2}^{2}}

    [1] S. J. Buchsbaum, Phys. Fluids 3, 418 (1960); Resonance in a Plasma with Two Ion Species; https://doi.org/10.1063/1.1706052
    [2] S. T. Vincena, W. A. Farmer, J. E. Maggs, and G. J. Morales, Phys. Plasmas, 20, 012111 (2013);
    Investigation of an ion-ion hybrid Alfvén wave resonator https://doi.org/10.1063/1.4775777
    """

    omega_c1 = gyrofrequency(B, particle1, signed=False, Z=Z1)
    omega_c2 = gyrofrequency(B, particle2, signed=False, Z=Z2)
    omega_p1 = plasma_frequency(n1: u.m**-3, particle1: Particle, z_mean=None)


    return (omega_p1**2 * omega_c2**2 + omega_p2**2 * omega_c1**2) / ( omega_p1**2 + omega_p2**2)

omega_bb_ = Buchsbaum_frequency
"""Alias to `~plasmapy.formulary.frequencies.Buchsbaum_frequency`."""

omega_ii_ = Buchsbaum_frequency
"""Alias to `~plasmapy.formulary.frequencies.Buchsbaum_frequency`."""

omega_bi_ = Buchsbaum_frequency
"""Alias to `~plasmapy.formulary.frequencies.Buchsbaum_frequency`."""