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


cali = ascii.read('calibration_tabl.txt')
Temp = np.array(list(map(X58257, cali.columns[1])))

plt.plot(cali.columns[0], Temp)

coefficents = Table()

for column in cali.colnames[2:]:

    coef  = np.polyfit(np.log10(medfilt(cali[column], 3)),np.log10(medfilt(Temp, 3)), 6)
    coefficents[column] = coef
    fit = np.poly1d(coef)
    T = lambda R: 10**(fit(np.log10(R)))
    plt.plot(cali.columns[0], T(cali[column]))
    plt.show()
