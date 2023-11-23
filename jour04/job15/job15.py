#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
@author: Cyril Génisson

@file: job15.py
@created: 23/11/2023

@project: 
@licence: GPLv3
"""
from mylib import *

L = [22.4, 4.0, 16.22, 9.10, 11.00, 12.22, 14.20, 5.20, 17.50]

def my_round(x: float) -> int:
    if x < (int(x) + 0.5):
        return int(x)
    else:
        return int(x) + 1

def my_int(l: list) -> list:
    for i in range(my_len(l)):
        l[i] = my_round(l[i])
    return l

print(L)
l = my_int(L)
print(l)
#print(l)
print(quicksort(l))
