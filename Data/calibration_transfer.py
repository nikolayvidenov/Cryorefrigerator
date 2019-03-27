# coding: utf-8
import numpy as np
import matplotlib.pyplot as plt
from astropy.io import ascii
from astropy.table import Table
from calibration import *


def medfilt(A, n):
    temp = []
    for i in range(n//2, len(A) - n//2, 1):
        temp.append( np.median(A[i -n//2:i+n//2]) )
    return temp

resistance = plt.figure()
temperatrue = plt.figure()
deviation = plt.figure()
goof = plt.figure()
ax = resistance.add_subplot(1,1,1)
ax2 = temperatrue.add_subplot(1,1,1)
ax3 = deviation.add_subplot(1,1,1)
ax4 = goof.add_subplot(1,1,1)



cali = ascii.read('calibration_tabl.txt')

Temp = np.array(list(map(X58257, cali.columns[1])))
coefficents = Table()

for column in cali.colnames[1:]:

    l = column.split('(')[-1].split(')')[0]


    ax.plot(cali.columns[0]/3600., cali[column], label=l)

    coef  = np.polyfit(np.log10(medfilt(cali[column], 3)),np.log10(medfilt(Temp, 3)), 6)
    coefficents[column] = coef
    fit = np.poly1d(coef)
    T = lambda R: 10**(fit(np.log10(R)))
    ax2.plot(cali.columns[0]/3600, T(cali[column]), label=l)
    ax3.plot(cali.columns[1], T(cali[column]), label=l)

    error=[]
    for x in range(0, len(Temp), 1):
        error.append(abs(Temp[x] - T(cali[column][x])))

    ax4.plot(Temp, error, label=l)


ax.set_ylabel(r'Resistance ($\Omega$)')
ax.set_xlabel('Time (Hours)')
ax.legend()
#resistance.show()

ax2.set_ylabel(r'Temperature (K)')
ax2.set_xlabel('Time (Hours)')
ax2.legend()
#temperatrue.show()

ax3.set_ylabel(r'Temperature (K)')
ax3.set_xlabel('Time (Hours)')
ax3.legend()
#deviation.show()

ax4.set_ylabel('Error (K)')
ax4.set_xlabel('Temperature (K)')
ax4.legend()
#goof.show()
