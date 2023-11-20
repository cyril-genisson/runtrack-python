#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
@author: Cyril Génisson

@file: inventory.py
@created: 20/11/2023

@project: 
@licence: GPLv3
"""
nom = ['Id', 'Produit', 'Prix (€)', 'Quantité']
produit1 = {"id": 1, "n": "Café", "p": .4, "q": 5}
produit2 = {"id": 2, "n": "Thé", "p": .5, "q": 12}
inventory = [produit1, produit2]


def menu() -> None:
    print()
    print("**********************")
    print("*    Inventaire      *")
    print("**********************")
    print()
    print("Option *1*: afficher l'inventaire")
    print("Option *2*: modifier un produit")
    print("Option *3*: ajouter un produit")
    print("Option *4*: sortir du programme")


opt = '0'

while opt != '4':
    menu()
    rep=input("Votre option: ")
    match rep:
        case '1':
            print(f"{nom[0]: ^5}|{nom[1]: ^20}|{nom[2]: ^10}|{nom[3]: ^10}|")
            print(f"{'-'*49}")
            for k in range(len(inventory)):
                print(f"{inventory[k]['id']: ^5}|{inventory[k]['n']: ^20}|{'{:.2f}'.format(inventory[k]['p']): ^10}|{inventory[k]['q']: ^10}|")
            print()
        case '2':
            id_produit = int(input("Id du produit: "))
            print("Changer le nom: n \t Changer le prix: p \t Changer la quantité: q")
            choice = input("Votre choix: ")
            match choice:
                case "n":
                    inventory[id_produit - 1][choice] = input("Nouveau nom: ")
                case "p":
                    inventory[id_produit - 1][choice] = float(input("Nouveau prix: "))
                case "q":
                    inventory[id_produit - 1][choice] = int(input("Nouvelle quantité: "))
                case _:
                    print("Rien à faire")
        case '3':
            name = input("Nom du nouveau produit: ")
            price = float(input("Prix du nouveau produit: "))
            quantity = int(input("Quantité du nouveau produit: "))
            inventory.append({"id": len(inventory) + 1, "n": name, "p": price, "q": quantity})
            print("Produit ajouté.")
        case '4':
            print("Fin du programme")
            break
        case _:
            continue

