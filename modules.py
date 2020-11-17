# -*- coding: utf-8 -*-
"""
Created on Thu Nov  5 11:44:10 2020

@author: super

modules for the fourier series solver program
"""

import math
import matplotlib
from sympy import *

x, y, z = symbols('x y z')
init_printing(use_unicode=True)

def base_function(x):
    return x**3
