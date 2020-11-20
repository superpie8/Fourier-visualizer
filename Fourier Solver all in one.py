# -*- coding: utf-8 -*-
"""
Author: Caleb Malaer
Created: 11/05/2020
Last Edit: 11/19/2020
Python Ver: 3.7

Solves for and plots fourier series and the input function
"""

import math
import matplotlib
from sympy import *

x, y, z = symbols('x y z')
init_printing(use_unicode=True)


function = str(input("Input Function \n"))
"""pfunction = function.replace("x", "(x * L / pi)")"""
pfunction = function.replace("^", "**")
pfunction = sympify(pfunction)

"""pprint(pfunction)"""

L = input("L (Interval=[-L, L])  \n")
L = sympify(L)

a0 = 1/(2*L) * integrate(pfunction, (x, -L, L))
an = 1/L * integrate(pfunction * cos(z * x * pi / L), (x, -L, L), conds='none')
bn = 1/L * integrate(pfunction * sin(z * x * pi / L), (x, -L, L), conds='none')
"""print(a0, "|", an, "|", bn)"""

sterm = bn * sin(z * x * pi / L)
cterm = an * cos(z * x * pi / L)

series = str(a0)
N = int(input("Number of terms \n"))
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

k = str(input("Save plot?  y/n \n"))

if k == "y":
    filename = "./" + input("File name? \n")
    P.save(filename)

bruh = "8"
while bruh == "8":
    bruh = input("Press enter to exit")