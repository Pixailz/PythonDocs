#!/usr/bin/env python3
#coding:utf-8

"""
Propriété   : manière de manipuler / contrôler des attributs
              principe d'encapsulation !
"""
"""
Fonctions utiles :
    isinstance(<objet>, <classe>) : vérifie qu'un objet est de la class
                                    renseignée

    issubclass(<class_fille>, <class_mere>) : vérifie qu'une classe est
                                              fille d'une autre
"""

class Humain:
    """Cette classe represante un Humain"""
    def __init__(self, nom, age):
        print("Création d'un humain...")
        self.nom = nom
        self._age = age

    def _getage(self):
        try:

            if self._age <= 1:
                return str(self._age) + " an"

            else:
                return str(self._age) + " ans"

        except AttributeError:
            print("L'âge n'existe pas !")

    def _setage(self, nouvel_age):
        if nouvel_age < 0:
            self._age = 0
        else:
            self._age = nouvel_age

    def _delage(self):
        del self._age

    # property(<getter><setter><deleter><helper>)
    age = property(_getage, _setage, _delage, "Je suis l'age d'un Humain")

# Programme principale
h1 = Humain("Pix", 26)

print(h1.age)

h1.age = 20

print(h1.age)

del h1.age

print(h1.age)

#help(Humain)
#help(Humain.age)

h2 = Humain("Julia", 1)
print("{} a {}".format(h2.nom, h2.age))


##TEASING
#if h1 < h2:
