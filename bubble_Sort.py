#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun  5 20:40:53 2019

@author: kartiktanksali
"""

#Bubble Sort
import time

def bubbleSort(lst):
    
    
    for i in range(len(lst)):
        flag = False
        for j in range(len(lst)-i-1):
            if lst[j] > lst[j+1]:
                temp = lst[j+1]
                lst[j+1] = lst[j]
                lst[j] = temp
                flag = True
        if flag == True:
            return lst

    return lst
    
lst = [1,2,3,4,5,7,6]
start_time = time.time()
res = bubbleSort(lst)
print("--- %s seconds ---" % (time.time() - start_time))
print(res)