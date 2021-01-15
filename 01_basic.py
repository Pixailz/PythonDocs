#!/usr/bin/env python3
#coding:utf-8

# THIS IS A COMMENT

def HelloWorld():

    print("Hello World ! 1")
    print("Hello World ! 2\nHello World ! 2")

    a = "Hello"
    b = " "
    c = "World"
    d = " "
    e = "!"
    f = " "
    g = "3"

    print(a + b + c + d + e + f + g + "\n")

class Variable():
    """
    var name rules  : begin with letter or undrescore
                      ne pas contenir de char spec
                      ne pas contenir d'espace
                      utliser des underscore

    Types standars  : entier numerique (int)
                      nombre flottant (float)
                      chaînes de caractères (str)
                      booléen (bool)

    Fonctions vues  : print()       -> afficher à l'écran
                      input()       -> lire au clavier
                      type()        -> retourne le type d'une donnée, variable, etc.
                      int(), float(), str(), bool() -> caster une donnée, la convertir
                      str.format()  -> formater une chaîne
    """
    def __init__(self, age=0, prixHT=0.99):

        self.age = age
        self.prixHT = prixHT

        self.name = input("Entrer un nom de Joueur : ")
        print("Bienvenue ,", self.name)
    
    def Afficher(self):

        print(self.age, type(self.age))
        print(self.prixHT, type(self.prixHT))
        print("L'âge de la personne est {} et le prix HT est de {} euros.".format(self.age, self.prixHT))
    
    def htTottc(self):

        self.prixTTC = int(self.prixHT + (self.prixHT * 0.2))
        print(f"PRIX HT\t\t{self.prixHT}\nPRIX TTC\t{self.prixTTC}")

def Operation(nombre1=0, nombre2=0, operateur=None):
    
    n1 = nombre1
    n2 = nombre2

    if operateur == None:
        print("Entrer un operateur")
    
    if operateur not in "*/-+":
        print("Entrer un operateur correct")
        exit()
    
    if operateur == "+":
        return n1 + n2

    elif operateur == "-":
        return n1 - n2

    elif operateur == "/":
        return n1 / n2

    elif operateur == "*":
        return n1 * n2

HelloWorld()

v = Variable(age=18, prixHT=19.95)

v.Afficher()
v.htTottc()

print(Operation(nombre1=2, nombre2=3, operateur="+"))