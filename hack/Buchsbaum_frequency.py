"""
Buchsbaum frequency[1], also called the bi-ion frequency, and ion-ion hybrid frequency[2].
in a magnetized
plasma, the presence of two ion species allows the perpendicular
component of the cold-plasma dielectric coefficient
:math: \epsilon_{\perp} :math: to vanish at a frequency commonly referred to as the ion-
hybrid frequency, or Buc

[1] S. J. Buchsbaum, Phys. Fluids 3, 418 (1960); Resonance in a Plasma with Two Ion Species; https://doi.org/10.1063/1.1706052
[2] S. T. Vincena, et al.: https://doi.org/10.1063/1.4775777
:math:
\omega_{BB}^2 \equiv \frac{\omega_{p1}^{2}\Omega_{c2}^{2} +
\omega_{p2}^{2}\Omega_{c1}^{2}}{\omega_{p2}^{2}+\omega_{p2}^{2}}
:math:
def Buchsbaum_frequency(omega_p1, omega_c1, omega_p2, omega_c2):
    return (omega_p1 ** 2 * omega_c2 **2 + omega_p2 ** 2 * omega_c1 **2) / ( omega_p1 **2 + omega_p2 **2)
"""

