# Projet5  (projet de NSI)

# Projet 10 : Motus
Description du mini projet
Le jeu du Motus consiste à retrouver un mot de 7 lettres en 6 coups maximum.

Le programme choisit au hasard un mot de 7 lettres, le joueur peut alors proposer 6 combinaisons de 7 lettres pour retrouver le mot choisi par le programme.

Un exemple : https://www.funmeninges.com/mastermots.html

# Cahier des charges
- Le programme choisit au hasard un mot de 7 lettres dans la liste donnée ci-dessous en téléchargment,

- Le programme enregistre le choix du joueur (en minuscules, sans accents)

- Le programme affiche la réponse de manière suivante :

      les lettres bien placées sont écrites en MAJUSCULE

      les lettres mal placées sont écrites en minuscules

      les autres sont remplacée par des points.

- Si le joueur trouve le bon mot avant son 7éme essai, le programme le déclare victorieux, sinon il affiche le mot choisi.

Votre programme informera l'utilisateur du résultat de sa recherche.

11_liste.de.mots.francais.frgut.txt [txt]



# Palier 4 : Une fois le palier 3 franchi
- Gestion des scores (avec un fichier texte).

- Gestion du multi utilisateurs : 2 joueurs humains s'affrontent sur plusieurs parties, la main passe si le candidat devant jouer :

      ne trouve pas le mot au bout du nombre de tentatives imparties, c'est-à-dire quand la grille des mots est complète (6 essais au début de chaque mot) ;

      propose un mot non valide ;

      n'écrit pas correctement le mot proposé ;

      dépasse le temps imparti pour proposer un mot (8 secondes).
