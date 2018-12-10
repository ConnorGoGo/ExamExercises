# -*- coding: utf-8 -*-
"""
Created on Mon Dec 10 11:48:59 2018

@author: conno
"""

import numpy as np

def normrange(x, r):
    x = x.flatten()
    s = np.zeros([np.size(x)])
    if np.size(x) > 1:
        for i in range(np.size(x)):
            for item in x:
                if item > 1 or item < 0:
                    s[i] = (r[1]-r[0])*float((x[i]-min(x))/(max(x)-min(x)))+r[0]
                else:
                    s[i] = x[i]
    else:
        s = x
    return s