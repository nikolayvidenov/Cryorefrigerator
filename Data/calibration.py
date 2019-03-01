import numpy as np
from astropy.io import ascii

# Generic method for applying the temperature calibartion function to a LakeShore thermometer
# LakeShore provides a  set of 5-10 coefficients which make up the coefficients of
# a fourier serices:

#   Temp(K) = S from 0 to i A_i * cos( i * arccos( k ))
# where the sum is over the coefficients, A_i are the coefficients
# and k = (( Z - ZL ) - ( ZU - Z ) ) / ( ZU - ZL )
# finally ZU and ZL are provided along with the coefficients and
# Z = log(R)
def tempfit(R, T, ZL, ZU):
    Z = np.log10(R)
    k = ((Z - ZL) - (ZU - Z))/(ZU-ZL)
    temp = 0
    for i in range(0, len(T)-1, 1):
        temp += T[i] * np.cos(i*np.arccos(k))
    return temp

# the following functions just define the coefficients taken from calibration documents
def X58257_4to24(R):
    T = [ 1.20031724366835E+01, -1.12634514115660E+01, 3.53694869483886E+00,\
        -7.81795386431073E-01, 1.09059334811546E-01, -4.53105197564518E-03,\
        -2.95796956432681E-04, -6.04635137473733E-04]
    ZL = 2.91940388806204
    ZU = 4.04054290499423
    return tempfit(R, T, ZL, ZU)

def X58257_24to110(R):
    T=[ 6.38282756140952E+01, -5.28071750699773E+01, 1.16878683490819E+01,\
    -1.73342447227213E+00, 1.77953666999213E-01, -6.90293138329567E-03,\
     1.12079862637973E-03, -1.47949739369935E-03, 1.30350676249440E-03]
    ZL =  2.22357474802502
    ZU = 3.04185995811886
    return tempfit(R, T, ZL, ZU)

def X58257_110to300(R):
    T=[ 1.93830156036307E+02, -1.14835289007890E+02, 1.84780332799354E+01,\
        -2.55114925433003E+00, 4.19103852924763E-01, -6.76001406366582E-02,\
         8.49386872681845E-03]
    ZL = 1.81269740614386
    ZU = 2.36401397921259
    return tempfit(R, T, ZL, ZU)

def X58257(R):
    if R <= 198.8031:
        return X58257_110to300(R)
    elif R <= 949.4923:
        return X58257_24to110(R)
    else: return X58257_4to24(R)

def X93305_1to14(R):
    T = [5.46111576871146E+00, -6.30052799467719E+00, 2.85824550762532E+00,\
         -1.08745211808566E+00, 3.49619972271653E-01, -9.13295907979604E-02,\
         1.62535845472240E-02, 5.16791487218548E-05, -1.46252587347450E-03,\
         1.14054283784156E-03]
    ZL = 2.95404664088527
    ZU = 4.4284954224139
    return tempfit(R, T, ZL, ZU)

def X93305_14to80(R):
    T = [4.25469467007750E+01, -3.78062350504343E+01, 8.41427988033905E+00,\
    -1.06261334220296E+00, 1.14208943536034E-01, -5.48180734258386E-03,\
    -5.77014325190617E-03, -1.92631864027111E-04, 7.98216698629609E-04]
    ZL = 2.35709142372795
    ZU = 3.04941914260006
    return tempfit(R, T, ZL, ZU)

def X93305_80to325(R):
    T = [ 1.77272379515581E+02, -1.26992463544615E+02, 2.22030747464721E+01,\
    -2.97563290878801E+00, 5.38760490281655E-01, -1.01454406450543E-01,\
     1.10821019897944E-02, -2.94363278324194E-03]
    ZL = 1.83755142483125
    ZU = 2.45032404300377
    return tempfit(R, T, ZL, ZU)

def X93305(R):
    if R <= 251.8228:
        return X93305_80to325(R)
    elif R <= 994.487:
        return X93305_14to80(R)
    else: return X93305_1to14(R)

# Coefficients for Temp = 10**( sum_i a_i*(log(R))**i) where i sums over coefficients and
# the first row from the top is i = 0
X538_table = ascii.read('X538 Calibration Coefficients.txt', data_start=2, header_start=1)

def X538(R, thermometer):
    f = np.poly1d(X538_table[thermometer])
    return 10**( f(np.log10(R)) )

def X53853(R):
    return X538(R, 'X53853')

def X53851(R):
    return X538(R, 'X53851')

def X53871(R):
    return X538(R, 'X53871')
