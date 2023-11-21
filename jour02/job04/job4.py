#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
@author: Cyril Génisson

@file: job4.py
@created: 21/11/2023

@project: 
@licence: GPLv3
"""

def mutliplication(n: int) -> None:
    print(f"Table de multiplication de {n}: ")
    for j in range(1, 11):
        print(f"{n} X {j} = {n*j}")
    print()

rep = int(input("Entrez un entier supérieur à zéro (N): "))
for k in range(1, rep + 1):
    mutliplication(k)
