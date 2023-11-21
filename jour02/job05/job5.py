#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
@author: Cyril Génisson

@file: job5.py
@created: 21/11/2023

@project: 
@licence: GPLv3
"""
def div(n: int, p: int) -> bool:
    if n % p == 0:
        return True
    else:
        return False

for k in range(1, 101):
    if div(k, 3) and div(k, 5):
        print("FizzBuzz")
    elif div(k, 3):
        print("Fizz")
    elif div(k, 5):
        print("Buzz")
    else:
        print(k)

