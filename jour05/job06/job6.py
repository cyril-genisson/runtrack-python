#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
@author: Cyril Génisson

@file: job6.py
@created: 24/11/2023

@project: 
@licence: GPLv3
"""


def distance(x: int, y: int) -> float:
    return round((7 * x * y) / 10., 2)
x = int(input("Nombre de marches: "))
y = int(input("Hauteur d'une marche (en cm): "))
print(f"Pour {x} marches de {y} cm, le gradien parcours {distance(x, y): .2f} m par semaine.")
