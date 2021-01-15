#!/usr/bin/env python3
#coding:utf-8

"""
Création de dictionnaire : <name> = {} #Vide
                           <name> = {<cle>:<valeur>, <cle>:<valeur2>}

Accès à une valeur       : <name>[<cle>]
Ajout au dictionnaire    : <name>[<cle>] = <valeur>

Suppresion               : <name>.pop(<cle>)
                           del dico[<cle>]

Copie de dictionnaire    : dico1 = {1:11, 2:22}
                           dico2 = dico1.copy()
"""

# Init
"""
dico = {1:145, "prénom":"Jason"}
"""

# Accès
"""
dico = {"name":"Jason"}
print(dico["name"])
"""

dico = {"chat":"C'est un félin"}
print(dico["chat"])

dico["chien"] = "C'est un mammifère, le meilleur ami de l'homme"
print(dico)

valeurSupprimee = dico.pop("chien")
#del dico["chien"]
print(dico)
print(valeurSupprimee)

if "chien" in dico:
    print("Oui")
else:
    print("Non")

dico["chien"] = valeurSupprimee
dico["reptile"] = "C'est un animal mystique, un peuple qui vie dans les egout..."

#for key in dico:
for key in dico.keys():
    print(key)

for value in dico.values():
    print(value)

for k,v in dico.items():
    print("{} : {}".format(k, v))

try:
    print(dico["lapin"])
except KeyError:
    print("key not found")


dico2 = dico.copy()

print(dico)
print(dico2)

dico["poule"] = "Animal qui pond des oeuf et chie partout"
print(dico)
print(dico2)

def maFonction(**parametres):
    print(parametres)

maFonction(p=154, nom="Blablabla")
