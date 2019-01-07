# coding: utf-8

import scipy.integrate as integrate
from scipy.constants import *
import numpy as np
import matplotlib.pyplot as plt

# the debye temperatres are lifted from 
# http://www.knowledgedoor.com/2/elements_handbook/debye_temperature.html
# a better fit was achieved using the room temperature Debye temp
copper_th_d = 310.
aluminium_th_d = 390.
# Note that the units are per mol for the heat capacity
# So you must divide by the molar mass to get the heat
# capacity per mass and again to get to kilograms
copper_molar_mass = 0.063 # Kg/mol
aluminium_molar_mass = 0.027 # Kg/mol
# density values from wikipedia
Cu_density = 8.96 # g/cm^3
Al_density = 2.70 # g/cm^3

c = lambda x: ( x**4.*np.exp(x) ) / ( np.exp(x)-1)**2

def C_Al(T):
    r = integrate.quad(c, 0, aluminium_th_d/T)
    return 9*R*(T / aluminium_th_d)**3*r[0]/aluminium_molar_mass

def C_Cu(T):
    r = integrate.quad(c, 0, copper_th_d/T)
    return 9*R*(T / copper_th_d)**3*r[0]/copper_molar_mass

x = np.linspace(50, 300, 500)

# cooling power as a function of temperature from matching
# the PT415 data in the excel spreadhseet

def cool_power(T):
    return 15.6478521420156*(T - 31.3432835820895)**.5

def cool_time_Al(T):
    return C_Al(T) / cool_power(T)

def cool_time_Cu(T):
    return C_Cu(T) / cool_power(T)

# cool time per kilogram of aluminum
Al_time = integrate.quad(cool_time_Al, 40, 300)[0]

# cool time per kilogram of copper
Cu_time = integrate.quad(cool_time_Cu, 40, 300)[0]

print("Al: ", Al_time/60, "min/Kg ", Al_time/60*Al_density, "min/L" )
print("Cu: ", Cu_time/60, "min/Kg ", Cu_time/60*Cu_density, "min/L")


#Validation of Data
temp = np.array([4, 6, 8, 10, 12, 14, 16, 18, 20, 30, 40, 50, 60, 70, 80, 90, 100, 120, 140, 160, 180, 200, 220, 240, 260, 280, 300 ]) # in Kelvin
Al = np.array([0.292, 0.6047, 1.048, 1.573, 2.268, 3.235, 4.581, 6.416, 8.854, 33.45, 81.96, 148.8, 223.6, 298.3, 368.7, 433.3, 492.2, 594.1, 677.6, 744.5, 796.4, 835.2, 863.7, 885.4, 904.6, 925.8, 953.9 ]) # in J/ K Kg?
Cu = np.array([0.09942, 0.2303, 0.4639, 0.8558, 1.47, 2.375, 3.64, 5.327, 7.491, 26.4, 57.63, 95.84, 135.2, 171.8, 203.8, 230.9, 253.5, 287.6, 311.6, 329.4, 343.4, 355, 364.7, 372.6, 378.6, 382.5, 384 ])
extemp = np.linspace(temp[0], temp[-1], 100)


debye_Al = list(map(C_Al, extemp))
plt.plot(temp, Al, label='Al Bradley et al.', linestyle='none', marker='o', color='#6666ff', markersize=5)
plt.plot(extemp, debye_Al, label = 'Al Debye Theory', color = '#6666ff', linestyle='--')

debye_Cu = list(map(C_Cu, extemp))
plt.plot(temp, Cu, label='Cu Bradley et al.', linestyle='none', marker='o', color='#ff6666', markersize=5)
plt.plot(extemp, debye_Cu, label = 'Cu Debye Theory', linestyle='--', color='#ff6666')

plt.legend()
plt.xlabel('Temperature (K)')
plt.ylabel(r'Heat Capacity (JK$^{-1}$Kg$^{-1}$)')
plt.show()