from random import *

def mode_terminal() :
	
	fichier = open('liste_mots.txt', 'r')
	mots = fichier.readlines()

	mot_7 = [elt.strip() for elt in mots if len(elt.strip()) == 7]  # Sélection des mots de 7 lettres


	i_mot = randint(0, len(mot_7) - 1)
	mot = mot_7[i_mot]  # Choix du mot de la partie

	#print(mot)  # Test, pour vérifier la fonctionnalité du programme. À enlever pour jouer

	max_tours = 6
	tours = 0
	condition = True

	# Boucle de jeu : donner un nombre de tours au joueur pour trouver le mot
	while condition == True:
		print("Tour n°{}/{}".format((tours + 1), max_tours))
			
		mot_joueur = input("Entrez un mot de 7 lettres : ")
		# Vérifier que le mot du joueur est bien de 7 lettres et que ce sont des lettres uniquement
		while len(mot_joueur) != 7 or not mot_joueur.isalpha() or not mot_joueur.islower(): # .isalpha et .islower pour verifier que c'est bien des lettres (str) et en minuscules
			print("Le mot doit être composé de 7 lettres, sans chiffres ni caractère spéciaux.")
			mot_joueur = input("Entrez un mot de 7 lettres : ")

		reponse = []

		for i in range(len(mot_joueur)):
			if mot_joueur[i] == mot[i]:
				reponse.append(mot_joueur[i].upper())  # Lettre correcte et bien placée
			elif mot_joueur[i] in mot:
				reponse.append(mot_joueur[i])  # Lettre correcte mais mal placée
			else:
				reponse.append('.')  # Lettre incorrecte

		print("Réponse : {}".format(reponse))

		if mot_joueur == mot:  # Si le mot a été trouvé, arrêter la partie et annoncer la victoire
			print("Félicitations, vous avez gagné et trouvé le mot en {} tours !".format((tours + 1)))
			condition = False

		tours += 1
		if tours >= max_tours :
			condition = False
			

	if tours == max_tours and mot_joueur != mot:  # Si le mot n'a pas été trouvé, arrêter la partie et annoncer la défaite, puis donner le mot qu'il fallait trouver
		print("Dommage, vous avez perdu. Le mot était : {}".format(mot))
