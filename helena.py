import pygame
import sys
import random
import os

pygame.init()

# fenêtre de jeu
screen = pygame.display.set_mode((400,450))

# titre
pygame.display.set_caption("Minesweeper (mais en mieux ;) )")

#FPS
clock = pygame.time.Clock()
compteur_fps = 10

# tuiles
tuile_taille = 40
tuile_nbe = 10

# couleurs 
# 1ere couche
arriere_plan = (130,220,240)
tuile_c1 = (110,150,160)
tuile_c2 = (140,190,200)
border_c = (85,115,140)

# 2eme couche
sous_tuile_c1 = (220,250,240)
sous_tuile_c2 = (210,240,230)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()    

    # arrière plan
    screen.fill(arriere_plan)
    
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
