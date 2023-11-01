"""
Projet : Bataille Navale
Auteurs : Pierre BIDET, Anaëlle BOUSSIN
Languages : Python
Classe : 1G NSI
Licence : GPL-3.0
"""


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


def askPosition():
    inp = input("Entrez la position à frapper (type a5) -> ")
    if len(inp) == 2:
        if inp[0] in "abcdeABCDE" and inp[1] in "12345":
            return inp[0].lower() + inp[1]
        else:
            print("La position est incorrecte !")
            return askPosition()
    else:
        print("La position est incorrecte !")
        return askPosition()


def getIndexFromPosition(position: str) -> tuple:
    return "abcde".index(position[0]), int(position[1]) - 1


def getNearestBoatDelta(plateau: [[]], position: ()) -> int:
    pos1, pos2 = position
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
