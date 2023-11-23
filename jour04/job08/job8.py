#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
@author: Cyril Génisson

@file: job8.py
@created: 23/11/2023

@project: 
@licence: GPLv3
"""

L = [8, 24, 27, 48, 2, 16, 9, 7, 84, 91]

def AddParity(l: list) -> int:
    sum = 0
    for k in range(len(l)):
        if not (l[k] % 2):
            sum += l[k]
    return sum

print(f"Somme des valeurs paires de la liste {L} : {AddParity(L)}")

