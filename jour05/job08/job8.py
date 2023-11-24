#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
@author: Cyril Génisson

@file: job8.py
@created: 24/11/2023

@project: 
@licence: GPLv3
"""

def my_sort(l: list) -> list:
    """
    Je ne sais pas trop bien ce que je dois commenter
    puisqu'il s'agit d'un algorithme de tri à bulles
    bien connu et très peu efficace. Dans les faits,
    personne ne l'utilise à cause de sa complexité en
    O(n^2) en moyenne.
    """
    cpt = 0
    for i in range(len(l) - 1, 0, -1):
        for j in range(0, i):
            if l[j+1] < l[j]:
                l[j+1], l[j] = l[j], l[j+1]
                cpt += 1
    print(f"Nombre total de coups nécessaires pour trier la liste: {cpt}")
    print(f"Liste triée: {l}")
    return l

from random import randint
L = [randint(1, 100) for k in range(1, 8)]
my_sort(L)
