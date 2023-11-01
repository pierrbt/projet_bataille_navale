"""
Projet : Bataille Navale
Auteurs : Pierre BIDET, Anaëlle BOUSSIN
Languages : Python
Classe : 1G NSI
Licence : GPL-3.0
"""

import customtkinter

from components.game import Game
from components.home import Homepage
from components.leaderboard import Leaderboard

if __name__ == '__main__':
    print("Bienvenue sur l'excellente bataille navale !!")

    customtkinter.set_appearance_mode("dark")
    customtkinter.set_default_color_theme("blue")

    app = customtkinter.CTk()  # On crée la fenêtre
    app.geometry("400x240")
    app.title("Bataille navale")  # Nom de la fenêtre

    app.minsize(400, 240)  # Taille minimale de la fenêtre

    # Fonctions de callback
    def quit():
        print("Quitting...")
        global frame, globalPoints
        frame.destroy()
        frame = Leaderboard(app, globalPoints)


    def restart():
        print("Restarting...")
        global frame, players
        frame.destroy()
        frame = Game(app, players, globalPoints, restart, quit)


    def switchPage():
        global frame, globalPoints, players
        players = int(frame.input.get())
        frame.destroy()
        frame = Game(app, players, globalPoints, restart, quit)


    frame: Homepage = Homepage(app, switchPage)  # On crée la frame de la page d'accueil
    globalPoints = []  # On crée une liste vide qui contiendra les points de chaque joueur
    players = 1  # On initialise le nombre de joueurs à 1

    app.mainloop()  # On lance la boucle principale

# main.py
