from astropy.io import ascii
import matplotlib.pyplot as plt
from calibration import *

run = ascii.read('27022019 Troubleshooting Run', format='csv')
run0 = ascii.read('19022019 First Cooldown Clean.txt', format='csv')
run1 = ascii.read('run01032019_clean.txt', format='csv')

fig = plt.figure()
ax = fig.add_subplot(1,1,1)

Sheild55K1 = list(map(X53871, run1['Temp (Ohm) (X53871)']))
Plate55K1 = list(map(X53851, run1['Temp (Ohm) (X53851)']))
Stage4K1 =  list(map(X93305, run1['Temp (Ohm) (X93305)']))
Stage55K1 = list(map(X58257, run1['Temp (Ohm) (X58257)']))

Sheild55K = list(map(X53871, run['Temp (Ohm) (X53871) (55K Shield)']))
Plate55K = list(map(X53851, run['Temp (Ohm) (X53851) (55K Al Plate)']))
Stage4K =  list(map(X93305, run['Temp (Ohm) (X93305) (4K Stage)']))
Stage55K = list(map(X58257, run['Temp (Ohm) (X58257) (55K Stage)']))

Stage4K2 = list(map(X58257, run0['Temp (Ohm) (X58257)']))

ax.plot( run['Time (s)']/3600-.3, Sheild55K, label=r'Sheild; Super Insulation')
ax.plot( run1['Time (s)']/3600-.9, Sheild55K1, label=r'Sheild; Better Cables')

ax.plot( run['Time (s)']/3600-.3, Stage55K, label=r'Stage; Super Insulation')
ax.plot( run1['Time (s)']/3600-.9, Stage55K1, label=r'Stage; Better Cables')

ax.set_ylabel('Temperature (K)')
ax.set_xlabel('Time (Hours)')

ax.legend()
fig.show()
