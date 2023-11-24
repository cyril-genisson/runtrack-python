#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
@author: Cyril Génisson

@file: job3.py
@created: 24/11/2023

@project: 
@licence: GPLv3
"""

def triangle(n: int) -> None:
    for k in range(n - 1):
        space = "/" + "  " * k + "\\"
        print(f"{space: ^{n*2}}")
    space = "_" * (n-1) * 2
    print(f"/{space}\\")

n = int(input("Entrer un entier strictement positif: "))
triangle(n)
