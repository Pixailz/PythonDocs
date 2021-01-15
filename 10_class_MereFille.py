#!/usr/bin/env python3
#coding:utf-8

"""
Fonctions utiles :
    isinstance(<objet>, <classe>) : vérifie qu'un objet est de la class
                                    renseignée

    issubclass(<class_fille>, <class_mere>) : vérifie qu'une classe est
                                              fille d'une autre
"""


#Classe Mère
class Vehicule:

    def __init__(self, nom_vehicule, quantite_essence):
        self.nom = nom_vehicule
        self.essence = quantite_essence
    
    def se_deplacer(self):
        print("Le véhicule {} se déplace...".format(self.nom))

# Classe Fille
class Voiture(Vehicule):
    
    def __init__(self, nom_voiture, essence, puissance):
        Vehicule.__init__(self, nom_voiture, essence)
        self.puissance = puissance

    def se_deplacer(self):
        print("Je roule...")

class Avion(Vehicule):
    def __init__(self, nom, essence, marchandise):
        Vehicule.__init__(self, nom, essence)
        self.marchandise = marchandise
    
    def se_deplacer(self):
        print("Je vole...")

voiture1 = Voiture("Toyota Supra", 90, "420")
voiture1.se_deplacer()
print(voiture1.puissance + " CH")

av1 = Avion("F22 Raptor", 2400, "Missiles")
av1.se_deplacer()
print("l'avion {} contient {} comme marchandise".format(av1.nom, av1.marchandise))



# Classe Mère 1
class ObjetJeu:
    pass

# Classe Mère
class Arme:
    pass

# Class Fille
class Fusil(Arme, ObjetJeu):
    pass



class Etudiant:
    pass

class Enseignant:
    pass

class Doctorant(Etudiant, Enseignant):
    pass

class Animal:
    def __init__(self, nom):
        self.nom = nom

    def manger(self):
        print(self.nom, "mange...")

class Reptile(Animal):
    def __init__(self, nom, regime_alimentaire):
        Animal.__init__(self, nom)
        self.regime = regime_alimentaire

    def manger(self):
        print("Le reptile mange...")

lezard = Reptile("Lézard", "grenouille")
lezard.manger()
if isinstance(lezard, Animal):
    print("Lézard est un Animal")

if issubclass(Reptile, Animal):
    print("Réptile hérite d'Animal")
