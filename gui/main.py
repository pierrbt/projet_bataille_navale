"""
Projet : Bataille Navale
Auteurs : Pierre BIDET, Anaëlle BOUSSIN
Languages : Python
Classe : 1G NSI
Licence : GPL-3.0
"""

import customtkinter  # Importe le module customtkinter

# Importe les composants
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
    def quit():  # Fonction qui quitte le jeu
        print("Quitting...")  # Affiche "Quitting..." dans la console
        global frame, globalPoints  # Récupère les variables globales frame et globalPoints
        frame.destroy()  # Détruit la frame
        frame = Leaderboard(app, globalPoints)  # Crée la frame du leaderboard


    def restart():  # Fonction qui redémarre le jeu
        print("Restarting...")  # Affiche "Restarting..." dans la console
        global frame, players  # Récupère les variables globales frame et players
        frame.destroy()  # Détruit la frame
        frame = Game(app, players, globalPoints, restart, quit)  # Crée la frame du jeu


    def switchPage():  # Fonction qui change de page
        global frame, globalPoints, players  # Récupère les variables globales frame, globalPoints et players
        players = int(frame.input.get())  # Récupère le nombre de joueurs
        if not 1 <= players <= 9:  # Si le nombre de joueurs n'est pas compris entre 1 et 9
            return  # On annule la fonction
        frame.destroy()  # Détruit la frame
        frame = Game(app, players, globalPoints, restart, quit)  # Crée la frame du jeu


    frame = Homepage(app, switchPage)  # On crée la frame de la page d'accueil
    globalPoints = []  # On crée une liste vide qui contiendra les points de chaque joueur
    players = 1  # On initialise le nombre de joueurs à 1

    app.mainloop()  # On lance la boucle principale

# main.py
