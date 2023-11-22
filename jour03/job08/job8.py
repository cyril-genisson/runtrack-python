#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
@author: Cyril Génisson

@file: job8.py
@created: 22/11/2023

@project: 
@licence: GPLv3
"""

saisons = [ "hiver", "été"] 
types =  {"fruits": [["orange", "mandarine", "kiwi"],
                    ["Poire", "fraise", "cassis"]],
          "légumes": [["carotte", "topinambour", "endive"],
                       ["artichaut", "aubergine", "navet"]]
          }


def bouf(typ: str, sais: str) -> None:
    match sais:
        case "hiver":
            if typ == "fruits":
                print(', '.join(types["fruits"][0]))
            else:
                print(', '.join(types["légumes"][0]))
        case "été":
            if typ == "fruits":
                print(', '.join(types["fruits"][1]))
            else:
                print(', '.join(types["légumes"][1]))

for i in saisons:
    for j in ["fruits", "légumes"]:
        bouf(j, i)
