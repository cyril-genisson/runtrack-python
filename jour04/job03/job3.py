#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
@author: Cyril Génisson

@file: job3.py
@created: 23/11/2023

@project: 
@licence: GPLv3
"""

l = ['pomme', 'cerise', 'orange']

def main(liste: list) -> list:
    liste.append('Melon')
    return liste

print(main(l))
