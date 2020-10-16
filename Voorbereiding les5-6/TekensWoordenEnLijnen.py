# -*- coding: utf-8 -*-
"""
Created on Fri Oct 16 17:07:27 2020

@author: Thibaut
"""

x = input("Naam van het .txt document: \n> ")

while x != "":
    fileName = x+str(".txt")
    file = open(fileName, "r")
    
    text = file.read()
    
    tekens = len(text)
    
    lijnenLijst = text.split("\n")
    lijnen = len(lijnenLijst)
    
    woorden = 0
    for i in lijnenLijst:
        woordenLijst = i.split(" ")
        woorden += len(woordenLijst)
    
    print(f"\nLijnen: {lijnen}\nWoorden: {woorden}\nTekens: {tekens}")
    
    x = input(">")