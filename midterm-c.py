# -*- coding: utf-8 -*-
"""
Created on Thu May  2 16:06:27 2019

@author: salam
"""


def tail_condition():
    
    dxu = xlist[1]-xlist[0]
    dyu = ylist[1]-ylist[0]
    mu = dyu/dxu 

    dxl = xlist[-2]-xlist[-1]
    dyl = ylist[-2]-ylist[-1]
    ml = dyl/dxl
    if abs(mu) == abs(ml):
        cond = print('The airfoil is pointed')
    else:
        cond = print('The airfoil is cusped')
    return cond
