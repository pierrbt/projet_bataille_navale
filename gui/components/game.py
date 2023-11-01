import customtkinter
from ..utils import getNearestBoatDelta
from ..plate import generatePlate
from CTkTable import *
import time


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

        self.table = CTkTable(master=self, row=5, column=5, values=self.disp, hover_color="#555555",
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
                self.text.configure(text=f"Fin de la partie {len(self.globalPoints)} !")
                points = [[f"Joueur {i + 1}", f"{self.points[i]}"] for i in range(self.maxPlayers)]
                self.results = CTkTable(master=app, row=self.maxPlayers, column=2, values=points,
                                        hover_color="#555555", )
                self.results.place(relx=0.5, rely=0.4, anchor=customtkinter.CENTER)
                self.button = customtkinter.CTkButton(master=self, text="Recommencer", command=self.restart)
                self.button2 = customtkinter.CTkButton(master=self, text="Quitter", command=self.quit)

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
