# coding: utf-8

import sympy
import numpy
import scipy
import scipy.integrate as integrate
from scipy.constants import *
th_d = h*c/(2*np.pi*k)*(6*pi**2*(NV))**(1/3.)
import numpy as np
copper_th_d = 343
aluminium_th_d = 428
c = lambda x: ( x**4.*np.exp(x) ) / ( np.exp(x)-1)**2
r = integrate.quad(c, 0, copper_th_d/300)
r
r[0]
r[0]*9* N_A*k *300**4/copper_th_d**3
x = np.linspace(4, 300, 16)
x
x = np.linspace(4, 300, 14)
x
x = np.linspace(4, 300, 15)
def c(T):
    r = integrate.quad(c, 0, copper_th_d/T)
    return r[0]*9*N_A*k*(T/ copper_th_d)**3
N_A
k
y = np.array(map(c, x))
def c(T):
    print T
    r = integrate.quad(c, 0, copper_th_d/T)
    return r[0]*9*N_A*k*(T/ copper_th_d)**3
y = np.array(map(c, x))
for i in x:
    print i
    
y = []
for i in x:
    print i
    y.append(c(i))
    
: c = lambda x: ( x**4.*np.exp(x) ) / ( np.exp(x)-1)**2

In [11]: r = integrate.quad(c, 0, copper_th_d/300)
: c = lambda x: ( x**4.*np.exp(x) ) / ( np.exp(x)-1)**2
c = lambda x: ( x**4.*np.exp(x) ) / ( np.exp(x)-1)**2
def C(T):
    print T
    r = integrate.quad(c, 0, copper_th_d/T)
    return r[0]*9*N_A*k*(T/ copper_th_d)**3
y = np.array(map(C, x))
y
x = np.linspace(4, 300, 25)
x
x = np.linspace(4, 300, 26)
x
x
y
C(10)
copper_th_d = 343.
C(10)
c = lambda x: ( x**4.*np.exp(x) ) / ( np.exp(x)-1)**2
y /= 0.063
y
y = np.array(map(C, x))
y
def C(T):
    print T
    r = integrate.quad(c, 0, copper_th_d/T)
    return r[0]*9*N_A*k*(T/ copper_th_d)**3/0.063
y = np.array(map(C, x))
y
C(100)
def C(T):
    print T
    r = integrate.quad(c, 0, copper_th_d/T)
    return r[0]*9*N_A*k*(T/ copper_th_d)**3
C(100)
C(300)
c = lambda x: ( x**4.*np.exp(x) ) / ( np.exp(x)-1)**2
C(1000)
C(100000)
3*N_A*k
C(1)
R 
N_A*K
N_A*k
12*np.pi**4/5
12*np.pi**4/5*(1/ copper_th_d)**3
12*np.pi**4/5*(1/ copper_th_d)**3*R
15/0.06
25/0.06
x = [4
6
8
10
12
14
16
18
20
30
40
50
60
70
80
90
100
120
140
160
180
200
220
240
260
280
300
]
x=[4, 6, 8, 10, 12, 14, 16, 18, 20, 30, 40, 50, 60, 70, 80, 90, 100, 120, 140, 160, 180, 200, 220, 240, 260, 280, 300]
y = np.array(map(C, x))
y
def C_Al(T):
    print T
    r = integrate.quad(c, 0, aluminium_th_d /T)
    return r[0]*9*N_A*k*(T/ aluminium_th_d)**3
def C_Al(T):
    print T
    r = integrate.quad(c, 0, aluminium_th_d /T)
    return r[0]*9*N_A*k*(T/ aluminium_th_d)**3/0.027
y = np.array(map(C_Al, x))
y
aluminium_th_d = 428.
y = np.array(map(C_Al, x))
u
y
