#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 20 21:37:59 2020

@author: Yuyang Zhang
"""

import numpy as np
import matplotlib.pyplot as plt

sigma_V = 0.2
r = 0.04
V_0 = 12.5
D = 10
T = 2

def simulate_V(steps):
    h = T / steps
    dw = np.random.normal(size = steps)
    dw = np.append(0, dw)
    logV = np.array([(r-sigma_V**2/2)*h*i + sigma_V*sum(dw[:i+1])*np.sqrt(h) for i in range(steps+1)])
    
    V = V_0 * np.exp(logV)
    
    return V

def default_prob(M, steps, rho):
    K1 = rho * D * np.exp(-r * T)
    a = 0
    for i in range(M) :
        V = simulate_V(steps)
        if min(V) < K1:
            a += 1
        elif V[-1] < D:
            a += 1
    
    return a/M

        
    
