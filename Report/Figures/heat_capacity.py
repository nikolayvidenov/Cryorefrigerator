import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit

temp = np.array([4, 6, 8, 10, 12, 14, 16, 18, 20, 30, 40, 50, 60, 70, 80, 90, 100, 120, 140, 160, 180, 200, 220, 240, 260, 280, 300 ]) # in Kelvin
C_Al = np.array([0.292, 0.6047, 1.048, 1.573, 2.268, 3.235, 4.581, 6.416, 8.854, 33.45, 81.96, 148.8, 223.6, 298.3, 368.7, 433.3, 492.2, 594.1, 677.6, 744.5, 796.4, 835.2, 863.7, 885.4, 904.6, 925.8, 953.9 ]) # in J K/mol?
C_Cu = np.array([0.09942, 0.2303, 0.4639, 0.8558, 1.47, 2.375, 3.64, 5.327, 7.491, 26.4, 57.63, 95.84, 135.2, 171.8, 203.8, 230.9, 253.5, 287.6, 311.6, 329.4, 343.4, 355, 364.7, 372.6, 378.6, 382.5, 384 ])
extemp = np.linspace(temp[0], temp[-1], 100)



plt.plot(temp, cool, label='Green et al.', linestyle='none', marker='o')
plt.plot(extemp, fit(extemp, *p), label = 'fit: {0:.2f} ( T - {1:.2f} )^0.5'.format(*p) )
plt.legend()
plt.xlabel('1st Stage Temperature (K)')
plt.ylabel('Cooling Power (W)')
plt.show()