# -*- coding: utf-8 -*-
"""
Author: Caleb Malaer
Created: 11/05/2020
Last Edit: 11/19/2020

Solves for and plots fourier series and the input function
"""

from modules import *


function = str(input("Input Function: "))
"""pfunction = function.replace("x", "(x * L / pi)")"""
pfunction = function.replace("^", "**")
pfunction = sympify(pfunction)

"""pprint(pfunction)"""

L = input("L (Interval=[-L, L]): ")
L = sympify(L)

a0 = 1/(2*L) * integrate(pfunction, (x, -L, L))
an = 1/L * integrate(pfunction * cos(z * x * pi / L), (x, -L, L), conds='none')
bn = 1/L * integrate(pfunction * sin(z * x * pi / L), (x, -L, L), conds='none')
"""print(a0, "|", an, "|", bn)"""

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

series = sympify(series)
print("\n", "\n", "Series:  ", "\n")
pprint(series)

F = plot(pfunction, (x,-L, L), show = False, line_color = "black")
P = plot(series, (x,-L, L), show = False, line_color = "red")

P.append(F[0])
P.show()