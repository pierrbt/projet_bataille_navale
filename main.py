"""
Projet : Bataille Navale
Auteurs : Pierre BIDET, Anaëlle BOUSSIN
Languages : Python
Classe : 1G NSI
Licence : GPL-3.0
"""

from random import randint, choice
from time import sleep

def askInt(question: str, mini=0, maxi=9999) -> int:
    isOk = False
    number = 0
    while not isOk:
        inp = input(question)
        if inp.isnumeric():
            number = int(inp)
            if number < mini or number > maxi:
                print(f"La valeur est hors des bornes {mini}-{maxi}")
            else:
                isOk = True
        else:
            print("Ceci n'est pas un entier !")
    return number

def generatePlate():
    plate = []

from plate import generatePlate
from utils import askInt, askPosition, getIndexFromPosition, getNearestBoatDelta

    for i in range(5):
        row = []
        for j in range(5):
            if (i,j) == pos1 or (i,j) == pos2:
                row.append("#")
            else:
                row.append("-")
        plate.append(row)
    #print(plate)
    return plate



def Jeu() -> None:
    print("Bienvenue sur l'excellente bataille navale !!")
    nb_joueurs = askInt("Entrez le nombre de joueur -> ", mini=2, maxi=9)
    print("Génération du plateau")

    for i in range(1, nb_joueurs + 1):
        plateau = generatePlate()
        points = 0
        print(f"\n----------------------------\n\nJoueur n°{i} : ")
        print('\n '.join([''.join(['{:4}'.format(item) for item in row]) for row in plateau]), end="\n\n",)
        for j in range(1, 4):
            print(f"Essai n{j}")
            pos1 = askInt("x -> ", mini=1, maxi=5)
            pos2 = askInt("y -> ", mini=1, maxi=5)
            if plateau[pos2 - 1][pos1 - 1] == "#":
                print("Touché !")
                points += 1
                if points == 2:
                    points = 8
            else:
                print("Raté !")

        print("")
    
    print("\n--------------------------------\n\nFin du jeu")
    return points_joueurs


if __name__ == '__main__':
    print("Bienvenue sur l'excellente bataille navale !!")
    nb_joueurs = askInt("Entrez le nombre de joueur -> ", mini=2, maxi=9)
    jouerUnePartie(nb_joueurs)


# main.py
