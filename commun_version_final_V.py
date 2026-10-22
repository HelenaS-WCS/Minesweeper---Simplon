# La partie à changer pour réinitialisation des drapeaux (Vinuisaa)

# Rejouer
def rejouer():
    # il faut rendre global les variables pour pouvoir les reset
    global grille, cases_visibles, drapeaux, nombre_flag, etat_jeu

    # Créer une nouvelle grille avec de nouvelles mines
    grille = generer_grille()

    # Cacher toutes les cases
    cases_visibles = [[False for col in range(10)] for row in range(10)]

    # Enlever tous les drapeaux
    drapeaux = [[False for col in range(10)] for row in range(10)]

    # Réinitialiser le compteur de drapeaux
    nombre_flag = 10

    # Revenir à l'écran de jeu
    etat_jeu = "JEU"
