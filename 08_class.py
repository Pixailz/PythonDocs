#!/usr/bin/env python3
#coding:utf-8

"""
Classe				: plan de conception, genre (ex : Humain)
Objet				: instance de classe (ex : Pix)
Attribut			: variable de classe (ex : nom, age, sexe, taille, ...)

Méthode d'instance  : fonction sur une instance
Méthode de classe 	: fonction sur une classe
Méthode statique	: fonction indépendante mais "lié" a une classe
"""

class Humain:
    """Classe qui définit un humain"""

    lieu_habitation = "Terre"
    humains_crees = 0

    def __init__(self, nom, age):
        self.nom = nom
        self.age = age
        Humain.humains_crees += 1

    def parler(self, message): # self= méthode standard
        print("{} a dit : {}".format(self.nom, message))

    def changer_planete(cls, nouvelle_planete): # cls = méthode de classe
        Humain.lieu_habitation = nouvelle_planete

    changer_planete = classmethod(changer_planete)

    def definition():
        print("L'Humain est classé comme etant le plus haut de la chaine alimentaires")

    definition = staticmethod(definition)

# Programme principal
print("Lancement du programme...")

print("Humain existant : {}".format(Humain.humains_crees))

h1 = Humain("Pix", 16)
print("Prenom de h1 -> {}".format(h1.nom))
print("age de h1 -> {}".format(h1.age))

print("Humain existant : {}".format(Humain.humains_crees))

h2 = Humain("Albert", 24)
print("Prenom de h2 -> {}".format(h2.nom))
print("age de h2 -> {}".format(h2.age))

print("Humain existant : {}".format(Humain.humains_crees))

h1.prenom = "???"
h1.age = 1000

print("Prenom de h1 -> {}".format(h1.nom))
print("age de h1 -> {}".format(h1.age))
print("Humain existant : {}".format(Humain.humains_crees))

print("Planète actuelle : {}".format(Humain.lieu_habitation))
Humain.changer_planete("Mars")
print("Planète actuelle : {}".format(Humain.lieu_habitation))

Humain.definition()
