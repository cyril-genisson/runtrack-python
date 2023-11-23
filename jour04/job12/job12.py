#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
@author: Cyril Génisson

@file: job12.py
@created: 23/11/2023

@project: 
@licence: GPLv3
"""

def my_len(l: list) -> int:
    cpt = 0
    for k in l:
        cpt += 1
    return cpt


def mini(l: list) -> tuple:
    m, rg = l[0], 0

    for k in range(1, my_len(l)):
        if m > l[k]:
            rg, m = k, l[k]
    
    return m, rg 


def maxi(l: list) -> int:
    m = l[0]

    for k in range(1, my_len(l)):
        if m < l[k]:
            rg, m = k, l[k]

    return m, rg


def partition(l: list, start: int, end: int) -> int:
    while start < end:
        while start < end:
            if l[start] > l[end]:
                l[start], l[end] = l[end], l[start]
                break
            end -= 1
        while start < end:
            if l[start] > l[end]:
                l[start], l[end] = l[end], l[start]
                break
            start += 1
    return start


def my_sort(l: list) -> list:
    res = []

    for k in range(my_len(l)):
        m, rg = mini(l)
        res.append(m)
        l.pop(rg)

    return res


def my_bubblesort(l: list) -> list:
    for i in range(len(l) - 1, 0, -1):
        for j in range(0, i):
            if l[j+1] < l[j]:
                l[j+1], l[j] = l[j], l[j+1]

    return l


def quicksort(l:list, start=None, end=None) -> list:
    if start is None:
        start = 0
    if end is None:
        end = my_len(l)
    if start < end:
        i = partition(l, start, end-1)
        quicksort(l, start, i)
        quicksort(l, i+1, end)

    return l

