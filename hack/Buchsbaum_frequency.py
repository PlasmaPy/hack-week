__all__ = ["buchsbaum_frequency"]
__aliases__ = ["w_bb_", "w_ii_", "w_bi_"]

import numpy as np
import astropy.units as u

from plasmapy.formulary.frequencies import gyrofrequency, plasma_frequency
from plasmapy.particles import Particle
from plasmapy.utils.decorators import (
    angular_freq_to_hz,
    validate_quantities,
)
__all__ += __aliases__


@validate_quantities(
    validations_on_return={
        "units": [u.rad / u.s, u.Hz],
        "equivalencies": [(u.cy / u.s, u.Hz)],
    }
)
@angular_freq_to_hz
def buchsbaum_frequency(
    B: u.T,
    n1: u.m**-3,
    n2: u.m**-3,
    particle1: Particle,
    particle2: Particle,
    Z1=None,
    Z2=None,
) -> u.rad / u.s:
    r"""
    Calculate the Buchsbaum frequency in units of radians per second.

    **Aliases:** `w_bb_`, `w_ii_`, `w_bi_`

    Parameters
    ----------
    B : `~astropy.units.Quantity`
        The magnetic field magnitude in units convertible to tesla.
    n1 : `~astropy.units.Quantity`
        Particle number density of species #1 in units convertible to m\ :sup:`-3`.
    n2 : `~astropy.units.Quantity`
        Particle number density of species #2 in units convertible to m\ :sup:`-3`.
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
        The charge state for ion species #1. If not provided, it defaults to the charge number of ``particle1``.
    Z2 : `float` or `~astropy.units.Quantity`, optional
        The charge state for ion species #2. If not provided, it defaults to the charge number of ``particle2``.

    Returns
    -------
    omega_BB : `~astropy.units.Quantity`
        The Buchsbaum frequency of the plasma in units of radians per second.
        Setting keyword ``to_hz=True`` will apply the factor of :math:`1/2π`
        and yield a value in Hz.

    Raises
    ------
    `TypeError`
        If the magnetic field is not a `~astropy.units.Quantity` or
        ``particle`` is not of an appropriate type.
    `ValueError`
        If the magnetic field contains invalid values or particle cannot
        be used to identify a particle or isotope.

    Warns
    -----
    : `~astropy.units.UnitsWarning`
        If units are not provided, SI units are assumed.

    Notes
    -----
    In a magnetized plasma, the presence of two ion species allows the
    perpendicular component of the cold-plasma dielectric coefficient
    :math:`\epsilon_{\perp}` to vanish at an angular frequency referred
    to as the Buchsbaum frequency :cite:p:`buchsbaum:1960`, also called
    the bi-ion frequency or ion-ion hybrid frequency
    :cite:p:`vincena:2013`.  This frequency can be defined as:

    .. math::
        \omega_{BB} \equiv \sqrt{\frac{\omega_{p1}^{2}\omega_{c2}^{2}
            + \omega_{p2}^{2}\omega_{c1}^{2}}{\omega_{p2}^{2}+\omega_{p2}^{2}}}


    """

    omega_c1 = gyrofrequency(B, particle1, signed=False, Z=Z1)
    omega_c2 = gyrofrequency(B, particle2, signed=False, Z=Z2)
    omega_p1 = plasma_frequency(n1, particle1, z_mean=Z1)
    omega_p2 = plasma_frequency(n2, particle2, z_mean=Z2)

    return np.sqrt((omega_p1**2 * omega_c2**2 + omega_p2**2 * omega_c1**2) / ( omega_p1**2 + omega_p2**2))


w_bb_ = buchsbaum_frequency
"""Alias to `~hack.Buchsbaum_frequency.buchsbaum_frequency`."""

w_ii_ = buchsbaum_frequency
"""Alias to `~hack.Buchsbaum_frequency.buchsbaum_frequency`."""

w_bi_ = buchsbaum_frequency
"""Alias to `~hack.Buchsbaum_frequency.buchsbaum_frequency`."""
