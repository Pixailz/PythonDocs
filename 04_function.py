#!/usr/bin/env python3
#coding:utf-8

def fonc(a=1, b=2, c=3, d=4, e=5):
    print("a =", a, "b =", b, "c =", c, "d =", d, "e =", e)

def dire_bonjour():
  print("bonjour tout le monde ! :)")

def dire(nom_personne="Tom", message_personne="Salut !", age_personne=18):
  print("{} ({} ans): {}".format(nom_personne, age_personne, message_personne))

def show_inventory(*list_items):
  for item in list_items:
    print(item)

def calculer_somme(nombre1, nombre2):
  resultat = nombre1 + nombre2

def le_plus_grand(nombre1, nombre2):
  if nombre1 > nombre2:
    print(f"{nombre1} est plus grand que {nombre2}")
  elif nombre2 > nombre1:
    print(f"{nombre2} est plus grand que {nombre1}")
  else:
    print("EGALITÉ !")

def table(nb, max):
    i = 0
    while i < max:
        print(i + 1, "*", nb, "=", (i + 1) * nb)
        i += 1

fonc()
fonc(4)
fonc(b=8, d=5)
fonc(b=35, c=48, a=4, e=9)

dire_bonjour()

dire(nom_personne="Jason", age_personne=26)
dire()
dire(message_personne="Yo !", age_personne=25, nom_personne="Roger")

show_inventory("épée")
show_inventory("épée", "arc", "potion de mana", "cape de Dragon rouge")

print(calculer_somme(5, 16))

le_plus_grand(2, 1)
le_plus_grand(15, 2)

table(5, 20)

# LAMBDA

coucou = lambda:print("Bonjour")
coucou()

ttc = lambda prixHT:prixHT + (prixHT * 0.2)

print(ttc(24))

calculer = lambda a, b : a + b
print(calculer(14, 27))

afficher = lambda text: print("[{}]".format(text))
afficher("je m'appelle lucien")

f = lambda x: x * x
print(f(-38))
