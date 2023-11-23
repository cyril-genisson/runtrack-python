#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
@author: Cyril Génisson

@file: job13.py
@created: 23/11/2023

@project: 
@licence: GPLv3
"""
from mylib import *

L = [10, 20, 30, 20, 10, 50, 60, 40, 80, 50, 40]
Lmin, Lrg = mini(L)
l = [Lmin]

print(L)

for k in range(my_len(L)):
    Lmin, Lrg = mini(L)
    lmax, lrg = maxi(l)
    if lmax != Lmin:
        l.append(L.pop(Lrg))
    else:
        L.pop(Lrg)

print(l)
