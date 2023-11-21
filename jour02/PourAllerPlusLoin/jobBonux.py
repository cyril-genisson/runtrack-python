#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
@author: Cyril Génisson

@file: jobBonux.py
@created: 21/11/2023

@project: 
@licence: GPLv3
"""
from math import sqrt

def pyth(l: list) -> bool:
    if (l[2]**2 == l[1]**2 + l[0]**2):
        return True
    else:
        return False

def iso(l: list) -> bool:
    if (l[0] == l[1]) or (l[0] == l[2]) or (l[1] == l[2]):
        return True
    else:
        return False

def existe(l: list) -> bool:
    if (l[0] +l[1] > l[2]):
        return True
    else:
        return False

triangle = []
for k in range(3):
    triangle.append(float(input("Entrer un nombre strictement positif: ")))

triangle = sorted(triangle)
if existe(triangle):
    if pyth(triangle) and iso(triangle):
        print("Le triangle existe et il est rectangle isocèle.")
    elif pyth(triangle):
        print("Le triangle existe et il est rectangle.")
    elif iso(triangle):
        print("Le triangle existe et il est isocèle.")
    else:
        print("Le triangle existe et il est quelconque.")
else:
    print("Le triangle n'est pas constructible")

