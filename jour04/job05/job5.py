#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
@author: Cyril Génisson

@file: job5.py
@created: 23/11/2023

@project: 
@licence: GPLv3
"""

def CreateList() -> list:
    L =[ k for k in range(1, 6)]
    print(L)
    print(L[1])
    return L

def ModifList(l: list) -> list:
    l[3] = l[2] + l[4]
    print(l)
    print(l[4])
    return l

ModifList(CreateList())
