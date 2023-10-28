"""
Projet : Bataille Navale
Auteurs : Pierre BIDET, Anaëlle BOUSSIN
Languages : Python
Classe : 1G NSI
Licence : GPL-3.0
"""
from typing import List
import time
import customtkinter
from plate import generatePlate
from utils import askPosition, getIndexFromPosition, getNearestBoatDelta, askInt


def jouerUnePartie(nb_joueurs: int) -> List[int]:  # Fonction qui permet de jouer une partie

    points_joueurs = []  # Liste des points des joueurs

    for i in range(1, nb_joueurs + 1):
        plateau = generatePlate()
        points = 0
        print(f"\n----------------------------\n\nJoueur n°{i} : ")
        print('\n '.join([''.join(['{:4}'.format(item) for item in row]) for row in plateau]), end="\n\n",)
        for j in range(1, 4):
            print(f"Essai n{j}")
            position = askPosition()
            pos1, pos2 = getIndexFromPosition(position)
            if plateau[pos1][pos2] == "#":
                print("Touché !")
                points += 1
                plateau[pos1][pos2] = "X"
                # Get nearest # to pos1, pos2 in order to see if it is touched or destroyed
                delta = getNearestBoatDelta(plateau, (pos1, pos2))
                if delta > 1:
                    print("Coulé !")
                    points += 7
            else:
                print("Raté !")
                plateau[pos1][pos2] = "O"
        print(f"Vous cumulez {points} points")
        points_joueurs.append(points)
    return points_joueurs


if __name__ == '__main__':
    print("Bienvenue sur l'excellente bataille navale !!")
    nb_joueurs = askInt("Entrez le nombre de joueur -> ", mini=2, maxi=9)
    jouerUnePartie(nb_joueurs)


# main.py
