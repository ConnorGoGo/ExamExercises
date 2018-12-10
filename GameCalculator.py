# -*- coding: utf-8 -*-
"""
Created on Mon Dec 10 20:58:03 2018

@author: conno
"""

def gamecalculator(goals):
    #insert your code
    points = 0
    for i in range(len(goals[0,:])):
            if goals[0,i] == goals[1,i]:
                points += 1
            elif goals[0,i] > goals[1,i]:
                points += 3
            else:
                points += 0
    GF = goals[0,:].sum()
    GA = goals[1,:].sum()
    GD = GF - GA
    result = [points,GD]
    
    return result
