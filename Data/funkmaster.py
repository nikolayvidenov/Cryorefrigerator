from astropy.io import ascii
import matplotlib.pyplot as plt
import numpy as np

run1 = ascii.read('19022019 First Cooldown Clean.txt')
run2 = ascii.read('calA cleaner.txt')
run3 = ascii.read('25022019 Cal X538--.txt')

fig = plt.figure()
ax = fig.add_subplot(1,1,1)

ax.plot(run1['Time (s)']/3600, run1['Temp (Ohm) (X58257)'], label='19022019 First Cooldown')
ax.plot(run2['Time (s)']/3600, run2['Temp (Ohm) (X58257)'], label='calA')
ax.plot(run3['Time (s)']/3600, run3['Temp (Ohm) (X58257)'], label='25022019 Super Insulation')

ax.set_ylim([0, 3800])
ax.set_xlabel('Time (hours)')
ax.set_ylabel('Temperature (Ohm) (X58257)')
ax.legend()
fig.show()

fig2 = plt.figure()
ax2 = fig2.add_subplot(1,1,1)


def cali_4to24(R):

    T = [12.003172, -11.263451, 3.536949, -0.781795, 0.109059, -0.004531, -0.000296, -0.000605]
    ZL = 2.91940388806
    ZU = 4.04054290499
    Z = np.log10(R)
    k = ((Z - ZL) - (ZU - Z))/(ZU-ZL)
    temp = 0
    for i in range(0, 8, 1):
        temp += T[i] * np.cos(i*np.arccos(k))
    return temp
def cali_24to110(R):

    T = [63.828276, -52.807175, 11.687868, -1.733424, 0.177954, -0.006903, 0.001121, -0.001479, 0.001304]
    ZL =  2.22357474803
    ZU = 3.04185995812
    Z = np.log10(R)
    k = ((Z - ZL) - (ZU - Z))/(ZU-ZL)
    temp = 0
    for i in range(0, 9, 1):
        temp += T[i] * np.cos(i*np.arccos(k))
    return temp
def cali_110to300(R):

    T=[193.830156, -114.83528, 18.478033, -2.551149, 0.419104, -0.06760, 0.008494]
    ZL = 1.81269740614
    ZU = 2.36401397921 
    Z = np.log10(R)
    k = ((Z - ZL) - (ZU - Z))/(ZU-ZL)
    temp = 0
    for i in range(0, 7, 1):
        temp += T[i] * np.cos(i*np.arccos(k))
    return temp

def temp(R):
    if R <= 198.8:
        return cali_110to300(R)
    elif R <=949.5:
        return cali_24to110(R)
    else: return cali_4to24(R)

t1 = list(map(temp, list(run1['Temp (Ohm) (X58257)'])))
t2 = list(map(temp, list(run2['Temp (Ohm) (X58257)'])))
t3 = list(map(temp, list(run3['Temp (Ohm) (X58257)'])))

ax2.plot(run1['Time (s)']/3600,t1, label='19022019 First Cooldown')
ax2.plot(run2['Time (s)']/3600,t2, label='calA')
ax2.plot(run3['Time (s)']/3600,t3, label='25022019 Super Insulation')


ax2.set_xlabel('Time (hours)')
ax2.set_ylabel('Temperature (K) (X58257)')
ax2.set_xlim([0, 2])
ax2.legend()
fig2.show()


