"""
Projet : Bataille Navale
Auteurs : Pierre BIDET, Anaëlle BOUSSIN
Languages : Python
Classe : 1G NSI
Licence : GPL-3.0
"""

def getNearestBoatDelta(plateau: [[]], position: ()) -> int:
    pos1, pos2 = position
    delta = 5  # Initialise la variable delta à une valeur maximale (5 dans ce cas)

    # Calcul des bateaux dans la ligne de la position
    for index, cell in enumerate(plateau[pos2]):
        if cell == "#":
            # Si un bateau est trouvé dans la même ligne
            if abs(index - pos1) < delta:
                delta = abs(index - pos1)  # Met à jour la valeur de delta si le bateau est plus proche

    # Calcul des bateaux dans la colonne de la position
    for index, row in enumerate(plateau):
        cell = row[pos1]
        if cell == "#":
            # Si un bateau est trouvé dans la même colonne
            if abs(index - pos2) < delta:
                delta = abs(index - pos2)  # Met à jour la valeur de delta si le bateau est plus proche

    return delta
