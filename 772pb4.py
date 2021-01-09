#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct  4 20:38:06 2020

@author: shousakai
"""
import numpy as np
from math import log, exp, sqrt
from scipy.stats import norm

sigma = 0.25
s_target = 0.5

a = 140
b = 150
T = 4
r = 0.05
V_0 = 120

def spread(D):
    d1 = (log(V_0/D) + (r + sigma ** 2 / 2) * T) / (sigma * sqrt(T))
    d2 = d1 - sigma * sqrt(T)
    
    S = -log(norm.cdf(d2) + V_0/(D * exp(-r * T)) * norm.cdf(-d1)) / T
    
    return S

def reverse_spread(s_target, epsilon, a, b):
    x = (a + b) / 2
    s = spread(x)
    while abs(s - s_target) > epsilon:
        s = spread(x)
        if s > s_target:
            b = x
        else:
            a = x
        x = (b + a) / 2
    
    return x
