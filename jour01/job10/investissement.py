#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
@author: Cyril Génisson

@file: investissement.py
@created: 20/11/2023

@project: 
@licence: GPLv3
"""
# Conditions initiales
operations=[(0, 100000.)]
capital = [[0, operations[0][1]]]
interets = [(0, 0.)] 
taux = 4.5


def Value(c: float, t: float) -> float:
    """ Calcul la plus-value d'un capital sur une annuité
    c (float): capital initial
    t (float): taux annuel en pourcentage
    return: plus-value annuelle en euros
    """
    return (c * t / 100)


def OperationCompte(m: float) -> tuple:
    """ Enregistre l'ordre des opérations annuelles du compte
    et retourne le tuple associé
    m (float): capital versé ou retiré
    return: (id_op (int): id de l'opération sur compte, m (float): montant de la transaction)
    """
    id_op = len(operations) + 1
    return (id_op, m)


def SommeInterets(liste: list) -> float:
    """ Effectue la somme des intérêts sur l'ensemble des exercices.
        liste (list): liste de tuples (id_année:int, interets: float)
        return: retourne la somme des intérêts (float)
    """
    sum = 0.
    for k in range(len(liste)):
        sum += liste[k][1]
    return sum


print(f"Balance initiale du compte: {capital[0][1]: .2f}€ Taux initial: {taux: .2f}%")
print("Fin année 0")
interets.append((1, Value(capital[0][1], taux)))
capital.append([1, capital[0][1] + interets[1][1]])
print(f"Balance: {capital[1][1]: .2f}€ Intérêts: {interets[1][1]: .2f}€")
print()
print("**********************************************************************")
print()
print("Début année 1: opération sur compte +5000€ et augmentation du taux de 2pts")
operations.append(OperationCompte(5000))
taux += 2.
capital[1][1] += operations[1][1]
print(f"Balance: {capital[1][1]: .2f}€ Nouveau taux: {taux: .2f}%")
print("Fin année 1")
interets.append((2, Value(capital[1][1], taux)))
capital.append([1, capital[1][1] + interets[2][1]])
print(f"Balance: {capital[2][1]: .2f}€ Intérêts: {interets[2][1]: .2f}€")
print()
print("**********************************************************************")
print()
print("Début année 2: opération sur compte -10% du capital et diminution du taux de 1pts")
operations.append(OperationCompte(- 0.1 * capital[2][1]))
taux -= 1.
capital[2][1] += operations[2][1]
print(f"Balance: {capital[2][1]: .2f}€ Nouveau taux: {taux: .2f}%")
print("Fin année 2")
interets.append((3, Value(capital[2][1], taux)))
capital.append([3, capital[2][1] + interets[3][1]])

print(f"Balance: {capital[3][1]: .2f}€ Intérêts: {interets[3][1]: .2f}€")
print()
print("************************************")
print("\t\tBilan")
print("************************************")

print(f"Balance finale: {capital[3][1]: .2f}€ Somme des intérêts: {SommeInterets(interets): .2f}€")
