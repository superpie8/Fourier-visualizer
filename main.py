# -*- coding: utf-8 -*-
"""
Created on Thu Nov  5 11:45:03 2020

@author: super

Solves and plots fourier series and the input function
"""
import math
import matplotlib
from sympy import *
import modules as m
    
x, y = symbols('x y')
init_printing(use_unicode=True)

function = input("Input Function: ")
pfunction = function.replace("x", "pi*x/L")
pfunction = sympify(function)
L = input("L (Interval=[-L, L]): ")
L = float(L)

a0 = 1/L * float(integrate(pfunction * L/x, (x, -L, L)))

print(a0)