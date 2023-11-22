#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
@author: Cyril Génisson

@file: job11.py
@created: 22/11/2023

@project: 
@licence: GPLv3
"""


def time_to_text(x: int) -> None:
    h, m= x // 60, x % 60
    print(f"{h} heures et {m} minutes")


time_to_text(49)
time_to_text(60)
time_to_text(890)
