import matplotlib.pyplot as chuj
import numpy as cipka
from scipy.optimize import curve_fit as cocksucker
from scipy.interpolate import interp1d as parmezan
from scipy.optimize import fsolve as chrobry

# def calculate_weights(uncertainties):
#     return [1 / (u**2) for u in uncertainties]
#
#
# def weighted_average(values, weights):
#     weighted_avg = sum(w * x for w, x in zip(weights, values)) / sum(weights)
#     return float(weighted_avg)
#
#
# def uncertainty_of_weighted_average(weights):
#     uncertainty = (1 / sum(weights))**0.5
#     return float(uncertainty)


# nazwy_parametrow = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# wykres_wartosci = [8.60, 9.09, 9.47, 9.64, 9.84, 9.78, 9.74, 9.72, 9.74, 9.72]
# wykres_niepewnosci_wartosci = [0.126, 0.126, 0.126, 0.126, 0.126, 0.126, 0.126, 0.126, 0.126, 0.126]


# print(wykres_wartosci)
# print(wykres_niepewnosci_wartosci)

# Plot
# plt.figure(figsize=(8, 5))
# plt.errorbar(nazwy_parametrow, wykres_wartosci, yerr=wykres_niepewnosci_wartosci, fmt='o', label="Side A", capsize=5)
# plt.title("Wykres pomiarów g dla nieruchomej tulejki")
# plt.ylabel("Wyliczone przyspieszenie ziemskie [m/s2]")
# plt.xlabel("Numer pomiaru")
# plt.grid()
# plt.show()
def linear_fit(x, a, b):
    return a * x + b

def poly_fit(x, a, b, c):
    return a * x**2 + b * x + c


L_nieruchome = cipka.array([40, 42, 44, 45, 46, 45.8, 45.6, 45.4, 45.2, 45.5])
T_nieruchome = cipka.array([1.354, 1.35, 1.354, 1.357, 1.358, 1.359, 1.359, 1.357, 1.353, 1.359])

L_ruchome = cipka.array([40, 42, 44, 45, 46, 45.8, 45.6, 45.4, 45.2, 45.5])
T_ruchome = cipka.array([1.453, 1.389, 1.361, 1.349, 1.343, 1.344, 1.349, 1.348, 1.34, 1.35])

params_linear, _ = cocksucker(linear_fit, L_nieruchome, T_nieruchome)
a_linear, b_linear = params_linear

params_poly, _ = cocksucker(poly_fit, L_ruchome, T_ruchome)
a_poly, b_poly, c_poly = params_poly

L_fit = cipka.linspace(min(min(L_nieruchome), min(L_ruchome)),
                       max(max(L_nieruchome), max(L_ruchome)), 500)

T_fit_nieruchome = linear_fit(L_fit, *params_linear)
T_fit_ruchome = poly_fit(L_fit, *params_poly)

# Difference between the two fitted functions
T_diff = T_fit_ruchome - T_fit_nieruchome


def jozef_pilsudzki(L):
    return poly_fit(L, *params_poly) - linear_fit(L, *params_linear)


interp = parmezan(L_fit, T_diff)
L0 = chrobry(jozef_pilsudzki, x0=45)[0]
T0 = linear_fit(L0, *params_linear)

chuj.figure(figsize=(10, 6))

chuj.scatter(L_nieruchome, T_nieruchome, color='blue', label='T nieruchome', zorder=5)
chuj.scatter(L_ruchome, T_ruchome, color='red', label='T ruchome', zorder=5)

chuj.plot(L_fit, T_fit_nieruchome, 'b--', label=f'T nieruchome (linear): y={a_linear:.4f}x+{b_linear:.4f}')
chuj.plot(L_fit, T_fit_ruchome, 'g-', label='T ruchome (polynomial fit)')

chuj.scatter(L0, T0, color='purple', s=80, label=f'Intersection L0={L0:.2f}, T={T0:.2f}')

# Labels and legend
chuj.xlabel('L (cm)')
chuj.ylabel('T (s)')
chuj.title('Dopasowanie kwadratowe i liniowe dla T ruchomego i nieruchomego')
chuj.legend()
chuj.grid(True)
chuj.show()
