# -*- coding: utf-8 -*-
"""
Created on Mon Dec 10 15:52:09 2018

@author: conno
"""

import numpy as np


def dataparser(data):
    if data[0] == 0 and np.size(data[2:]) >= 2:
        parsed = data[2:]
        parsed = parsed[0:data[1]]
    elif data[0] == 1 and np.size(data[3:]) >= 3:
        parsed = data[3:]
        if np.size(parsed) < data[1] or np.size(parsed) < data[2]:
            parsed = np.array([])
        else:
            parsed = np.resize(parsed,(data[1],data[2]))
    else:
        parsed = np.array([])
    return parsed