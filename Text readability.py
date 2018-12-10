# -*- coding: utf-8 -*-
"""
Created on Mon Dec 10 14:48:09 2018

@author: conno
"""
#Where
    #W is the number of words.
    #P is the number of full stops.
    #L is the number of long words (more than 6 letters).

def readability(text):
    
    if text.count(".") > 0:
        P = text.count(".")
        x = text.replace('.','')
        L = len([word for word in x.split() if len(word)>6])
        W = len(text.split())
        LIX = W/P + (L*100)/W
    else:
        LIX = 0 
    return LIX
        
        
