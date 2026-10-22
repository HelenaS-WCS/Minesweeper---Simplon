import pygame
import sys
import random
import os

pygame.init()
# matrice test
matrix = [[0,0,0,0,"X",0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,"X",0,0,0],
          [0,0,0,0,0,0,0,0,0,0],
          [0,0,0,"X",0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0,0]]


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

# COULEURS
# Fenêtre de départ
BLANC = (255, 255, 255)
NOIR = (40, 40, 40)
GRIS_CLAIR = (220, 220, 220)
GRIS_FONCE = (180, 180, 180)
BLEU_BOUTON = (52, 152, 219)
BLEU_HOVER = (41, 128, 185)

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
etat_jeu = "MENU"

# FONCTIONS

# Rejouer
#def rejouer():
    # il faut rendre global les variables pour pouvoir les reset
    # global variables
    

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit() 
            
        if etat_jeu == "MENU" and event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                if bouton_rect.collidepoint(event.pos):
                    etat_jeu = "JEU"       

    # arrière plan
    screen.fill(arriere_plan)
    
    if etat_jeu == "MENU":
        # Titre
        titre_principal = police_titre.render("MINESWEEPER",True, NOIR)
        titre_rect = titre_principal.get_rect(center = (400//2,450//2-80))
        screen.blit(titre_principal,titre_rect)
    
        # couleur survol bouton
        souris_pos = pygame.mouse.get_pos()
        if bouton_rect.collidepoint(souris_pos)==True:
            couleur_bouton = BLEU_HOVER
        else:
            couleur_bouton = BLEU_BOUTON
        
        # création du bouton
        pygame.draw.rect(screen,couleur_bouton,bouton_rect,border_radius=10)
        texte_bouton_1 = police_texte.render("Démarrer",True,BLANC)
        texte_rect = texte_bouton_1.get_rect(center=bouton_rect.center)
        screen.blit(texte_bouton_1,texte_rect)
            
    
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
                    if (row + col)%2 == 0:
                        color = tuile_c1
                    else:
                        color = tuile_c2
                    x = col * tuile_taille
                    y = row * tuile_taille + 50
                    pygame.draw.rect(screen,color,(x,y,tuile_taille,tuile_taille))
                    pygame.draw.rect(screen,border_c,(x,y,tuile_taille,tuile_taille),1)
    
    pygame.display.update()
    clock.tick(compteur_fps)
