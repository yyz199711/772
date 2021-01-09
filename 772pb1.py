#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 12 18:41:36 2020

@author: Yuyang Zhang
"""
import numpy as np

import seaborn as sns
import matplotlib.pyplot as plt


N = 10000

def f_inverse_1(u) :
    if 0 <= u < 1 - np.exp(-0.25) :
        return 20 * np.sqrt(-np.log(1-u))
    else:
        return 5 - 20 * np.log(1-u)
    

def f_inverse_2(u) :
    return -20 * np.log(1-u)
        
u = np.random.uniform(0,1,N)

T1 = np.zeros(N)
T2 = np.zeros(N)

for i in range(N) :
    # print(i)
    T1[i] = f_inverse_1(u[i])
    T2[i] = f_inverse_2(u[i])
    
sns.set_palette("hls")
sns.distplot(T1, color="r", bins = 30, kde=True)
plt.xlabel("T")
plt.ylabel("Frequency")
plt.title("For Hazard Function Which is Piecewise")
plt.show()

sns.distplot(T2, color="r", bins = 30, kde=True)
plt.xlabel("T")
plt.ylabel("Frequency")
plt.title("For Hazard Function Which is Constant")

plt.show()

print(sum(T1)/N)
print(sum(T2)/N)


    
