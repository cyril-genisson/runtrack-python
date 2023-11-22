#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
@author: Cyril Génisson

@file: job10.py
@created: 22/11/2023

@project: 
@licence: GPLv3
"""


def parite(x: int) -> None:
    erreur = "Le nombre doit être un entier strictement positf"
    if type(x) == type(0):
        if x > 0:
            if x % 2:
                print("Le nombre est impair")
            else:
                print("Le nombre est pair")
        else:
            print(erreur)
    else:
        print(erreur)

parite("Hello")
parite(2.)
parite(-5)
parite(5)
parite(6)
