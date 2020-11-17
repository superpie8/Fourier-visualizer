# -*- coding: utf-8 -*-
"""
Created on Thu Nov  5 11:45:03 2020

@author: super

Solves and plots fourier series and the input function
"""

from modules import *


function = str(input("Input Function: "))
"""pfunction = function.replace("x", "(x * L / pi)")"""
pfunction = function.replace("^", "**")
pfunction = sympify(pfunction)

pprint(pfunction)

L = input("L (Interval=[-L, L]): ")
L = sympify(L)

a0 = 1/(2*L) * integrate(pfunction, (x, -L, L))
an = 1/L * integrate(pfunction * cos(z * x * pi / L), (x, -L, L), conds='none')
bn = 1/L * integrate(pfunction * sin(z * x * pi / L), (x, -L, L), conds='none')
print(a0, "|", an, "|", bn)

sterm = bn * sin(z * x * pi / L)
cterm = an * cos(z * x * pi / L)

series = str(a0)
N = int(input("Number of terms: "))
n = 1
cterm = str(cterm)
sterm = str(sterm)

while n <= N: 
    r = str(n)
    series += " + "
    series += cterm.replace("z", r)
    series += " + "
    series += sterm.replace("z", r)
    n += 1
    print(series)

series = sympify(series)
print("\n")
pprint(series)