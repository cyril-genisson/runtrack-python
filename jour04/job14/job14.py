#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
@author: Cyril Génisson

@file: job14.py
@created: 23/11/2023

@project: 
@licence: GPLv3
"""
from mylib import *

string="La peur est le chemin vers le côté obscur, la peur mène à la colère, la colère mène à la haine, la haine mène à la souffrance"

def my_long_word(x: int, s: str) -> str:
    L = string.split()
    l = []
    for k in range(my_len(L)):
        if my_len(L[k]) > x:
            l.append(L[k])
    return (' ').join(l)

print(my_long_word(3, string))
