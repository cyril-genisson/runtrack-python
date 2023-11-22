#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
@author: Cyril Génisson

@file: job6.py
@created: 22/11/2023

@project: 
@licence: GPLv3
"""

def sign(x: float) -> None:
    if x < 0:
        print("Négatif")
    else:
        print("Positif")

sign(-1.5)
sign(9.3)
