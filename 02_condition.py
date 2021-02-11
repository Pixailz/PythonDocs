#!/usr/bin/env python3
#coding:utf-8

"""
Opérations de comparaison : == (égale à)
                            != (différent de)
                            <  (plus petit que)
                            >  (plus grand que)
                            <= (plus petit ou égal à)
                            >= (plus grand ou égal à)

Mots clés des conditions  : if / elif / else

Conditions multiples      : and (ET)
                            or (OU)
                            in / not in (DANS / PAS DANS)
"""

def passwordChecker(user_id, user_pass):

    identifiant = "Pix"
    mot_de_passe = "1234"

    print("Interface de connexion")

    if user_id == identifiant and user_pass == mot_de_passe:
        print("Vous êtes connectés, bienvenue", user_id)

    print("je ne suis plus dans le 'if'")

def isVoyelle(lettre):
    if lettre.lower() in "aeiouy":
        print(f"{lettre} est une voyelle")
    else:
        print(f"{lettre} est une consonne")

def checkAge(age):
    if age == 18:
        print("Tu viens d'être majeur")
    elif age == 50:
        print("Tu viens d'avoir 50 ans")
    elif age == 60:
        print("Tu viens d'avoir 60 ans")
    else:
        print("Tu as", age, "ans")

def checkAge2(age):
    #if age > 0 and age <= 100:
    if 0 < age <= 100:
        print("l'âge est validé")
    else:
        print("L'âge est incorrect")

def checkIfCharge(isit):
    if isit:
        print("Le jeu est en marche")
    else:
        print("Le jeu a été quitté")


passwordChecker(user_id="Pix", user_pass="1234")

isVoyelle("A")

checkAge(18)

checkAge2(50)

checkIfCharge(True)
