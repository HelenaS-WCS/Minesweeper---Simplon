# Minesweeper---Simplon
Python - Partie 2 - jeu video

Le but du jeu (Minesweeper) : Trouver les cases cachées sans mines et éviter les cases cachées contenant des mines. 

Règles :
- Le jeu se déroule sur une grille de 10 * 10 cases.
- Certaines cases contiennent des mines.
- D'autres cases contiennent des chiffres qui indiquent le nombre de mines à cotés.
- Les drapeaux permettent de marquer des cases suspectées de contenir une mine, avec un clic droit.

Contrôles : 
- Clic gauche de la souris : révèle une case.
- Clic droit de la souris : Pour poser ou retirer un drapeau.
- Boutons pour démarrer la partie de jeu et pour rejouer

Condition de victoire : révéler toutes les cases sans mines.

Condition de défaite : révéler une case avec minés.


Pour créer ce jeu, on s'est réparti avec des tâches définies pour chaque fonctionnalité : 

1/ Afficher une fenêtre avec une grille de cases
- Cases 10 x 10 : bande de 50 pixels en haut pour pouvoir afficher le nombre de balises dispos. 
- Couche supérieure 10x10 cases (40 pixels)
- Couche inférieure 10x10 cases (40 pixels)

2/ Créer une grille, dans un fichier Modules avec des Fonction
- Grille 10x10 avec 10 mines aléatoires + chiffres indiquant le nombre de mines autour de la case
- Compteur de mines dans les cases

3/ Détecter les clics gauche et droit.
- Clic gauche : dévoiler la case , suppression couche supérieure, dévoile couche inférieure. Attention : si 0 → dévoile toutes les cases autour et les premières cases numérotées incluses
- Clic droit : placer ou enlever une balise (mine suspectée) + compteur de balise qui diminue

4/ Dessiner les cases, les mines, les drapeaux et les chiffres. 
- Trouver les images
- - choisir format / couleurs des chiffres 

5/ Début et fin du jeu :
- petite présentation au début (optionnel) : Par exemple : l’objectif du jeu
- Fin : créer un évènement dans le cas où :
       - le joueur gagne
       - Le joueur perds (quand il clique sur une mine)
       - Proposer au joueur de relancer le jeu
