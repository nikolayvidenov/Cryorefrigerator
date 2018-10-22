# coding: utf-8

import scipy.integrate as integrate
from scipy.constants import *
import numpy as np

copper_th_d = 343
aluminium_th_d = 428
# Note that the units are per mol for the heat capacity
# So you must divide by the molar mass to get the heat
# capacity per mass and again to get to kilograms
copper_molar_mass = 0.063 # Kg/mol
aluminium_molar_mass = 0.027 # Kg/mol

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

print("Al: ", Al_time/60, "min/Kg")
print("Cu: ", Cu_time/60, "min/Kg")

