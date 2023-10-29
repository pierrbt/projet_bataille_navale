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

    tableau = generatePlate()

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
