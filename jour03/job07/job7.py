#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
@author: Cyril Génisson

@file: job7.py
@created: 22/11/2023

@project: 
@licence: GPLv3
"""


def devel(language: str) -> None:
    match language.lower():
        case 'javascript':
            print("tu es un développeur web")
        case 'python':
            print("tu es un développeur IA")
        case 'java':
            print("tu es un développeur logiciel")
        case 'reactjs':
            print("tu es un développeur mobile")
        case _:
            print("un jour, je serai le meilleur développeur...")

lang = ['JavaScript', 'Python', 'Java', 'ReactJS', 'dqkls']
    
for k in lang:
    devel(k)
