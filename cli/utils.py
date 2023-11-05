"""
Projet : Bataille Navale
Auteurs : Pierre BIDET, Anaëlle BOUSSIN
Languages : Python
Classe : 1G NSI
Licence : GPL-3.0
"""


def askInt(question: str, mini=0, maxi=9999) -> int:  # Demande un entier à l'utilisateur
    isOk = False  # Initialise la variable isOk à False
    number = 0  # Initialise la variable number à 0
    while not isOk:  # Tant que la valeur n'est pas correcte
        inp = input(question)  # On demande la valeur à l'utilisateur
        if inp.isnumeric():  # Si la valeur est un entier
            number = int(inp)  # On convertit la valeur en entier
            if number < mini or number > maxi:  # Si la valeur est hors des bornes
                print(f"La valeur est hors des bornes {mini}-{maxi}")  # On affiche un message d'erreur
            else:  # Sinon
                isOk = True  # On passe la variable isOk à True
        else:  # Sinon
            print("Ceci n'est pas un entier !")  # On affiche un message d'erreur
    return number  # On retourne la valeur


def askPosition():
    inp = input("Entrez la position à frapper (type a5) -> ")  # On demande la position à frapper
    if len(inp) == 2:  # Si la position est de longueur 2
        if inp[0] in "abcdeABCDE" and inp[1] in "12345":  # Si la position est correcte
            return inp[0].lower() + inp[1]  # On retourne la position
        else:  # Sinon
            print("La position est incorrecte !")  # On affiche un message d'erreur
            return askPosition()  # On redemande la position
    else:  # Sinon
        print("La position est incorrecte !")  # On affiche un message d'erreur
        return askPosition()  # On redemande la position


def getIndexFromPosition(position: str) -> tuple:  # Récupère les index d'une position
    return "abcde".index(position[0]), int(
        position[1]) - 1  # On retourne l'index correspondant à la lettre et le nombre


def getNearestBoatDelta(plateau: [[]],
                        position: ()) -> int:  # Récupère le delta entre la position et le bateau le plus proche
    pos1, pos2 = position  # pos1 = ligne, pos2 = colonne
    delta = 5  # Initialise la variable delta à une valeur maximale (5 dans ce cas)

    # Calcul des bateaux dans la ligne de la position
    for index, val in enumerate(plateau[pos1]):  # Pour chaque valeur de la ligne
        if val == "#":  # Si la valeur est un bateau
            if abs(index - pos2) < delta:  # Si la valeur est plus proche que le delta actuel
                delta = abs(index - pos2)  # On remplace le delta par la valeur

    # Calcul des bateaux dans la colonne de la position
    for index, row in enumerate(plateau):  # Pour chaque ligne
        val = row[pos2]  # On récupère la valeur de la colonne
        if val == "#":  # Si la valeur est un bateau
            if abs(index - pos1) < delta:  # Si la valeur est plus proche que le delta actuel
                delta = abs(index - pos1)  # On remplace le delta par la valeur

    return delta  # On retourne le delta
