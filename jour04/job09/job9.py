#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
@author: Cyril Génisson

@file: job9.py
@created: 23/11/2023

@project: 
@licence: GPLv3
"""

L = [8, 24, 27, 48, 2, 16, 9, 102, 7, 84, 91]

def extremum(l: list) -> None:
    maxi, mini = max(l), min(l)
    return (maxi, mini)

maxi, mini = extremum(L)
print(f"la valeur max est: {maxi}")
print(f"la valeur min est: {mini}")
