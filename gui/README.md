
# Informations

Ce dossier contient les fichiers de l'interface graphique.
Vous pouvez lancer le projet depuis le fichier `main.py`.

Ou en utilisant la version compilée dans bin. (Windows uniquement)
Afin de recompiler le projet, vous aurez besoin de pyinstaller.
Voici la configuration utilisée pour la compilation:
```bash
pyinstaller --noconfirm --onedir --windowed --add-data "C:\Users\pierr\AppData\Local\Programs\Python\Python311\Lib\site-packages/customtkinter;customtkinter/"  --add-data "C:\Users\pierr\AppData\Local\Programs\Python\Python311\Lib\site-packages/CtkTable;customtkinter/" "../main.py"
```

Vous devrez l'adapter avec votre chemin vers customtkinter et CtkTable, ainsi que le chemin vers main.py.


# Informations sur le projet

Projet : Bataille Navale
Auteurs : Pierre BIDET, Anaëlle BOUSSIN
Languages : Python
Classe : 1G NSI
Licence : GPL-3.0

