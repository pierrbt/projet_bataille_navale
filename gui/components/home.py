"""
Projet : Bataille Navale
Auteurs : Pierre BIDET, Anaëlle BOUSSIN
Languages : Python
Classe : 1G NSI
Licence : GPL-3.0
"""

import customtkinter  # Importe le module customtkinter


class Homepage(customtkinter.CTkFrame):  # Crée la classe Homepage qui hérite de la classe CTkFrame
    def __init__(self, master, callback, **kwargs):
        super().__init__(master, **kwargs)
        self.callback = callback  # Initialise le callback
        self.configure(fg_color="transparent")
        self.pack(fill=customtkinter.BOTH, expand=True)

        self.text = customtkinter.CTkLabel(master=self,
                                           text="Bienvenue sur l'excellente bataille navale !!")  # Crée le texte de bienvenue
        self.text.place(relx=0.5, rely=0.3, anchor=customtkinter.CENTER)
        self.text2 = customtkinter.CTkLabel(master=self,
                                            text="Entrez le nombre de joueur -> ")  # Crée le texte pour entrer le nombre de joueurs
        self.text2.place(relx=0.3, rely=0.5, anchor=customtkinter.CENTER)

        self.input = customtkinter.CTkComboBox(master=self, values=["1", "2", "3", "4", "5", "6", "7", "8",
                                                                    "9"])  # Crée la zone de saisie du nombre de joueurs
        self.input.place(relx=0.7, rely=0.5, anchor=customtkinter.CENTER)

        self.button = customtkinter.CTkButton(master=self, text="Valider",
                                              command=callback)  # Crée le bouton de validation
        self.button.place(relx=0.5, rely=0.7, anchor=customtkinter.CENTER)
