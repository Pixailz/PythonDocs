#!/usr/bin/env python3
#coding:utf-8

"""
help(<class>)

Une méthode de chaîne travaille sur une copie, et pas sur la chaîne
elle-même.

str.upper(), str.lower(), str.capitalize(), str.title()
str.center(<largeur>, <caractere_remplissage>)
str.strip()

str.find(<chaine>, <debut>, <fin>)
str.index(<chaine>, <debut>, <fin>)
str.replace(<ancienne>, <nouvelle>, <occurences>)

str.isalpha(), str.isdigit(), str.isdecimal(), str.isnumeric()
str.isalphanum()

str.islower(), str.isupper()

str.isidentifier(), str.iskeyword()
"""

class ChaineDeCharactere():
    
    def __init__(self, string):
        self.string = string

    def afficher(self):
        print(self.string)

    def afficherEnMiniscule(self):
        print(self.string.lower())

    def afficherEnMajuscule(self):
        print(self.string.upper())
    
    def afficherEnCapital(self):
        print(self.string.capitalize())

    def afficherEnTitre(self):
        print(self.string.title())

    def afficherCentrer(self, centrage=20):
        print(self.string.center(centrage, "-"))

    def afficherFormat1(self, exp, message):
        print("{0} say : {1}".format(exp, message))

    def afficherFormat2(self, name="name", surname="surname", age="23", pays="Amsterdam", hobbies="hackin'"):
        sentence = """
        je m'appelle {name}, {name} {surname} et j'ai {age} ans
        dans mon pays, en {pays}, j'aime bien {hobbies} toutes la journée
        """.format(name=name, surname=surname, age=age, pays=pays, hobbies=hobbies)
        print(sentence)
    
    def afficherStrip(self):
        content = self.string.strip()
        print(content)

    def findInString(self, content):
        try:
            print(f"La chaines {content}, se trouve a l'index",self.string.find(content))
        except ValueError:
            print(f"Je n'ai pas trouvé la chaîne {content}")

    def Tolist(self):
        self.list = self.string.split(" ")
        print(self.string)

    def replace(self, content, to):
        print(self.string.replace(content, to))
    
    def isLower(self):
        print(self.string.islower())
        
    def isAffected(self, content):
        print(content.isidentifier())
        
def Truncate(f):
    if not isinstance(f, float):
        raise TypeError("Le nombre doit etre un floattant")

    f = str(f)
    p_e, p_d = f.split(".")
    return ",".join([p_e, p_d[:2]])

c = ChaineDeCharactere(string="   ne CRIE pas trop FORT!")

c.afficher()
c.afficherEnMiniscule()
c.afficherEnMajuscule()
c.afficherEnCapital()
c.afficherEnTitre()
c.afficherCentrer(150)
c.afficherFormat1(exp="Pix", message="Salut kakine !")
c.afficherFormat2(name="Bruno", surname="DA SILVA", age="22", pays="Françe", hobbies="hackin'")
c.afficherStrip()
c.Tolist()
c.replace(content="p", to="l")
c.findInString(content="!")
c.isLower()
c.isAffected(content="var1")

phrase = "Magicien|10|5"
print(phrase.split("|"))
print(Truncate(f=1/3))

ch = "Le langage Python"
if "langage" in ch:
    print("Trouvé")
else:
    print("Non trouvé")