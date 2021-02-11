#!/usr/bin/env python3
#coding:utf-8

"""
Crée une liste:
                - empty list
                    - <name> = list()
                    - <name> = []
                - custom list
                    - <name> = ["name", 1, 15]
                    - <name> = [0] * 10
                    - <name> = ["name"] * 5

                    - list from 5 to 20
                        - <name> = range(5, 20)

Afficher une liste:

                - print(<name[:]>)

                - i = 0
                  while i < len(<name>):
                      print(<name>[i])
                      i += 1

                - for valeur in invenaire:
                      print(valeur)

                - ByIndex (where n is n-1)

                    # print n from the begin
                    - print(<name>[n])

                    # print n from the end
                    - print(<name>[-n])

                    # from n to end
                    - print(<name>[n:])

                    # from begin to n
                    - print(<name>[:n]

                    # from n1 o n2
                    - print(<name>[n1:n2]
"""

class List():

    def __init__(self, content=list()):

        if not isinstance(content, list):
            self.content = list()
        else:
            self.content = content

    def typeOf(self):

        print("Type Of VAR {}".format(type(self.content)))

    def Changer(self, content, index):
        self.content[index] = content
        self.Afficher()

    def Append(self, content):
        self.content.append(content)
        self.Afficher()

    def Insert(self, content, index):
        self.content.insert(index, content)
        self.Afficher()

    def Concatenate(self, content):
        self.content.extend(content)
        self.Afficher()

    def Del(self, index):
        del self.content[index]
        self.Afficher()

    def Remove(self, content):

        if isinstance(content, list):

            for x in range(len(content)):

                self.content.remove(content[x])

            self.Afficher()

        else:
            self.content.remove(content)
            self.Afficher()

    def Afficher(self):

        for x in range(len(self.content)):

            if x+1 == len(self.content):
                print(self.content[x])

            else:
                print(self.content[x], end=",")

    def Enumerate(self):

        for i, e in enumerate(self.content):

            print(f"A l'indice {i} se trouve {e}")

    def Search(self, content):
        if content in self.content:
            print("Trouvée")
        else:
            print("Pas trouvée")

    def IndexOf(self, content):
        index = self.content.index(content)
        print(f"{content} se trouve a l'index : {index}")

l = List(content=[1,2,3,4,5,6,7,7,8,9])

l.typeOf()
l.Afficher()
l.Changer(content=0, index=0)
l.Append(content=10)
l.Insert(content=1, index=1)
l.Concatenate(content=[11,12,13,14,15,16,17,18,19])
l.Del(index=12)
l.Remove(content=[12, 13, 14, 15, 16, 17, 18, 19])
l.Enumerate()
l.Search(content=1)
l.IndexOf(content=10)

def listTostr(content):

    content = " ".join(content)
    print(content)

listTostr(content=["Bonjour", "a", "tous"])

# sort()
inventaire = ["Potion de mana", "Arc", "Bouclier", "Manteau de cuir", "Arbalète"]
inventaire.sort()
print(inventaire)

# count()
inventaire = ["potion", "arc", "potion", "potion", "manteau"]
print("Nombre de potions : ", inventaire.count("potion"))

# reverse()
number = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(number[:])

number.reverse()
print(number[:])

# 1
inventaire = ["potion", "arc", "potion", "potion", "manteau"]
print(inventaire[:])

inventaire.clear()
print(inventaire[:])

# 2
inventaire2 = ["potion", "stuff", "dirt", "potion", "shield"]
print(inventaire2[:])

inventaire2[:] = []
print(inventaire[:])

# join() / split()
chaine = "Bonjour à tous"

chaine = chaine.split(" ")
print(chaine)

chaine = " ".join(chaine)
print(chaine)

# Copie de liste
liste1 = ["Arc", "Bouclier", "Tunique"]
liste2 = liste1[:]

print("Liste 1 :", liste1[:])
print("Liste 2 :", liste2[:])

liste2.append("Potion de mana")

print("Liste 1 :", liste1[:])
print("Liste 2 :", liste2[:])

import copy

liste3 = [1, 2, 3]
liste4 = copy.deepcopy(liste3)

print("Liste 3 :", liste3[:])
print("Liste 4 :", liste4[:])

liste4.append("Potion de mana")

print("Liste 3 :", liste3[:])
print("Liste 4 :", liste4[:])

# Tuples
inventaire = ["Arc", "Épée", "Bouclier", "Potion"]

for objet in inventaire:
    print(objet)

for indiceObjet, valeurObjet in enumerate(inventaire):
    indiceObjet += 1
    print("{}_{}".format(indiceObjet, valeurObjet))
