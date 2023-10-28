"""
Projet : Bataille Navale
Auteurs : Pierre BIDET, Anaëlle BOUSSIN
Languages : Python
Classe : 1G NSI
Licence : GPL-3.0
"""
from typing import List

from plate import generatePlate
from utils import askInt, askPosition, getIndexFromPosition, getNearestBoatDelta


def jouerUnePartie(nb_joueurs: int) -> List[int]:  # Fonction qui permet de jouer une partie


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
