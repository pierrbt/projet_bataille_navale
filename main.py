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


def Jeu() -> None:
    print("Bienvenue sur l'excellente bataille navale !!")
    nb_joueurs = askInt("Entrez le nombre de joueur -> ", mini=2, maxi=9)
    print("Génération du plateau")
    pos1 = (randint(0,5), randint(0,5))
    if choice(["V", "H"]) == "V":
        print("v")
        pos2 = (pos1[0], pos1[1] + 1)
        if pos2[1] > 5:
            pos2[1] -= 2
    else:
        print("h")
        pos2 = (pos1[0], pos1[1] + 1)
        if pos2[1] > 5:
            pos2[1] -= 2
    print(pos1, pos2)
if __name__ == '__main__':
    Jeu()

# main.py
