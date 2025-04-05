import math
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

# nazwy_parametrow = [0.12, 0.06, 0.04, 0.03, 0.024, 0.02, 0.017, 0.015, 0.013, 0.012, 0.011, 0.01, 0.0092]
#
# y_true = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65]
#
#
# # Plot
# plt.figure(figsize=(8, 5))
# plt.scatter(y_true, nazwy_parametrow, label="Zmierzona gęstość", color="blue")
# plt.plot(y_true, nazwy_parametrow, color="blue", linestyle="--", alpha=0.7)
# plt.title("Wykres zależności niepewności wzorcowania od ilości okrążeń wahadła")
# plt.ylabel("Niepewność wzorcowania [1/s]")
# plt.xlabel("Ilość okrążeń")
# plt.grid()
# plt.show()

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
# numer_pomiaru = np.arange(1, 7)
# voltage1stResistor = [2.34, 1.57, 0.78, -0.77, -1.56, -2.33]
# current1stResistor = [10.57 / 1000, 7.09 / 1000, 3.52/ 1000, -3.52 / 1000, -7.07 / 1000, -10.53 / 1000]
# resistance1stResistor = []
# resistance1stResistorUncertainty = []
# power1stResistor = []
# power1stResistorUncertainty = []
#
# voltage2ndResistor = [2.51, 1.68, 0.83, -0.83, -1.67, -2.52]
# current2ndResistor = [7.64 / 1000, 5.12 / 1000, 2.55 / 1000, -2.54 / 1000, -5.08 / 1000, -7.66 / 1000]
# resistance2ndResistor = []
# resistance2ndResistorUncertainty = []
# power2ndResistor = []
# power2ndResistorUncertainty = []
#
# voltage3rdResistor = [2.82, 1.88, 0.94, -0.94, -1.88, -2.83]
# current3rdResistor = [2.87 / 1000, 1.91 / 1000, 0.96 / 1000, -0.96 / 1000, -1.92 / 1000, -2.83 / 1000]
# resistance3rdResistor = []
# resistance3rdResistorUncertainty = []
# power3rdResistor = []
# power3rdResistorUncertainty = []
# def calculateResistanceUncertainty(inputVoltage, inputCurrent, inputVoltageUncertainty, inputCurrentUncertainty):
#     return math.sqrt(((1/inputCurrent)*inputVoltageUncertainty) ** 2 + ((-inputVoltage / (
#                 inputCurrent ** 2)) * inputCurrentUncertainty) ** 2)
#
#
# def calculatePowerUncertainty(inputVoltage, inputCurrent, inputVoltageUncertainty, inputCurrentUncertainty):
#     return math.sqrt((inputCurrent * inputVoltageUncertainty)**2 + (inputVoltage*inputCurrentUncertainty)**2)
#
# for i in range(6):
#     resistance1stResistor.append(voltage1stResistor[i]/current1stResistor[i])
#     resistance2ndResistor.append(voltage2ndResistor[i]/current2ndResistor[i])
#     resistance3rdResistor.append(voltage3rdResistor[i]/current3rdResistor[i])
#     power1stResistor.append(voltage1stResistor[i]*current1stResistor[i])
#     power2ndResistor.append(voltage2ndResistor[i]*current2ndResistor[i])
#     power3rdResistor.append(voltage3rdResistor[i]*current3rdResistor[i])
#     resistance1stResistorUncertainty.append(calculateResistanceUncertainty(voltage1stResistor[i], current1stResistor[i],
#                                                                            0.005*voltage1stResistor[i] + 3*0.01,
#                                                                            0.008*current1stResistor[i] + 3*0.00001) * 2)
#     resistance2ndResistorUncertainty.append(calculateResistanceUncertainty(voltage2ndResistor[i], current2ndResistor[i],
#                                                                            0.005*voltage2ndResistor[i] + 3*0.01,
#                                                                            0.008*current2ndResistor[i] + 3*0.00001) * 2)
#     resistance3rdResistorUncertainty.append(calculateResistanceUncertainty(voltage3rdResistor[i], current3rdResistor[i],
#                                                                            0.005 * voltage3rdResistor[i] + 3 * 0.01,
#                                                                            0.008 * current3rdResistor[i] + 3 * 0.00001) * 2)
#     power1stResistorUncertainty.append(calculatePowerUncertainty(voltage1stResistor[i], current1stResistor[i],
#                                                                  0.005*voltage1stResistor[i] + 3*0.01,
#                                                                  0.008*current1stResistor[i] + 3*0.00001) * 2)
#     power2ndResistorUncertainty.append(calculatePowerUncertainty(voltage2ndResistor[i], current2ndResistor[i],
#                                                                  0.005*voltage2ndResistor[i] + 3*0.01,
#                                                                  0.008*current2ndResistor[i] + 3*0.00001) * 2)
#     power3rdResistorUncertainty.append(calculatePowerUncertainty(voltage3rdResistor[i], current3rdResistor[i],
#                                                                  0.005*voltage3rdResistor[i] + 3*0.01,
#                                                                  0.008*current3rdResistor[i] + 3*0.00001) * 2)

# plt.figure(figsize=(10, 5))
# plt.errorbar(voltage1stResistor, power1stResistor, yerr=power1stResistorUncertainty, fmt='o-', capsize=5, label="Opornik 1 (220 Ω)")
# plt.errorbar(voltage2ndResistor, power2ndResistor, yerr=power2ndResistorUncertainty, fmt='s-', capsize=5, label="Opornik 2 (330 Ω)")
# plt.errorbar(voltage3rdResistor, power3rdResistor, yerr=power3rdResistorUncertainty, fmt='d-', capsize=5, label="Opornik 3 (1k Ω)")
# plt.xlabel("Napięcie (V)")
# plt.ylabel("Zmierzona moc (W)")
# plt.title("Moc prądu na odpowiednich opornikach")
# plt.legend()
# plt.grid(True)
# plt.show()

# x = [2, 20, 200, 2000]
# y = [0.12, 1.17, 12.4, 173]
# plt.plot(x, y, color='r', marker='o')
# plt.xlabel("Zakres oporu [kΩ]")
# plt.ylabel("Niepewność wzorcowania [%]")
# plt.title("Zależność zakresu oporu od niepewności wzrocowania")
# plt.grid(True)
# plt.show()
