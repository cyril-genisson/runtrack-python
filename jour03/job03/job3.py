#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
@author: Cyril Génisson

@file: job3.py
@created: 22/11/2023

@project: 
@licence: GPLv3
"""


def Add(x: int, y: int) -> None:
    print(f"{x} + {y} = {x + y}")


for i in range(1, 5):
    for j in range(1, 5):
        Add(i, j)
