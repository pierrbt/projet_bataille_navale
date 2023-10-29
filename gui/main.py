"""
Projet : Bataille Navale
Auteurs : Pierre BIDET, Anaëlle BOUSSIN
Languages : Python
Classe : 1G NSI
Licence : GPL-3.0
"""
import time
import customtkinter
from plate import generatePlate
from utils import getNearestBoatDelta
from CTkTable import *

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
    def __init__(self, master, players, **kwargs):
        super().__init__(master, **kwargs)

        self.maxPlayers = players
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

    def update_component(self, values):
        row = values["row"]
        col = values["column"]

        if self.tab[row][col] == "#":
            self.points[self.player - 1] += 1
            self.tab[row][col] = "X"
            self.disp[row][col] = "X"
            delta = getNearestBoatDelta(self.tab, (row, col))
            if delta > 1:
                self.points[self.player - 1] += 7
        else:
            self.disp[row][col] = "O"


        #print(row, col)
        print(self.player, self.maxPlayers, self.round)

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
                print("terminégros")
                self.table.destroy()
                self.text.configure(text="Fin de la partie !")
                self.button = customtkinter.CTkButton(master=self, text="Recommencer", command=lambda: print("restart"))
                self.button2 = customtkinter.CTkButton(master=self, text="Quitter", command=lambda: print("quit"))
                self.button.place(relx=0.3, rely=0.8, anchor=customtkinter.CENTER)
                self.button2.place(relx=0.7, rely=0.8, anchor=customtkinter.CENTER)
                return
        self.round += 1

        self.text.configure(text=f"Joueur {self.player} (essai {self.round})")
        self.table.update_values(values=self.disp)



if __name__ == '__main__':
    print("Bienvenue sur l'excellente bataille navale !!")

    customtkinter.set_appearance_mode("dark")  # Modes: system (default), light, dark
    customtkinter.set_default_color_theme("blue")  # Themes: blue (default), dark-blue, green

    app = customtkinter.CTk()  # create CTk window like you do with the Tk window
    app.geometry("400x240")
    app.title("Bataille navale")

    app.minsize(400, 240)

    text = customtkinter.CTkLabel(master=app, text="Bienvenue sur l'excellente bataille navale !!")
    text.place(relx=0.5, rely=0.3, anchor=customtkinter.CENTER)
    text2 = customtkinter.CTkLabel(master=app, text="Entrez le nombre de joueur -> ")
    text2.place(relx=0.3, rely=0.5, anchor=customtkinter.CENTER)

    display_table = [list("/ABCDE")]
    for i, row in enumerate(tableau):
        line = [str(i + 1)]
        for j in row:
            line.append(j)
        display_table.append(line)
    for row in display_table:
        print(row)

    input = customtkinter.CTkComboBox(master=app, values=["1", "2", "3", "4", "5", "6", "7", "8", "9"])
    input.place(relx=0.7, rely=0.5, anchor=customtkinter.CENTER)

    def displayCell(val: dict):
        row = val.get("row")
        column = val.get("column")
        value = val.get("value")

        print(f"Row: {row}, Column: {column}, Value: {value}")

    table = CTkTable(master=app, row=5, column=5, values=display_table, hover_color="#555555", orientation="vertical", command=displayCell, justify="stretch")
    table.place(relx=0.5, rely=0.8, anchor=customtkinter.CENTER)
    # set the table square



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

    app.mainloop()




# main.py
