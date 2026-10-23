import pygame
import sys
import random
import os
from matrices import generer_grille

pygame.init()

# fenêtre de jeu
screen = pygame.display.set_mode((400,450))

# titre
pygame.display.set_caption("Minesweeper (mais en mieux ;) )")

# POLICES
# Fenêtre de départ
police_titre = pygame.font.SysFont("Arial", 42, bold=True)
police_texte = pygame.font.SysFont("Arial", 30)
police_compteur = pygame.font.SysFont("Arial", 30, bold=True)

#FPS
clock = pygame.time.Clock()
compteur_fps = 10

# tuiles
tuile_taille = 40
tuile_nbe = 10

# Cases cachées au début
cases_visibles = [[False for col in range(10)] for row in range(10)]

## BALISES
# nombre de balises restantes                                #HELENA
nombre_flag = 10
# matrice drapeau
drapeaux = [[False for col in range(10)] for row in range(10)]

## COULEURS
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
etat_jeu = "MENU"

### IMAGES
flag = pygame.image.load('images/flag.png')
flag = pygame.transform.scale(flag, (40, 40))
explosion = pygame.image.load('images/explosion.png')
explosion = pygame.transform.scale(explosion, (40, 40))
mine = pygame.image.load('images/mine.png')
mine = pygame.transform.scale(mine, (40, 40))

# FONCTIONS
# Est-ce qu'on a gagné?
def did_you_win():
    global etat_jeu, temps_victoire
    for row in range(tuile_nbe):
        for col in range(tuile_nbe):
            if grille[row][col] != -1 and not cases_visibles[row][col]:
                return  
                
    etat_jeu = "WINNING"
    temps_victoire = pygame.time.get_ticks()
    
# Montrer une case
def ouvre_case(ligne, colonne, clic_direct=True):
    global etat_jeu, temps_defaite

    # Vérifier que la case est dans la grille
    if ligne < 0 or ligne >= 10 or colonne < 0 or colonne >= 10:
        return

    # Si c'est une mine
    if grille[ligne][colonne] == -1:
        if clic_direct:
            cases_visibles[ligne][colonne] = True
            etat_jeu = "LOSING"
            temps_defaite = pygame.time.get_ticks()
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
                
# rappatrier drapeaux
def rappat_drapeaux():

    global nombre_flag
    global drapeaux
    
    for ligne in range(10):
        for colonne in range(10):
            if drapeaux[ligne][colonne]==True and cases_visibles[ligne][colonne] == True:
                drapeaux[ligne][colonne]=False
                nombre_flag += 1
                
# Bouton
def bouton(couleur,couleur_hover,texte):
    souris_pos = pygame.mouse.get_pos()
    if bouton_rect.collidepoint(souris_pos)==True:
        couleur_bouton = couleur_hover
    else:
        couleur_bouton = couleur
        
    pygame.draw.rect(screen,couleur_bouton,bouton_rect,border_radius=10)
    texte_bouton_3 = police_texte.render(texte,True,BLANC)
    texte_rect_3 = texte_bouton_3.get_rect(center=bouton_rect.center)
    screen.blit(texte_bouton_3,texte_rect_3)

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
    

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit() 
            
        if (etat_jeu == "MENU" or etat_jeu == "GAME OVER" or etat_jeu == "WINNER") and event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                if bouton_rect.collidepoint(event.pos):
                    if etat_jeu == "MENU":
                        etat_jeu = "JEU"
                    else:
                        rejouer()

                    temps_depart = pygame.time.get_ticks()       

        elif etat_jeu == "JEU" and event.type == pygame.MOUSEBUTTONDOWN:     
            if event.button == 1:
                x, y = event.pos

                if 0 <= x < 400 and 50 <= y < 450:
                    colonne = x // tuile_taille
                    ligne = (y - 50) // tuile_taille
                    ouvre_case(ligne, colonne)
                    
            if event.button == 3:                       
                x,y = event.pos
                if 0 <= x < 400 and 50 <= y < 450:
                    colonne = x // tuile_taille
                    ligne = (y - 50) // tuile_taille
                    if cases_visibles[ligne][colonne] == False:
                        if drapeaux[ligne][colonne]==False and nombre_flag > 0:
                            drapeaux[ligne][colonne] = True
                            nombre_flag -= 1
                        elif drapeaux[ligne][colonne]==True:
                            drapeaux[ligne][colonne] = False
                            nombre_flag += 1 
                    elif cases_visibles[ligne][colonne] == True and drapeaux[ligne][colonne]==True:
                        drapeaux[ligne][colonne] = False
                        nombre_flag += 1 
                        
    # 1 seconde avant de passer à l'état jeu = "WINNER", 
    if etat_jeu == "WINNING":
        if pygame.time.get_ticks() - temps_victoire >= 1000:
            etat_jeu = "WINNER"

    # 1 seconde avant de passer à l'état jeu = "GAME OVER", 
    if etat_jeu == "LOSING":
        if pygame.time.get_ticks() - temps_defaite >= 1000:
            etat_jeu = "GAME OVER"
                    
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
        
        temps_actuel = pygame.time.get_ticks()
        
        # image flag et mine
        screen.blit(flag,(5,5))
        screen.blit(mine,(180,5))
        
        # nombre de flags
        compteur_flags = police_compteur.render(f" : {nombre_flag}",True, ROUGE)
        screen.blit(compteur_flags,(50,10))
        
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
                    x = col * tuile_taille
                    y = row * tuile_taille + 50

                    if not cases_visibles[row][col]:
                        if (row + col)%2 == 0:
                            color = tuile_c1
                        else:
                            color = tuile_c2
                        pygame.draw.rect(screen,color,(x,y,tuile_taille,tuile_taille))
                        pygame.draw.rect(screen,border_c,(x,y,tuile_taille,tuile_taille),1)

                    elif grille[row][col] > 0:
                        texte_case = police_texte.render(str(grille[row][col]), True, NOIR)
                        texte_rect = texte_case.get_rect(
                            center=(x + tuile_taille // 2, y + tuile_taille // 2)
                            )
                        screen.blit(texte_case, texte_rect)
                        
                    elif grille[row][col] == -1:
                        screen.blit(explosion, (x,y))
                        
        # couche de drapeaux                                
        for row in range(10):
            for col in range(10):
                if drapeaux[row][col] == True:
                    x = col * tuile_taille
                    y = row * tuile_taille
                    screen.blit(flag,(x,y+50))

        # rappatriement drapeaux
        rappat_drapeaux()
        
        # vérification si on a gagné            
        did_you_win()
        
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
