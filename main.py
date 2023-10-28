"""
Projet : Bataille Navale
Auteurs : Pierre BIDET, Anaëlle BOUSSIN
Languages : Python
Classe : 1G NSI
Licence : GPL-3.0
"""
from typing import List
import time
import customtkinter
from plate import generatePlate
from utils import askPosition, getIndexFromPosition, getNearestBoatDelta, askInt


def jouerUnePartie(nb_joueurs: int) -> List[int]:  # Fonction qui permet de jouer une partie

    points_joueurs = []  # Liste des points des joueurs

    for i in range(1, nb_joueurs + 1):
        plateau = generatePlate()
        points = 0
        print(f"\n----------------------------\n\nJoueur n°{i} : ")
        print('\n '.join([''.join(['{:4}'.format(item) for item in row]) for row in plateau]), end="\n\n",)
        for j in range(1, 4):
            print(f"Essai n{j}")
            position = askPosition()
            pos1, pos2 = getIndexFromPosition(position)
            if plateau[pos1][pos2] == "#":
                print("Touché !")
                points += 1
                plateau[pos1][pos2] = "X"
                # Get nearest # to pos1, pos2 in order to see if it is touched or destroyed
                delta = getNearestBoatDelta(plateau, (pos1, pos2))
                if delta > 1:
                    print("Coulé !")
                    points += 7
            else:
                print("Raté !")
                plateau[pos1][pos2] = "O"
        print(f"Vous cumulez {points} points")
        points_joueurs.append(points)
    return points_joueurs


if __name__ == '__main__':
    print("Bienvenue sur l'excellente bataille navale !!")
    nb_joueurs = askInt("Entrez le nombre de joueur -> ", mini=2, maxi=9)

    wantToContinue = True
    points_totaux = [0 for _ in range(nb_joueurs)]

    while wantToContinue:
        points = jouerUnePartie(nb_joueurs)
        for i,pts in enumerate(points):
            points_totaux[i] += pts

        wantToContinue = input("\nVoulez-vous continuer (o/n) -> ") == "o"
    print("\nVoici le résumé des scores : ")
    for joueur, points in enumerate(points_totaux):
        print(f"Joueur {joueur + 1} : {points} points")

    gagnants = []
    maxi = max(points_totaux)
    for index, points in enumerate(points_totaux):
        if points == maxi:
            gagnants.append(index)

    if len(gagnants) == 1:
        print(f"\nLe joueur {gagnants[0] + 1} a gagné")
    else:
        print(f"\nLes joueurs {','.join(gagnants)} ont gagné")



    """customtkinter.set_appearance_mode("System")  # Modes: system (default), light, dark
    customtkinter.set_default_color_theme("blue")  # Themes: blue (default), dark-blue, green

    app = customtkinter.CTk()  # create CTk window like you do with the Tk window
    app.geometry("400x240")
    app.title("Bataille navale")

    app.minsize(400, 240)

    text = customtkinter.CTkLabel(master=app, text="Bienvenue sur l'excellente bataille navale !!")
    text.place(relx=0.5, rely=0.3, anchor=customtkinter.CENTER)
    text2 = customtkinter.CTkLabel(master=app, text="Entrez le nombre de joueur -> ")
    text2.place(relx=0.3, rely=0.5, anchor=customtkinter.CENTER)

    input = customtkinter.CTkComboBox(master=app, values=["1", "2", "3", "4", "5", "6", "7", "8", "9"])
    input.place(relx=0.7, rely=0.5, anchor=customtkinter.CENTER)


    def button_function():
        inp = int(input.get())
        if 1 <= inp <= 10:
            text2.destroy()
            button.destroy()
            input.destroy()
            for _ in range(1, inp + 1):
                text.configure(text=f"Joueur {_}")
                text.update()
                time.sleep(1)



    button = customtkinter.CTkButton(master=app, text="Valider", command=button_function)
    button.place(relx=0.5, rely=0.7, anchor=customtkinter.CENTER)

    app.mainloop()"""


# main.py
