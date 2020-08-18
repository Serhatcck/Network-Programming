# -*- coding: utf-8 -*-
"""
Created on Thu Aug  6 17:04:54 2020

@author: fikirsanat
"""

for i in range(32,128,32):
    print(' '.join(chr(j) for j in range(i, i+32)))