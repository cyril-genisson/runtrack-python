#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
@author: Cyril Génisson

@file: job4.py
@created: 24/11/2023

@project: 
@licence: GPLv3
"""

def tapis(n: int) -> None:
    cloture = "+" + "-" * n + "+"
    print(f"{cloture}")
    for k in range(n):
        interieur = "#" * (n-k-1) + " " + "#" * k
        print(f"|{interieur}|")
    print(f"{cloture}")

tapis(10)
