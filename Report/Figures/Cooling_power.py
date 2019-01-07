import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit

temp = np.array([31.34328358, 50, 75, 114.1791045, 216.0447761, 286.1940299 ]) # in Kelvin
cool = np.array([0, 50, 100, 150, 200, 250 ]) # in watts
extemp = np.linspace(temp[0], temp[-1], 100)
fit = lambda T, a, b: a*(T-b)**0.5
p=np.array([15.64785214,31.34328358])

plt.plot(temp, cool, label='Green et al.', linestyle='none', marker='o')
plt.plot(extemp, fit(extemp, *p), label = 'fit: {0:.2f} ( T - {1:.2f} )^0.5'.format(*p) )
plt.legend()
plt.xlabel('1st Stage Temperature (K)')
plt.ylabel('Cooling Power (W)')
plt.show()