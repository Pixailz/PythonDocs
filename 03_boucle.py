#!/usr/bin/env python3
#coding:utf-8

"""
Boucles     : while / for
Mots-clés   : break (casse la boucle) / continue (revient au début de la boucle)
"""

def enumerateSTR(content):
    for letter in content:
        print(letter, end="")
    print("")

def checkVoyelle(content):
    for lettre in content:
        if lettre in "AEIOUYaeiouy": # lettre est une voyelle
            print(lettre, end="")
        else: # lettre est une consonne... ou plus exactement, lettre n'est pas une voyelle
            print("*", end="")
    print("")

def spammeur(nombre):
    c = 0
    while c < nombre:
        c += 1
        print(f"nombre est a : {c}")
    print("Je suis sorti de la boucle...")

def Menu():
    jeu_lance = True

    while jeu_lance:
        #BLA
        #BLA
        #BLA
        choixMenu = input("> ")

        if choixMenu == "again":
            continue
        elif choixMenu == "quit":
            jeu_lance = False
        elif choixMenu == "hello":
            print("Bonjour :) !")
        else:
            print("Commande introuvable")

enumerateSTR("testtttter")
checkVoyelle("Bonjour les ZER0S")
spammeur(50)
Menu()
