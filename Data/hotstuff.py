from astropy.io import ascii
import matplotlib.pyplot as plt
from calibration import *

run = ascii.read('27022019 Troubleshooting Run', format='csv')
run2 = ascii.read('run01032019.txt')

fig = plt.figure()
ax = fig.add_subplot(1,1,1)


Sheild55K = list(map(X53871, run['Temp (Ohm) (X53871) (55K Shield)']))
Plate55K = list(map(X53851, run['Temp (Ohm) (X53851) (55K Al Plate)']))
Sheild55K2 = list(map(X53871, run2['col11']))
Plate55K2 = list(map(X53851, run2['col4']))

ax.plot( run['Time (s)']/3600, Sheild55K, label=r'55K Rad Sheild ($\pm7K$)')
ax.plot( run['Time (s)']/3600, Plate55K, label=r'55K Top Plate ($\pm7K$)')
ax.plot( run2['col1']/3600, Sheild55K2, label=r'run2 55K Rad Sheild ($\pm7K$)')
ax.plot( run2['col1']/3600, Plate55K2, label=r'run2 55K Top Plate ($\pm7K$)')

ax.set_ylabel('Temperature (K)')
ax.set_xlabel('Time (Hours)')

ax.legend()
fig.show()
