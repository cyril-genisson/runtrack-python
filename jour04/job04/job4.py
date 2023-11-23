#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
@author: Cyril Génisson

@file: job4.py
@created: 23/11/2023

@project: 
@licence: GPLv3
"""

l = ['pomme', 'cerise', 'orange', 'Melon']

def main(liste: list) -> list:
    liste[2] = 'Mangue'
    return liste

print(main(l))
