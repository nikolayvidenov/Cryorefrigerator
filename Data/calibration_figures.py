# coding: utf-8
import numpy as np
import matplotlib.pyplot as plt
from astropy.io import ascii
from astropy.table import Table
from calibration import *



def medfilt(A, n):
    temp = []
    for i in range(n, len(A) - n, 1):
        temp.append( np.median(A[i -n//2:i+n//2]) )
    return temp
def avgfilt(A, n):
    temp = []
    for i in range(n, len(A)-n, 1):
        temp.append(np.average(A[i-n:i+n]))
        if temp[-1] == 'nan':
            print(i)
    return temp

cali = ascii.read('calibration_tabl.txt')
Temp = np.array(list(map(X58257, cali.columns[1])))

fig = plt.figure()
ax = fig.add_subplot(1,1,1)

#ax.plot(cali.columns[0], Temp, marker='o', label='X58257')
#ax.plot(cali.columns[0], medfilt(Temp, 3), marker='.')
ax.plot(Temp, marker = '.',label='a')
ax.plot(medfilt(Temp, 1), marker='.',label='b')
t = avgfilt(Temp, 1)
ax.plot(t, marker='.',label='c')
#t = avgfilt(medfilt(Temp, 1),1)
#ax.plot(t, marker='.',label='d')


#
#for column in cali.colnames[2:]:
#
#    coef  = np.polyfit(np.log10(medfilt(cali[column], 3)),np.log10(medfilt(Temp, 3)), 6)
#    coefficents[column] = coef
#    fit = np.poly1d(coef)
#    T = lambda R: 10**(fit(np.log10(R)))

ax.set_ylabel('Temperature (K)')
ax.set_xlabel('Time (s)')
ax.set_xlim([0, 500])
ax.legend()
fig.show()

