import customtkinter


class Homepage(customtkinter.CTkFrame): # Component that contains the homepage
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
