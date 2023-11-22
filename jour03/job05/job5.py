#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
@author: Cyril Génisson

@file: job5.py
@created: 22/11/2023

@project: 
@licence: GPLv3
"""


def calcul(num1: float, operator: str, num2: float) -> float:
    match operator:
        case '+':
            return num1 + num2
        case '-':
            return num1 - num2
        case '*':
            return num1 * num2
        case '/':
            return num1 / num2
        case '//':
            return int(num1) // int(num2)
        case '%':
            return int(num1) % int(num2)

for op in ['+', '-', '*', '/', '//', '%']:
    for i in range(1, 5):
        for j in range(1, 5):
            print(f"{i} {op} {j} = {calcul(i, op, j)}")
