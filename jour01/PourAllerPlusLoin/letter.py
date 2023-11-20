#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
@author: Cyril Génisson

@file: letter.py
@created: 20/11/2023

@project: 
@licence: GPLv3
"""

def recherche(s: str, c: str) -> None:
    """ Recherche si un caratère c est présente dans une chaine
    de caractères s et affiche les positions du caractère dans la
    chaîne.
    s: str
    c: str
    """
    l = []
    
    for k in range(len(s)):
        if s[k] == c:
            l.append(k)

    if len(l) != 0:
        print(f"Le caractère {c} est présent dans la chaîne.")
        print("Position du caractère dans la chaîne: ")
        for k in range(len(l)):
            print(f"{l[k] + 1}", end=" ")
        print()
    else:
        print(f"Le caractère {c} n'est pas présent dans la chaîne.")
        print()


chaine1 = ",dslmdsjcqdfqjsdufiojdsqpojfdiosqjfiosjipfioqsdoiidosjijs"
chaine2 = "zeaoeiazepuiazoupoazeupiezapeauioazueiopazuepoazi"

recherche(chaine1, 'e')
recherche(chaine2, 'e')
