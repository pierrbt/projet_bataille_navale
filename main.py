"""
Projet : Bataille Navale
Auteurs : Pierre BIDET, Anaëlle BOUSSIN
Languages : Python
Classe : 1G NSI
Licence : GPL-3.0
"""

from random import randint

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
    bateaux_joueurs = {}
    for i in range(1,nb_joueurs + 1):
        bateaux_joueurs[i] = [(randint(0,5), randint(0,5)) for _ in range(3)]
    print(bateaux_joueurs)

if __name__ == '__main__':
    Jeu()

# main.py
