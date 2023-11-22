#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
@author: Cyril Génisson

@file: main.py
@created: 21/11/2023

@project: 
@licence: GPLv3
"""
import tkinter as tk
from tkinter import ttk

root = tk.Tk()
frm = ttk.Frame(root, padding=10)
frm.grid()
ttk.Label=(frm, text="Hello World!").grid(column=0, row=0)
ttk.Buttom(frm, text="Quit", command=root.destroy).grid(column=1, row=0)
root.mainloop()
