"""
Projet : Bataille Navale
Auteurs : Pierre BIDET, Anaëlle BOUSSIN
Languages : Python
Classe : 1G NSI
Licence : GPL-3.0
"""


def getNearestBoatDelta(plateau: [[]],
                        position: ()) -> int:  # Fonction qui retourne le delta entre la position et le bateau le plus proche
    pos1, pos2 = position # pos1 = ligne, pos2 = colonne
    delta = 5  # Initialise la variable delta à une valeur maximale (5 dans ce cas)

    # Calcul des bateaux dans la ligne de la position
    for index, val in enumerate(plateau[pos1]):  # Pour chaque élément de la ligne
        if val == "#":  # Si l'élément est un bateau
            if abs(index - pos2) < delta:  # Si la distance entre l'élément et la position est inférieure à delta
                delta = abs(index - pos2)  # On met à jour delta

    # Calcul des bateaux dans la colonne de la position
    for index, row in enumerate(plateau):  # Pour chaque ligne
        val = row[pos2]  # On récupère l'élément de la colonne
        if val == "#":  # Si l'élément est un bateau
            if abs(index - pos1) < delta:  # Si la distance entre l'élément et la position est inférieure à delta
                delta = abs(index - pos1)  # On met à jour delta

    return delta  # On retourne delta
