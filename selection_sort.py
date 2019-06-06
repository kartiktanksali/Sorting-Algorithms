#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun  5 18:29:39 2019

@author: kartiktanksali
"""

#Selection Sort

def selectionSort(lst):
    
    for i in range(len(lst)):
        ind = i
        for j in range(i,len(lst)):
            if lst[j] < lst[ind]:
                ind = j
        
        temp = lst[ind]
        lst[ind] = lst[i]
        lst[i] = temp
    
    
    return lst






lst = [5,6,2,1,3,7,2,4]

res = selectionSort(lst)

print(res)