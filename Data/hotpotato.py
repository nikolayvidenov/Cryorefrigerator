from astropy.io import ascii
import matplotlib.pyplot as plt
from calibration import *

run = ascii.read('27022019 Troubleshooting Run', format='csv')
run0 = ascii.read('19022019 First Cooldown Clean.txt', format='csv')

fig = plt.figure()
ax = fig.add_subplot(1,1,1)


Sheild55K = list(map(X53871, run['Temp (Ohm) (X53871) (55K Shield)']))
Plate55K = list(map(X53851, run['Temp (Ohm) (X53851) (55K Al Plate)']))
Stage4K =  list(map(X93305, run['Temp (Ohm) (X93305) (4K Stage)']))
Stage55K = list(map(X58257, run['Temp (Ohm) (X58257) (55K Stage)']))

Stage4K2 = list(map(X58257, run0['Temp (Ohm) (X58257)']))

ax.plot( run['Time (s)']/3600-.3, Stage4K, label=r'Super Insulation 4K Cold Head')

ax.plot( run0['Time (s)']/3600, Stage4K2, label=r'4K Cold Head')

ax.set_ylabel('Temperature (K)')
ax.set_xlabel('Time (Hours)')

ax.legend()
fig.show()
