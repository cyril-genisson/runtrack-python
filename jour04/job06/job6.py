#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
@author: Cyril Génisson

@file: job6.py
@created: 23/11/2023

@project: 
@licence: GPLv3
"""

l = [ k for k in range(1, 6)]

def main(liste: list) -> list:
    liste[0], liste[len(liste) - 1] = liste[len(liste) - 1], liste[0]
    return liste

print(l)
print(main(l))
