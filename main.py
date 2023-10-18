"""
Projet : Bataille Navale
Auteurs : Pierre BIDET, Anaëlle BOUSSIN
Languages : Python
Classe : 1G NSI
Licence : GPL-3.0
"""

from random import randint, choice

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

    if choice(["V", "H"]) == "V":
        pos1 = (randint(0,4), randint(0,3))
        pos2 = (pos1[0], pos1[1] + 1)
    else:
        pos1 = (randint(0,3), randint(0,4))
        pos2 = (pos1[0] + 1, pos1[1])

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
        print('\n'.join([''.join(['{:4}'.format(item) for item in row]) for row in plateau]), end="\n\n")


if __name__ == '__main__':
    Jeu()

# main.py
