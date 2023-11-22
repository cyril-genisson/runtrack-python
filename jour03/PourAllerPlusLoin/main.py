#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
@author: Cyril Génisson

@file: main.py
@created: 22/11/2023

@project: 
@licence: GPLv3
"""


def reverse_string(x: str) -> str:
    inv = ''
    for k in range(len(x) - 1, -1 , -1):
        inv += x[k]
    return inv

print(reverse_string('nikana'))
