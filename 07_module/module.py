#!/usr/bin/env python3
#coding:utf-8

"""
Importer un modules : import <nom_module>
                      from <nom_module> import <nom_fonction>
                      from <nom_module> import *
"""

"""
import math 
help("math")
"""

## many way to import
#1
"""
import math

resultat = math.sqrt(100)
print(resultat)
"""
#2
"""
from math import sqrt

resultat = sqrt(100)
print(resultat)
sinus = math.sin(42)
print(sinus)
"""
#3
"""
from math import *

resultat = sqrt(100)
print(resultat)
"""


from player import parler
from player import au_revoir

parler("Pix", "Salut tout le monde :] !")
au_revoir()