#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 10 19:55:22 2019

@author: kartiktanksali
"""

#Insertion Sort

def selectionSort(lst):
    
    for i in range(1,len(lst)):
        val = lst[i]
        hole = i
        
        while(hole > 0 and lst[hole-1] > val):
            lst[hole] = lst[hole-1]
            hole -= 1
        
        lst[hole]=val
    
    return lst

lst = [5,6,2,1,3,7,2,4]
res = selectionSort(lst)
print(res)
        