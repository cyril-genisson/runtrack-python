#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
@author: Cyril Génisson

@file: job7.py
@created: 21/11/2023

@project: 
@licence: GPLv3
"""
chaine = [chr(k) for k in range(97, 123)] * 10

print(chaine[0])
for i in range(1, len(chaine), 2):
    for j in range(0, i+2):
        if j < len(chaine):
            print(chaine[j], end="")
    print()
