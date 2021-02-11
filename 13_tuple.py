#!/usr/bin/env python3
#coding:utf-8

"""
(!) Tuple : conteneur immuable (dont on ne peut modifier les valeurs)

Création de tuple : monTuple = ()       #Vide
                    monTuple = 17,      #Une seul valeur
                    monTuple = (17,)    #Idem
                    monTuple = (4, 6)   #Plusieur valeurs

Accès aux valeurs : monTuple[X]         #Valeur d'indice X

2 raisons d'uliliser les tuples : affectation multiple de variable
                                  retour multiple de fonction
"""

class Tuples():

    def __init__(self, content):

        self.content = content

    def Afficher(self):

        print(self.content[:])

    def pasUnTuple(self):

        PasUnTuple = (45)
        print(type(PasUnTuple))

    def unTuple(self):

        UnTuple = (45,)
        print(type(UnTuple))

    def doubleAffect(self):
        n1, n2 = 14, 46
        print(f"{n1} {n2}")

t1 = Tuples(content=(1,"ABC"))
t1.Afficher()
t1.pasUnTuple()
t1.unTuple()
t1.doubleAffect()

def get_player_position():

    posX = 148
    posY = 86

    return (posX, posY)

# Programme principale
coordX = 0
coordY = 0

print("Position du joueur : (X:{}/Y:{})".format(coordX, coordY))

coordX, coordY = get_player_position()

print("Position du joueur : (X:{}/Y:{})".format(coordX, coordY))
