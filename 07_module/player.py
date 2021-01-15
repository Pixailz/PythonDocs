#!/usr/bin/env python3
#coding:utf-8

"""
Module pour le joueur
"""

def parler(personnage, message):
	print("{} : {}".format(personnage, message))
def au_revoir():
	print("Au revoir :) !")

if __name__ == "__main__":
	parler("USER", "MESSAGES <3<3<3")
	au_revoir()
