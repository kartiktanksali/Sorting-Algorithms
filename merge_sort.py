#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 11 00:06:41 2019

@author: kartiktanksali
"""

#Merge Sort


def Merge(llst,rlst,lst):
    
    i = 0
    j = 0
    k = 0
    
    while(i < len(llst) and j < len(rlst)):
        
        if llst[i] <= rlst[j]:
            lst[k] = llst[i]
            i += 1
            k += 1
        elif rlst[j] <= llst[i]:
            lst[k] = rlst[j]
            j += 1
            k += 1
    
    while(i<len(llst)):
        lst[k] = llst[i]
        i += 1
        k += 1
    
    while(j<len(rlst)):
        lst[k] = rlst[j]
        j += 1
        k += 1


def MergeSort(lst):
    
    if len(lst) < 2:
        return "No need to sort the list"
    else:
        mid = int(len(lst)/2)
        llst = list(range(mid))
        rlst = list(range(len(lst)-mid))

        
        for i in range(mid):
            llst[i] = lst[i]
        
        for i in range(mid,len(lst)):
            rlst[i-mid] = lst[i]

        MergeSort(llst)
        MergeSort(rlst)
        
        Merge(llst,rlst,lst)
    
    return lst


lst = [5,6,2,1,3,7,2,4,9]
res = MergeSort(lst)
print(res)