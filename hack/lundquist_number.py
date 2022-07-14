import astropy.units as u

from plasmapy.formulary import dimensionless, speeds


def Lundquist_Num(
        L: u.m,
        B: u.T,
        density: (u.m**-3, u.kg / u.m**3),
        sigma: u.S / u.m
) -> u.dimensionless_unscaled:
    alfven = speeds.Alfven_speed(B, density)
    return dimensionless.Mag_Reynolds(alfven, L, sigma)
