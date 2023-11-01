"""
Projet : Bataille Navale
Auteurs : Pierre BIDET, Anaëlle BOUSSIN
Languages : Python
Classe : 1G NSI
Licence : GPL-3.0
"""

def getNearestBoatDelta(plateau: [[]], position: ()) -> int:
    pos1, pos2 = position # pos1 = ligne, pos2 = colonne
    delta = 5  # Initialise la variable delta à une valeur maximale (5 dans ce cas)

    # Calcul des bateaux dans la ligne de la position
    for index, val in enumerate(plateau[pos1]):
        if val == "#":
            if abs(index - pos2) < delta:
                delta = abs(index - pos2)

    # Calcul des bateaux dans la colonne de la position
    for index, row in enumerate(plateau):
        val = row[pos2]
        if val == "#":
            if abs(index - pos1) < delta:
                delta = abs(index - pos1)

    return delta
