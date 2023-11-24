#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
@author: Cyril Génisson

@file: job2.py
@created: 24/11/2023

@project: 
@licence: GPLv3
"""

def draw_rectangle(width: int, height: int) -> None:
    c = "-" * (width - 2)
    space = " " * (width - 2)
    print(f"|{c}|")
    for k in range((height - 2)):
        print(f"|{space}|")
    print(f"|{c}|")

draw_rectangle(10, 3)
