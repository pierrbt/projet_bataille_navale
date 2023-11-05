"""
Projet : Bataille Navale
Auteurs : Pierre BIDET, Anaëlle BOUSSIN
Languages : Python
Classe : 1G NSI
Licence : GPL-3.0
"""

import customtkinter  # Importe le module customtkinter
from CTkTable import *  # Importe la classe CTkTable


class Leaderboard(customtkinter.CTkFrame):  # Crée la classe Leaderboard qui hérite de la classe CTkFrame
    def __init__(self, master, globalPoints, **kwargs):
        super().__init__(master, **kwargs)
        playerPoints = [0 for _ in range(len(globalPoints[0]))]  # Initialise la liste des points de chaque joueur
        for game in globalPoints:  # Pour chaque partie
            for index, points in enumerate(game):  # Pour chaque joueur
                playerPoints[index] += points  # On ajoute les points du joueur à la liste des points


        self.configure(fg_color="transparent")
        self.pack(fill=customtkinter.BOTH, expand=True)

        self.text = customtkinter.CTkLabel(master=self, text="Voici le résumé des scores : ")
        self.text.place(relx=0.5, rely=0.1, anchor=customtkinter.CENTER)

        display = [[f"Joueur {i + 1}", f"{playerPoints[i]} pts"] for i in
                   range(len(playerPoints))]  # Initialise le tableau des scores

        self.table = CTkTable(master=self, row=len(display), column=len(display[0]), values=display,
                              hover_color="#555555", )  # Crée le tableau des scores
        self.table.place(relx=0.5, rely=0.5, anchor=customtkinter.CENTER)

        # Meme logique pour déterminer le gagnant que dans game.py
        gagnants = []  # Initialise la liste des gagnants
        maxi = max(playerPoints)  # Récupère le score maximum
        for index, points in enumerate(playerPoints):  # Pour chaque joueur
            if points == maxi:  # Si le joueur a le score maximum
                gagnants.append(str(index + 1))  # On l'ajoute à la liste des gagnants

        self.winner = customtkinter.CTkLabel(master=self)
        if len(gagnants) == 1:  # Si il n'y a qu'un seul gagnant
            self.winner.configure(text=f"Le joueur {gagnants[0]} a gagné")  # On affiche le gagnant
        else:  # Sinon
            self.winner.configure(text=f"Les joueurs {','.join(gagnants)} ont gagné")  # On affiche les gagnants

        self.winner.place(relx=0.5, rely=0.90, anchor=customtkinter.CENTER)

