#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
@author: Cyril Génisson

@file: job10.py
@created: 23/11/2023

@project: 
@licence: GPLv3
"""
L = [8, 24, 27, 48, 2, 16, 9, 102, 7, 84, 91]

def mutli(l: list) -> int:
    m = 1
    for k in range(len(l)):
        if (l[k] >= 25) and (l[k] <= 90):
            m *= l[k]
    return m

print(f"Produit des valeurs de la liste compris entre 25 et 90: {multi(L)}")
