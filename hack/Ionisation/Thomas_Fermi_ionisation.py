import numpy as np
import astropy.units as u
from plasmapy.particles import Particle, particle_input
from plasmapy.utils.decorators import validate_quantities

@validate_quantities(density={"can_be_negative": False}, equivalencies=u.temperature_energy())
@particle_input
def Zav_TF(particle: Particle, rho: u.g/u.cm**-3 , T: u.eV=0) -> u.dimensionless_unscaled:
    """
    Finite Temperature Thomas Fermi Charge State using 
    R.M. More (1985), "Pressure Ionization, Resonances, and the
    Continuity of Bound and Free States", Adv. in Atomic 
    Mol. Phys., Vol. 21, p. 332 (Table IV).

    This is a light-weight fit of the Thomas-Fermi model, not the model itself.
    """

    Z = particle.atomic_number
    A = particle.mass_number

    alpha = 14.3139
    beta = 0.6624
    a1 = 0.003323
    a2 = 0.9718
    a3 = 9.26148e-5
    a4 = 3.10165
    b0 = -1.7630
    b1 = 1.43175
    b2 = 0.31546
    c1 = -0.366667
    c2 = 0.983333

    rho1 = rho.value / A * Z
    T1 = T.value / Z ** (4. / 3.)
    Tf = T1 / (1 + T1)
    Ac = a1 * T1 ** a2 + a3 * T1 ** a4
    B = -np.exp(b0 + b1 * Tf + b2 * Tf ** 7)
    C = c1 * Tf + c2
    Q1 = Ac * rho1 ** B
    Q = (rho1 ** C + Q1 ** C) ** (1 / C)
    x = alpha * Q ** beta

    return Z * x / (1 + x + np.sqrt(1 + 2. * x))
