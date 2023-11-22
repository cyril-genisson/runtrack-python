#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
@author: Cyril Génisson

@file: job9.py
@created: 22/11/2023

@project: 
@licence: GPLv3
"""

def moyenne(x: float, y: float, z: float) -> None:
    return (x + y + z) / 3.

def main() -> None:
    n1 = float(input("Entrer la 1ère note: "))
    n2 = float(input("Entrer la 2ème note: "))
    n3 = float(input("Entrer la 3ème note: "))

    moyenne_etudiant = moyenne(n1, n2, n3)

    if moyenne_etudiant < 8:
        print("Elève devant faire des efforts.")
    elif moyenne_etudiant < 11:
        print("Elève moyen.")
    elif moyenne_etudiant < 15:
        print("Bon élève.")
    else:
        print("Très bon élève.")

main()

