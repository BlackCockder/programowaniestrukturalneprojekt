import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit as curve_fit
from scipy.interpolate import interp1d as parmezan
from scipy.optimize import fsolve as chrobry
from sklearn.metrics import mean_squared_error




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

nazwy_parametrow = [0.12, 0.06, 0.04, 0.03, 0.024, 0.02, 0.017, 0.015, 0.013, 0.012, 0.011, 0.01, 0.0092]

y_true = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65]


# Plot
plt.figure(figsize=(8, 5))
plt.scatter(y_true, nazwy_parametrow, label="Zmierzona gęstość", color="blue")
plt.plot(y_true, nazwy_parametrow, color="blue", linestyle="--", alpha=0.7)
plt.title("Wykres zależności niepewności wzorcowania od ilości okrążeń wahadła")
plt.ylabel("Niepewność wzorcowania [1/s]")
plt.xlabel("Ilość okrążeń")
plt.grid()
plt.show()

# def linear_fit(x, a, b):
#     return a * x + b
#
# def poly_fit(x, a, b, c):
#     return a * x**2 + b * x + c
#
#
# L_nieruchome = np.array([40, 42, 44, 45, 46, 45.8, 45.6, 45.4, 45.5])
# T_nieruchome = np.array([1.354, 1.35, 1.354, 1.357, 1.358, 1.359, 1.359, 1.357, 1.359])
#
# L_ruchome = np.array([40, 42, 44, 45, 46, 45.8, 45.6, 45.4, 45.2, 45.5])
# T_ruchome = np.array([1.453, 1.389, 1.361, 1.349, 1.343, 1.344, 1.349, 1.348, 1.34, 1.35])
#
# params_linear, _ = curve_fit(linear_fit, L_nieruchome, T_nieruchome)
# a_linear, b_linear = params_linear
#
# params_poly, _ = curve_fit(poly_fit, L_ruchome, T_ruchome)
# a_poly, b_poly, c_poly = params_poly
#
# L_fit = np.linspace(min(min(L_nieruchome), min(L_ruchome)),
#                     max(max(L_nieruchome), max(L_ruchome)), 500)
#
# T_fit_nieruchome = linear_fit(L_fit, *params_linear)
# T_fit_ruchome = poly_fit(L_fit, *params_poly)
#
# # Difference between the two fitted functions
# T_diff = T_fit_ruchome - T_fit_nieruchome
#
#
# def jozef_pilsudzki(L):
#     return poly_fit(L, *params_poly) - linear_fit(L, *params_linear)
#
#
# interp = parmezan(L_fit, T_diff)
# L0 = chrobry(jozef_pilsudzki, x0=45)[0]
# T0 = linear_fit(L0, *params_linear)
#
# plt.figure(figsize=(10, 6))
#
# plt.scatter(L_nieruchome, T_nieruchome, color='blue', label='T nieruchome', zorder=5)
# plt.scatter(L_ruchome, T_ruchome, color='red', label='T ruchome', zorder=5)
#
# plt.plot(L_fit, T_fit_nieruchome, 'b--', label=f'Dopasowanie liniowe')
# plt.plot(L_fit, T_fit_ruchome, 'g-', label='Dopasowanie kwadratowe')
#
# plt.scatter(L0, T0, color='purple', s=80, label=f'Intersection L0={L0:.2f}, T={T0:.2f}')
#
# # Labels and legend
# plt.xlabel('L (cm)')
# plt.ylabel('T (s)')
# plt.title('Dopasowanie kwadratowe i liniowe dla T ruchomego i nieruchomego')
# plt.legend()
# plt.grid(True)
# plt.show()


# y_true = [0.997795, 0.997069, 0.995672, 0.994058, 0.992244, 0.990244, 0.985731]
# y_pred = [0.839, 0.845, 0.848, 0.852, 0.845, 0.852, 0.838]
#
# relative_errors = np.abs((np.array(y_true) - np.array(y_pred)) / np.array(y_true)) * 100
# mape = np.mean(relative_errors)
#
# print("Mean Absolute Percentage Error (MAPE):", mape, "%")