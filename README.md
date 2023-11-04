# Bataille navale

Voici le projet bataille navale, deuxième projet de NSI en 1G SPE NSI.
Veuillez lire la (fiche de projet)[https://docs.google.com/document/d/1riDNvgQS0Sdhk8hi8XL-WjN9lX2G-O65f6PdLyULSZk/edit?usp=sharing] pour plus d'informations sur le projet.
Vous trouverez dans les dossiers `cli` et `gui` les deux versions du projet, qui contiennent un autre README avec des informations spécifiques à chaque version.

## Structure
Le projet est divisé en deux parties :
- cli : Le jeu avec une interface en ligne de commande basique
- gui : Le jeu avec une interface graphique implémentant CTkinter
- compiled_bin : Le jeu compilé en un seul fichier exécutable (recommandé pour exécuter simplement sur Windows)

Chaque partie source est composée de plusieurs fichiers :
- `main.py` : Le fichier principal, contenant le code principal du jeu
- `plate.py` : Le fichier contenant les fonctions de génération de plateau
- `utils.py` : Le fichier contenant les fonctions utilitaires
- `components/` : Le dossier contenant les composants graphiques (gui uniquement)

## Auteurs
- Pierre BIDET
- Anaëlle BOUSSIN

## Technologies
- Python
- CTkinter
- CtkTable
- PyInstaller

## Licence
Ce projet est sous license CC-BY-NC-SA 4.0.
Copyright (c) 2023 Veagle