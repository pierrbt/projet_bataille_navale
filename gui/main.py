"""
Projet : Bataille Navale
Auteurs : Pierre BIDET, Anaëlle BOUSSIN
Languages : Python
Classe : 1G NSI
Licence : GPL-3.0
"""
import time

import customtkinter
from CTkTable import *

from plate import generatePlate
from utils import getNearestBoatDelta


class Homepage(customtkinter.CTkFrame):
    def __init__(self, master, callback, **kwargs):
        super().__init__(master, **kwargs)
        self.callback = callback
        self.configure(fg_color="transparent")
        self.pack(fill=customtkinter.BOTH, expand=True)

        self.text = customtkinter.CTkLabel(master=self, text="Bienvenue sur l'excellente bataille navale !!")
        self.text.place(relx=0.5, rely=0.3, anchor=customtkinter.CENTER)
        self.text2 = customtkinter.CTkLabel(master=self, text="Entrez le nombre de joueur -> ")
        self.text2.place(relx=0.3, rely=0.5, anchor=customtkinter.CENTER)

        self.input = customtkinter.CTkComboBox(master=self, values=["1", "2", "3", "4", "5", "6", "7", "8", "9"])
        self.input.place(relx=0.7, rely=0.5, anchor=customtkinter.CENTER)

        self.button = customtkinter.CTkButton(master=self, text="Valider", command=callback)
        self.button.place(relx=0.5, rely=0.7, anchor=customtkinter.CENTER)


class Game(customtkinter.CTkFrame):
    def __init__(self, master, players, globalPoints, restart, quit, **kwargs):
        super().__init__(master, **kwargs)
        self.globalPoints = globalPoints
        self.maxPlayers = players
        self.restart = restart
        self.quit = quit

        self.points = [0 for _ in range(self.maxPlayers)]
        self.configure(fg_color="transparent")
        self.pack(fill=customtkinter.BOTH, expand=True)

        self.player = 1
        self.round = 1

        self.tab = generatePlate()
        self.disp = [["-" for i in range(5)] for j in range(5)]

        self.text = customtkinter.CTkLabel(master=self, text=f"Joueur {self.player} (essai {self.round})")
        self.text.place(relx=0.5, rely=0.1, anchor=customtkinter.CENTER)


        self.table = CTkTable(master=app, row=5, column=5, values=self.disp, hover_color="#555555",
                              command=self.update_component, width=30, height=30)
        self.table.place(relx=0.5, rely=0.5, anchor=customtkinter.CENTER)

        self.coup = customtkinter.CTkLabel(master=self)
        self.coup.place(relx=0.5, rely=0.9, anchor=customtkinter.CENTER)

    def update_component(self, values):
        row = values["row"]
        col = values["column"]

        if self.tab[row][col] == "#":
            self.points[self.player - 1] += 1
            self.tab[row][col] = "X"
            self.disp[row][col] = "X"
            self.coup.configure(text="Touché !")
            delta = getNearestBoatDelta(self.tab, (row, col))
            if delta > 1:
                self.points[self.player - 1] += 7
                self.coup.configure(text="Coulé !")
        else:
            self.disp[row][col] = "O"
            self.coup.configure(text="Raté !")

        if self.round == 3:
            self.table.update_values(values=self.disp)
            self.table.update()
            time.sleep(1)
            if self.player < self.maxPlayers:
                self.player += 1
                self.round = 0
                self.disp = [["-" for i in range(5)] for j in range(5)]
                self.tab = generatePlate()
            else:
                self.globalPoints.append(self.points)
                self.table.destroy()
                self.coup.destroy()
                self.text.configure(text=f"Fin de la partie {len(globalPoints)} !")
                points = [[ f"Joueur {i + 1}", f"{self.points[i]}"] for i in range(self.maxPlayers)]
                self.results = CTkTable(master=app, row=self.maxPlayers, column=2, values=points, hover_color="#555555",)
                self.results.place(relx=0.5, rely=0.4, anchor=customtkinter.CENTER)
                self.button = customtkinter.CTkButton(master=self, text="Recommencer", command=restart)
                self.button2 = customtkinter.CTkButton(master=self, text="Quitter", command=quit)

                gagnants = []
                maxi = max(self.points)
                for index, points in enumerate(self.points):
                    if points == maxi:
                        gagnants.append(str(index + 1))

                self.winner = customtkinter.CTkLabel(master=self)

                if len(gagnants) == 1:
                    self.winner.configure(text=f"Le joueur {gagnants[0]} a gagné")
                else:
                    self.winner.configure(text=f"Les joueurs {','.join(gagnants)} ont gagné")

                self.winner.place(relx=0.5, rely=0.75, anchor=customtkinter.CENTER)

                self.button.place(relx=0.3, rely=0.9, anchor=customtkinter.CENTER)
                self.button2.place(relx=0.7, rely=0.9, anchor=customtkinter.CENTER)
                return
        self.round += 1

        self.text.configure(text=f"Joueur {self.player} (essai {self.round})")
        self.table.update_values(values=self.disp)

class Leaderboard(customtkinter.CTkFrame):
    def __init__(self, master, globalPoints, **kwargs):
        super().__init__(master, **kwargs)
        print(globalPoints)
        playerPoints = [0 for _ in range(len(globalPoints[0]))]
        for game in globalPoints:
            for index, points in enumerate(game):
                playerPoints[index] += points


        self.configure(fg_color="transparent")
        self.pack(fill=customtkinter.BOTH, expand=True)

        self.text = customtkinter.CTkLabel(master=self, text="Voici le résumé des scores : ")
        self.text.place(relx=0.5, rely=0.1, anchor=customtkinter.CENTER)
        # Create a table with the results
        display = [[f"Joueur {i+1}", f"{playerPoints[i]} pts"] for i in range(len(playerPoints))]

        self.table = CTkTable(master=app, row=len(display), column=len(display[0]), values=display, hover_color="#555555",)
        self.table.place(relx=0.5, rely=0.5, anchor=customtkinter.CENTER)

        # Create a label with the winner
        gagnants = []
        maxi = max(playerPoints)
        for index, points in enumerate(playerPoints):
            if points == maxi:
                gagnants.append(str(index + 1))

        self.winner = customtkinter.CTkLabel(master=self)
        if len(gagnants) == 1:
            self.winner.configure(text=f"Le joueur {gagnants[0]} a gagné")
        else:
            self.winner.configure(text=f"Les joueurs {','.join(gagnants)} ont gagné")

        self.winner.place(relx=0.5, rely=0.90, anchor=customtkinter.CENTER)


if __name__ == '__main__':
    print("Bienvenue sur l'excellente bataille navale !!")

    customtkinter.set_appearance_mode("dark")  # Modes: system (default), light, dark
    customtkinter.set_default_color_theme("blue")  # Themes: blue (default), dark-blue, green

    app = customtkinter.CTk()  # create CTk window like you do with the Tk window
    app.geometry("400x240")
    app.title("Bataille navale")

    app.minsize(400, 240)


    def quit():
        print("Quitting...")
        global frame, globalPoints
        # Get the globalPoints
        # Destroy the current frame
        frame.destroy()
        # Create a new frame with the results
        frame = Leaderboard(app, globalPoints)
        pass


    def restart():
        print("Restarting...")
        global frame, players
        # Destroy the current frame
        frame.destroy()
        # Create a new frame with the new Game
        frame = Game(app, players, globalPoints, restart, quit)


    def switchPage():
        global frame, globalPoints, players
        players = int(frame.input.get())
        frame.destroy()
        frame = Game(app, players, globalPoints, restart, quit)




    frame = Homepage(app, switchPage)
    globalPoints = []
    players = 1

    app.mainloop()

    print(globalPoints)

# main.py
