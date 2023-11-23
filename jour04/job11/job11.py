#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
@author: Cyril Génisson

@file: job11.py
@created: 23/11/2023

@project: 
@licence: GPLv3
"""
L = [7, 11, 42, 39, 2]

print(f"Liste initiale:{L}")

for k in range(len(L)):
    L[k] += 1

print(f"Liste modifiée:{L}")
