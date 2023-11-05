"""
Projet : Bataille Navale
Auteurs : Pierre BIDET, Anaëlle BOUSSIN
Languages : Python
Classe : 1G NSI
Licence : GPL-3.0
"""

import sys  # Importe le module sys
import time  # Importe le module time

import customtkinter  # Importe le module customtkinter
from CTkTable import *  # Importe la classe CTkTable

sys.path.append('../')  # Ajoute le dossier parent au path
from plate import generatePlate  # Importe la fonction generatePlate du module plate
from utils import getNearestBoatDelta  # Importe la fonction getNearestBoatDelta du module utils


class Game(customtkinter.CTkFrame):  # Crée la classe Game qui hérite de la classe CTkFrame
    def __init__(self, master, players, globalPoints, restart, quit, **kwargs):
        super().__init__(master, **kwargs)
        self.globalPoints = globalPoints
        self.maxPlayers = players
        self.restart = restart
        self.quit = quit

        self.points = [0 for _ in range(self.maxPlayers)]  # Initialise la liste des points de chaque joueur
        self.configure(fg_color="transparent")
        self.pack(fill=customtkinter.BOTH, expand=True)

        self.player = 1
        self.round = 1

        self.tab = generatePlate()  # Génère le plateau de jeu
        self.disp = [["-" for i in range(5)] for j in range(5)]  # Initialise le plateau de jeu affiché

        self.text = customtkinter.CTkLabel(master=self, text=f"Joueur {self.player} (essai {self.round})")
        self.text.place(relx=0.5, rely=0.1, anchor=customtkinter.CENTER)

        self.table = CTkTable(master=self, row=5, column=5, values=self.disp, hover_color="#555555",
                              command=self.update_component, width=30, height=30)
        self.table.place(relx=0.5, rely=0.5, anchor=customtkinter.CENTER)

        self.coup = customtkinter.CTkLabel(master=self, text="Cliquez sur une case pour commencer")
        self.coup.place(relx=0.5, rely=0.9, anchor=customtkinter.CENTER)

    def update_component(self, values):  # Fonction qui met à jour le composant quand on clique sur une case
        row = values["row"]  # Récupère la ligne
        col = values["column"]  # Récupère la colonne

        if self.tab[row][col] == "#":  # Si la position est celle d'un bateau
            self.points[self.player - 1] += 1  # On ajoute 1 point au joueur
            self.tab[row][col] = "X"
            self.disp[row][col] = "X"
            self.coup.configure(text="Touché !")
            delta = getNearestBoatDelta(self.tab, (row, col))  # On récupère le delta
            if delta > 1:  # Si delta < 1 (que le bateau est coulé car la case collée est déjà touchée)
                self.points[self.player - 1] += 7  # On ajoute 7 points au joueur
                self.coup.configure(text="Coulé !")
        else:
            self.disp[row][col] = "O"
            self.coup.configure(text="Raté !")

        if self.round == 3:  # Si le joueur a fait 3 essais
            self.table.update_values(values=self.disp)
            self.table.update()
            time.sleep(.6)  # On attend 0.6 secondes pour que le joueur puisse voir le résultat
            if self.player < self.maxPlayers:  # Si ce n'est pas le dernier joueur
                self.player += 1  # On passe au joueur suivant
                self.round = 0  # On réinitialise le nombre d'essais
                self.disp = [["-" for i in range(5)] for j in range(5)]  # On réinitialise le plateau de jeu affiché
                self.tab = generatePlate()  # On génère un nouveau plateau de jeu
                self.coup.configure(
                    text="Cliquez sur une case pour commencer")  # On affiche le message "Cliquez sur une case pour commencer"
            else:  # Si c'est le dernier joueur
                self.globalPoints.append(self.points)  # On ajoute les points du joueur à la liste des points globaux
                self.table.destroy()  # On détruit le tableau
                self.coup.destroy()  # On détruit le label
                self.text.configure(
                    text=f"Fin de la partie {len(self.globalPoints)} !")  # On affiche le message "Fin de la partie {len(self.globalPoints)} !"
                points = [[f"Joueur {i + 1}", f"{self.points[i]}"] for i in
                          range(self.maxPlayers)]  # On crée une liste de points
                self.results = CTkTable(master=self, row=self.maxPlayers, column=2, values=points, width=30, height=30,
                                        hover_color="#555555", )  # On crée un tableau avec les points de chaque joueur
                self.results.place(relx=0.5, rely=0.4, anchor=customtkinter.CENTER)
                self.button = customtkinter.CTkButton(master=self, text="Recommencer", command=self.restart)
                self.button2 = customtkinter.CTkButton(master=self, text="Quitter", command=self.quit)

                gagnants = []  # On crée une liste des gagnants
                maxi = max(self.points)  # On récupère le score maximum
                for index, points in enumerate(self.points):  # Pour chaque joueur
                    if points == maxi:  # Si le joueur a le score maximum
                        gagnants.append(str(index + 1))  # On ajoute le joueur à la liste des gagnants

                self.winner = customtkinter.CTkLabel(master=self)  # On crée un label pour afficher le gagnant

                if len(gagnants) == 1:  # Si il n'y a qu'un seul gagnant
                    self.winner.configure(text=f"Le joueur {gagnants[0]} a gagné")  # On affiche le joueur qui a gagné
                else:  # Si il y a plusieurs gagnants
                    self.winner.configure(
                        text=f"Les joueurs {','.join(gagnants)} ont gagné")  # On affiche les joueurs qui ont gagné

                self.winner.place(relx=0.5, rely=0.75, anchor=customtkinter.CENTER)

                self.button.place(relx=0.3, rely=0.9, anchor=customtkinter.CENTER)
                self.button2.place(relx=0.7, rely=0.9, anchor=customtkinter.CENTER)
                return
        self.round += 1

        self.text.configure(text=f"Joueur {self.player} (essai {self.round})")
        self.table.update_values(values=self.disp)
