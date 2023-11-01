import customtkinter
from CTkTable import *


class Leaderboard(customtkinter.CTkFrame):
    def __init__(self, master, globalPoints, **kwargs):
        super().__init__(master, **kwargs)
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

        self.table = CTkTable(master=self, row=len(display), column=len(display[0]), values=display, hover_color="#555555",)
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

