import numpy as np

# values = {
#     "MR_air": 0.0133,      # moment w powietrzu [N·m]
#     "MR_ciecz": 0.0227,  # moment w cieczy [N·m]
#     "rho_ref": 1.2,       # gęstość referencyjna w kg/m^3
#     "uMR_air": 4.76 * (10**-5),    # niepewność momentu w powietrzu [N·m] 0.002
#     "uMR_ciecz": 6.12 * (10**-5),  # niepewność momentu w cieczy [N·m] 0.001, 0.0000166
# }
#
# # Wiktor
# # values = {
# #     "MR_air": 0.01478,      # moment w powietrzu [N·m]
# #     "MR_ciecz": 0.0236,  # moment w cieczy [N·m]
# #     "rho_ref": 1.2,       # gęstość referencyjna w kg/m^3
# #     "uMR_air": 9.25 * (10**-5),    # niepewność momentu w powietrzu [N·m] 0.002
# #     "uMR_ciecz": 7.33 * (10**-5),  # niepewność momentu w cieczy [N·m] 0.001, 0.0000166
# # }
#
#
# def rho_uncertainty(mrAir, mrFluid, pref, u_mrAir, u_mrFluid):
#     return np.sqrt((pref/mrAir*u_mrFluid)**2+(pref*(-((mrFluid-mrAir)/mrAir**2)-(1/mrAir))*u_mrAir)**2) / 1000
#
#
# print(rho_uncertainty(values["MR_air"], values["MR_ciecz"], values["rho_ref"], values["uMR_air"], values["uMR_ciecz"]))

g = 9.81
l = 0.01

massArray = [1, 0, 0, 0, 1, 0, 0, 0, 1]


def MR_uncertainty(massArray):
    sumOfIndexes = []
    for index, value in enumerate(massArray):
        if value != 0:
            sumOfIndexes.append(((index + 1)*0.058)**2)
    return g*l*np.sqrt(sum(sumOfIndexes)) / 1000


print(MR_uncertainty(massArray))
