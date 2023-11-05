"""
Projet : Bataille Navale
Auteurs : Pierre BIDET, Anaëlle BOUSSIN
Languages : Python
Classe : 1G NSI
Licence : GPL-3.0
"""
from typing import List

from plate import generatePlate
from utils import askPosition, getIndexFromPosition, getNearestBoatDelta, askInt


def jouerUnePartie(nb_joueurs: int) -> List[int]:  # Fonction qui permet de jouer une partie

    points_joueurs = []  # Liste des points des joueurs

    for i in range(1, nb_joueurs + 1):  # Pour chaque joueur
        plateau = generatePlate()  # On génère un plateau de jeu
        points = 0  # On initialise les points du joueur à 0
        print(f"\n----------------------------\n\nJoueur n°{i} : ")  # On affiche le numéro du joueur
        print('\n '.join([''.join(['{:4}'.format(item) for item in row]) for row in plateau]),
              end="\n\n", )  # On affiche le plateau de jeu
        for j in range(1, 4):  # Pour chaque essai
            print(f"Essai n{j}")  # On affiche le numéro de l'essai
            position = askPosition()  # On demande la position à frapper
            pos1, pos2 = getIndexFromPosition(position)  # On récupère les index de la position
            if plateau[pos1][pos2] == "#":  # Si la position est celle d'un bateau
                print("Touché !")  # On affiche "Touché !"
                points += 1  # On ajoute 1 point au joueur
                plateau[pos1][pos2] = "X"  # On remplace la position par un X
                delta = getNearestBoatDelta(plateau, (pos1, pos2))  # On récupère le delta
                if delta > 1:  # Si delta < 1 (que le bateau est coulé car la case collée est déjà touchée)
                    print("Coulé !")  # On affiche "Coulé !"
                    points += 7  # On ajoute 7 points au joueur
            else:  # Sinon
                print("Raté !")  # On affiche "Raté !"
                plateau[pos1][pos2] = "O"  # On remplace la position par un O
        print(f"Vous cumulez {points} points")  # On affiche les points du joueur
        points_joueurs.append(points)  # On ajoute les points du joueur à la liste des points des joueurs
    return points_joueurs  # On retourne la liste des points des joueurs


if __name__ == '__main__':  # Si le fichier est exécuté directement
    print("Bienvenue sur l'excellente bataille navale !!")  # On affiche un message de bienvenue
    nb_joueurs = askInt("Entrez le nombre de joueur -> ", mini=2, maxi=9)  # On demande le nombre de joueurs

    wantToContinue = True  # On initialise la variable wantToContinue à True
    points_totaux = [0 for _ in range(nb_joueurs)]  # On initialise la liste des points totaux à 0 pour chaque joueur

    while wantToContinue:  # Tant que wantToContinue est True
        points = jouerUnePartie(nb_joueurs)  # On joue une partie
        for i, pts in enumerate(points):  # Pour chaque joueur
            points_totaux[i] += pts  # On ajoute les points de la partie aux points totaux du joueur

        wantToContinue = input("\nVoulez-vous continuer (o/n) -> ") == "o"  # On demande si on veut continuer
    print("\nVoici le résumé des scores : ")  # On affiche le résumé des scores
    for joueur, points in enumerate(points_totaux):  # Pour chaque joueur
        print(f"Joueur {joueur + 1} : {points} points")  # On affiche les points du joueur

    gagnants = []  # On initialise la liste des gagnants
    maxi = max(points_totaux)  # On récupère le score maximum
    for index, points in enumerate(points_totaux):  # Pour chaque joueur
        if points == maxi:  # Si le joueur a le score maximum
            gagnants.append(index)  # On ajoute le joueur à la liste des gagnants

    if len(gagnants) == 1:  # Si il n'y a qu'un seul gagnant
        print(f"\nLe joueur {gagnants[0] + 1} a gagné")  # On affiche le gagnant
    else:  # Sinon
        print(f"\nLes joueurs {','.join(gagnants)} ont gagné")  # On affiche les gagnants

# main.py
