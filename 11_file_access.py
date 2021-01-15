#!/usr/bin/env python3
#coding:utf-8

"""
Modes d'ouvertue : r (lecture seule)
                   w (écriture avec replacement)
                   a (écriture avec ajout en fin de fichier)
                   x (lecture et écriture)
                   r+ (lecture/écriture dans un même fichier)
Fermeture        : <name>.close()

Lecture          : read(), readline(), readlines()

Écriture         : write()
"""

# 1st Method
class Files():

    def __init__(self, name):

        self.name = name
        self.FCountLines()

    def FCountLines(self):

        self.FOpen()
        self.nbline = len(self.f.read().split("\n"))
        self.FClose()

    def FOpen(self):

        self.f = open("11donnees.txt", "r")

    def FClose(self):

        self.f.close()

    def FRead(self):

        content = self.f.read()
        print(content)

    def FReadLine(self):

        for line in range(self.nbline):
            print(self.f.readline(), end="")

    def FReadlines(self):

        content = self.f.readlines()
        for line in range(len(content)):
            print(content[line], end="")
    
    def FCheckOpened(self):
        if self.f.closed:
            print("Fichier fermé")
        else:
            print("Fichier encore ouvert")

    def FReplace(self, nombre=0):
        with open(self.name, "w") as f:
            f.write(str(nombre) + "\n")
            f.write("Bonjour, je suis une phrase\n")
            f.write("Et une autre ...\n")
        input(f"Regarde le contenus du fichier : {self.name}")

f = Files(name="11donnees.txt")
print("Readline\n")
f.FOpen()
f.FReadLine()
f.FClose()
f.FCheckOpened()

print("\n\nReadlines\n")
f.FOpen()
f.FReadlines()
f.FClose()
f.FCheckOpened()

print("\nRead\n")
f.FOpen()
f.FRead()
f.FClose()
f.FCheckOpened()

print("\nReplace\n")
f.FReplace(nombre=15)
f.FOpen()
f.FReadlines()
f.FClose()
f.FCheckOpened()
# 2nd Method

print("\n\n\n2nd Method\n")

fi = "11donnees.txt"

with open(fi, "r") as f:
    content = f.readlines()
    for line in range(len(content)):
        print(content[line], end="")
    print("")

if f.closed:
    print("Fichier fermé")
else:
    print("Fichier encore ouvert")
print("")
# BONUS (PICKLE)

import pickle

class Player:
    def __init__(self, name, level):
        self.name = name
        self.level = level

    def whoami(self):
        print("{} ({})".format(self.name, self.level))

p1 = Player("Pix", 1000)
p1.whoami()

with open("11player.data", "wb") as fic:
    record = pickle.Pickler(fic)
    record.dump(p1)

with open("11player.data", "rb") as fic:
    get_record = pickle.Unpickler(fic)
    player_one = get_record.load()

player_one.whoami()


# TO REVERT CHANGE MADE ON FILE

with open("11donnees.txt.bak", "r") as f1:

    content = f1.readlines()

    with open("11donnees.txt", "w") as f2:

        for line in range(len(content)):

            f2.write(content[line])