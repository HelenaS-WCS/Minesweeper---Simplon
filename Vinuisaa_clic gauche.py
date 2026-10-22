import pygame
import sys
import random
import os

pygame.init()
# matrice test
from Vinuisaa_matrices import generer_grille
grille = generer_grille()

# fenêtre de jeu
screen = pygame.display.set_mode((400,450))

# titre
pygame.display.set_caption("Minesweeper (mais en mieux ;) )")

# POLICES
# Fenêtre de départ
police_titre = pygame.font.SysFont("Arial", 42, bold=True)
police_texte = pygame.font.SysFont("Arial", 30)


#FPS
clock = pygame.time.Clock()
compteur_fps = 10

# tuiles
tuile_taille = 40
tuile_nbe = 10

# Cases cachées au début
cases_visibles = [[False for col in range(10)] for row in range(10)]

# COULEURS
# Fenêtre de départ
BLANC = (255, 255, 255)
NOIR = (40, 40, 40)
GRIS_CLAIR = (220, 220, 220)
GRIS_FONCE = (180, 180, 180)
BLEU_BOUTON = (52, 152, 219)
BLEU_HOVER = (41, 128, 185)

# Game over
ROUGE = (220,10,10)
ROUGE_FOND = (100,10,10)
ROUGE_BOUTON = (50, 5, 5)
ROUGE_HOVER = (150, 15, 15)

# Partie gagné
JAUNE = (250,200,80)
JAUNE_FOND = (145,100,10)
VERT_BOUTON = (125, 120, 10)
VERT_HOVER = (200,200, 15)

# 1ere couche
arriere_plan = (130,220,240)
tuile_c1 = (110,150,160)
tuile_c2 = (140,190,200)
border_c = (85,115,140)

# 2eme couche
sous_tuile_c1 = (220,250,240)
sous_tuile_c2 = (210,240,230)


# Définition du bouton "Démarrer" (x, y, largeur, hauteur)
bouton_rect = pygame.rect.Rect(400 // 2 - 125, 450 // 2 + 50, 250, 60)

# État initial du jeu
etat_jeu = "WINNER"

# FONCTIONS
# Bouton
# couleur survol bouton
def bouton(couleur,couleur_hover,texte):
    souris_pos = pygame.mouse.get_pos()
    if bouton_rect.collidepoint(souris_pos)==True:
        couleur_bouton = couleur_hover
    else:
        couleur_bouton = couleur

    # création du bouton
    pygame.draw.rect(screen,couleur_bouton,bouton_rect,border_radius=10)
    texte_bouton_3 = police_texte.render(texte,True,BLANC)
    texte_rect_3 = texte_bouton_3.get_rect(center=bouton_rect.center)
    screen.blit(texte_bouton_3,texte_rect_3)

########################## Partie pour la couche supérieure

# Montrer une case

def ouvre_case(ligne, colonne, clic_direct=True):
    global etat_jeu

    # Vérifier que la case est dans la grille
    if ligne < 0 or ligne >= 10 or colonne < 0 or colonne >= 10:
        return

    # Si c'est une mine
    if grille[ligne][colonne] == -1:
        if clic_direct:
            cases_visibles[ligne][colonne] = True
            etat_jeu = "GAME OVER"
        return
    
    # Si la case est déjà visible, arrêter
    if cases_visibles[ligne][colonne]:
        return

    # Montrez la case
    cases_visibles[ligne][colonne] = True

    # Si c'est un zéro, dévoiler les cases autour
    # Continuer uniquement si c'est un zéro
    if grille[ligne][colonne] == 0:
        for l in range(ligne - 1, ligne + 2):
            for c in range(colonne - 1, colonne + 2):
                ouvre_case(l, c, clic_direct=False)
                
########################## Fin de mon ajout

# Rejouer
#def rejouer():
    # il faut rendre global les variables pour pouvoir les reset
    # global variables
    

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit() 
            
        if (etat_jeu == "MENU" or etat_jeu == "GAME OVER" or etat_jeu == "WINNER") and event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                if bouton_rect.collidepoint(event.pos):
                    etat_jeu = "JEU"

########################### CLIC GAUCHE SUR UNE CASE
                    
        if etat_jeu == "JEU" and event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                x, y = event.pos

                if 0 <= x < 400 and 50 <= y < 450:
                    colonne = x // tuile_taille
                    ligne = (y - 50) // tuile_taille
                    ouvre_case(ligne, colonne)
                    
###################################################################

    # arrière plan
    screen.fill(arriere_plan)
    
    # MENU
    if etat_jeu == "MENU":
        # Titre
        titre_principal = police_titre.render("MINESWEEPER",True, NOIR)
        titre_rect = titre_principal.get_rect(center = (400//2,450//2-80))
        screen.blit(titre_principal,titre_rect)

        # bouton
        bouton(BLEU_BOUTON,BLEU_HOVER,"Démarrer")
        
    # JEU
    if etat_jeu == "JEU":

        # couche inférieure
        for row in range(tuile_nbe):
            for col in range(tuile_nbe):
                if (row + col)%2 == 0:
                    color = sous_tuile_c1
                else:
                    color = sous_tuile_c2
                x = col * tuile_taille
                y = row * tuile_taille + 50
                
                pygame.draw.rect(screen,color,(x,y,tuile_taille,tuile_taille))
                pygame.draw.rect(screen,border_c,(x,y,tuile_taille,tuile_taille),1)
                
        # couche supérieure
        for row in range(tuile_nbe):
                for col in range(tuile_nbe):
                    if not cases_visibles[row][col]:    ########### J'ai ajouter cette ligne pour le fonctionnement logique
                        if (row + col)%2 == 0:
                            color = tuile_c1
                        else:
                            color = tuile_c2

                        x = col * tuile_taille
                        y = row * tuile_taille + 50
                        pygame.draw.rect(screen,color,(x,y,tuile_taille,tuile_taille))
                        pygame.draw.rect(screen,border_c,(x,y,tuile_taille,tuile_taille),1)

    
    # GAME OVER
    if etat_jeu == "GAME OVER":
        
        # Arrière plan
        screen.fill(ROUGE_FOND)
        # Titre
        titre_go = police_titre.render("GAME OVER!",True, ROUGE)
        titre_go_rect = titre_go.get_rect(center = (400//2,450//2-80))
        screen.blit(titre_go,titre_go_rect)

        # bouton
        bouton(ROUGE_BOUTON,ROUGE_HOVER,"Rejouer")

        
    # WINNER
    if etat_jeu == "WINNER":
        
        # Arrière plan
        screen.fill(JAUNE_FOND)
        # Titre
        titre_go = police_titre.render("WINNER WINNER",True, JAUNE)
        titre_go_rect = titre_go.get_rect(center = (400//2,450//2-80))
        screen.blit(titre_go,titre_go_rect)
        titre_go = police_titre.render("CHICKEN DINNER!",True, JAUNE)
        titre_go_rect = titre_go.get_rect(center = (400//2,450//2-40))
        screen.blit(titre_go,titre_go_rect)

        # bouton
        bouton(VERT_BOUTON,VERT_HOVER,"Rejouer")
    
    pygame.display.update()
    clock.tick(compteur_fps)
