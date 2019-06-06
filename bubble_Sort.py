#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun  5 20:40:53 2019

@author: kartiktanksali
"""

#Bubble Sort

def bubbleSort(lst):
    
    
    for i in range(len(lst)):
        flag = False
        for j in range(len(lst)-i-1):
            if lst[j] > lst[j+1]:
                temp = lst[j+1]
                lst[j+1] = lst[j]
                lst[j] = temp
                flag = True
        if flag == False:
            return lst

    return lst
    
lst = [5,6,2,1,3,7,2,4]
res = bubbleSort(lst)
print(res)