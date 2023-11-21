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

for i in range(len(chaine)):
    for j in range(i):
        print(chaine[j], end="")
    print()
