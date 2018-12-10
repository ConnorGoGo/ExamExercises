# -*- coding: utf-8 -*-
"""
Created on Mon Dec 10 19:07:32 2018

@author: conno
"""

import numpy as np

W = np.array([])
def temperaturemonitor(T):
    W = np.zeros(np.size(T))
    for i in range(np.size(T)):
        if T[i] > T[i-1]+2 or T[i] < T[i-1]-2:
            W[i] = 1
        if T[i] < 0 and T[i-1] < 0:
            W[i] = 2
        if T[i] > 5 and T[i-1] > 5:
            W[i] = 3
        if i == 0:
            W[0] = 0

    return W