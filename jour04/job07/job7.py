#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
@author: Cyril Génisson

@file: job7.py
@created: 23/11/2023

@project: 
@licence: GPLv3
"""

L = [8, 24, 48, 2, 16]

def main(l: list) -> int:
    cpt = 0
    for k in range(len(l)):
        if not (l[k] % 3):
            cpt += 1
    return cpt

print(f"Nombre de multitples de 3 dans {L}: {main(L)}")
