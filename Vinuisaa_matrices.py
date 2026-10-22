# Créer matrices : (Vinuisaa) → Fichier modules
# Objectif matrice 10x10 avec :
# 10 mines random + chiffres indiquant le nombre de mines autour de la case

import random

def creer_grille():
    """Création d'une matrice 10 x 10 remplies de zéros. J'aurai donc 100 cases au total."""
    grille = [[0 for colonne in range(10)] for ligne in range(10)]
    return grille


def placer_mines(grille):
    """place 10 mines dans des cases différentes. (-1 : mines)"""
    mines_placees = 0

    while mines_placees < 10:
        ligne = random.randint(0, 9)
        colonne = random.randint(0, 9)

        if grille[ligne][colonne] == 0:
            grille[ligne][colonne] = -1
            mines_placees += 1

    return grille


def compter_mines(grille, ligne, colonne):
    """compte les mines autour d'une case, sans sortir des limites de la grille."""
    mines = 0
    for l in range(max(0, ligne - 1), min(10, ligne + 2)):
        for c in range(max(0, colonne - 1), min(10, colonne + 2)):
            if grille[l][c] == -1:
                mines += 1
    return mines


def calculer_chiffres(grille):
    """remplace les zéros par les chiffres correspondants, tout en conservant les mines (-1)."""
    for ligne in range(10):
        for colonne in range(10):
            if grille[ligne][colonne] != -1:
                grille[ligne][colonne] = compter_mines(grille, ligne, colonne)
    return grille


def generer_grille():
    """Fonction finale : appelle les fonctions dans le bon ordre et renvoie la grille complète."""
    grille = creer_grille()
    placer_mines(grille)
    calculer_chiffres(grille)
    return grille
