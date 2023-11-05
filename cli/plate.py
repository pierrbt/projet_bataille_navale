"""
Projet : Bataille Navale
Auteurs : Pierre BIDET, Anaëlle BOUSSIN
Languages : Python
Classe : 1G NSI
Licence : GPL-3.0
"""

from random import randint, choice


def generatePlate():  # Génère un plateau de jeu
    plate = []  # Initialise le plateau de jeu
    orientation = choice(["V", "H"])  # On choisit aléatoirement l'orientation du bateau n°1

    if orientation == "V":
        # Générer le bateau n°1 à la verticale
        pos1 = (randint(0, 4), randint(0, 3))
        pos2 = (pos1[0], pos1[1] + 1)
    else:
        # Générer le bateau n°1 à l'horizontale
        pos1 = (randint(0, 3), randint(0, 4))
        pos2 = (pos1[0] + 1, pos1[1])

    if orientation == "V":
        # Générer le bateau n°2 à l'horizontale et qui n'est pas collé au bateau n°1
        pos3 = (randint(0, 4), randint(0, 3))  # Première position aléatoire
        while abs(pos1[0] - pos3[0]) < 2 or abs(
                pos3[1] - pos1[1]) < 2:  # Tant que le bateau n'est pas assez éloigné du bateau n°1
            pos3 = (randint(0, 3), randint(0, 4))  # On génère une nouvelle position aléatoire

        pos4 = (pos3[0] + 1, pos3[1])  # On génère la deuxième position du bateau n°2
    else:
        # Générer le bateau n°2 à la verticale et qui n'est pas collé au bateau n°1
        pos3 = (randint(0, 3), randint(0, 4))  # Première position aléatoire
        while abs(pos1[0] - pos3[0]) < 2 or abs(
                pos3[1] - pos1[1]) < 2:  # Tant que le bateau n'est pas assez éloigné du bateau n°1
            pos3 = (randint(0, 4), randint(0, 3))  # On génère une nouvelle position aléatoire

        pos4 = (pos3[0], pos3[1] + 1)  # On génère la deuxième position du bateau n°2

    # On génère le plateau de jeu avec les bateaux
    for i in range(5):
        row = []
        for j in range(5):
            if (i, j) in [pos1, pos2, pos3, pos4]:  # Si la position est celle d'un bateau
                row.append("#")  # On ajoute un bateau
            else:
                row.append("-")  # Sinon on ajoute de l'eau
        plate.append(row)

    return plate  # On retourne le plateau de jeu
