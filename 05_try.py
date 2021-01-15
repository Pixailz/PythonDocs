#!/usr/bin/env python3
#coding:utf-8

"""
Gérer le execptions : try / except (+ else, finally)

Types d'exceptions 	: ValueError
					  NameError
					  TypeError
					  ZeroDivisionError
					  OSError
					  AssertionError
"""

# try forme minimal
"""
try:
    resultat = numerateur / denominateur
except:
    print("Une erreur est survenue... laquelle ?")
"""

# try forme complete
"""
try:
    resultat = numerateur / denominateur
except NameError:
    print("La variable numerateur ou denominateur n'a pas été définie.")
except TypeError:
    print("La variable numerateur ou denominateur possède un type incompatible avec la division.")
except ZeroDivisionError:
    print("La variable denominateur est égale à 0.")
else:
    print("Le résultat obtenu est", resultat)
"""

def checkAge(ageUtilisateur):
    try:
        ageUtilisateur = int(ageUtilisateur)
    except:
        print("L'âge indiqué est incorrect !")
    else:
        print("tu as", ageUtilisateur, "ans")
    finally:
        print("FIN DU PROGRAMME...")

def divisionMINI(n1, n2):
    try:
        n2 = int(n2)
        print("Résultat = {}".format(n1 / n2))
    
    except:
        print("Une erreur est survenue")

def divisionFULL(n1, n2):
    try:
        n2 = int(n2)
        print("Résultat = {}".format(n1 / n2))

    except ZeroDivisionError:
        print("Vous ne pouver pas divisez par zéro.")

    except ValueError:
        print("Vous devez entrer un nombre.")

    except:
        print("Valeur incorrect.")

    else:
        print("Bravo, tu as noté un nombre valide !")

def checkAnnee(annee):
    try:
        annee = int(annee) # Conversion de l'année
        assert annee < 0

    except ValueError:
        print("Vous n'avez pas saisi un nombre.")

    except AssertionError:
        print("L'année saisie est inférieure ou égale à 0.")

checkAge(15)
checkAge("Pix")

divisionMINI(15, 0)
divisionFULL(15, 2)

checkAnnee(2015)
checkAnnee(-20154)