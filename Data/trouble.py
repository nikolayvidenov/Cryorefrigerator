from astropy.io import ascii
import matplotlib.pyplot as plt
from calibration import *

run = ascii.read('27022019 Troubleshooting Run', format='csv')

fig = plt.figure()
ax = fig.add_subplot(1,1,1)

HeStage = list(map(X93305, run['Temp (Ohm) (X93305) (4K Stage)']))
LNStage = list(map(X58257, run['Temp (Ohm) (X58257) (55K Stage)']))
Sheild55K = list(map(X53871, run['Temp (Ohm) (X53871) (55K Shield)']))
Plate55K = list(map(X53851, run['Temp (Ohm) (X53851) (55K Al Plate)']))

ax.plot( run['Time (s)']/3600, HeStage, label='55K Cold Head')
ax.plot( run['Time (s)']/3600, LNStage, label='4K Cold Head')
ax.plot( run['Time (s)']/3600, Sheild55K, label=r'55K Rad Sheild ($\pm7K$)')
ax.plot( run['Time (s)']/3600, Plate55K, label=r'55K Top Plate ($\pm7K$)')

ax.set_ylabel('Temperature (K)')
ax.set_xlabel('Time (Hours)')
ax.set_xlim([0, 21])
ax.legend()
fig.show()
