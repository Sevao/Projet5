import tkinter as tk #import du module d'interface graphique
from tkinter import messagebox
from random import randint
from stats_manager import * #imort du fichier stats_manager 


def calculer_affichage_stats():#mise en place des différentes statistiques du joueur
	stats = charger_stats()
	parties = stats["parties"]
	victoires = stats["victoires"]
	if parties > 0 :
		pourcentage = (victoires / parties * 100)
	else : 
		pourcentage = 0
	moyenne = (stats["total_tours_pour_gagner"] / victoires) if victoires else 0

	texte = ( #prépare les statistiques allant être donné au joueur
		f"🎮 Parties : {parties}    ✅ Victoires : {victoires}    "
		f"📈 Taux : {pourcentage:.1f}%    ⏱️ Moyenne : {moyenne:.1f} tours"
	)
	return texte #pourquoi il y a des parenthèses ?

def maj_stats_affichage():
	stats_label.config(text=calculer_affichage_stats())

def rejouer():#permet au joueur de relancer une partie
	global mot_secret, tours
	tours = 0
	entree.delete(0, tk.END)
	for widget in resultats_frame.winfo_children():
		widget.destroy()
	mot_secret = mot_7[randint(0, len(mot_7) - 1)]
	bouton_rejouer.pack_forget()

def verifier_mot():
	global tours

	mot_joueur = entree.get().lower()
	if len(mot_joueur) != 7 or not mot_joueur.isalpha():
		messagebox.showerror("Erreur", "Le mot doit être composé de 7 lettres, sans chiffres ni caractère spéciaux.") #en cas d'erreur dans le nombre de lettres
		return #même effet qu'un break

	ligne_frame = tk.Frame(resultats_frame)
	ligne_frame.pack(pady=2)

	mot_temp = list(mot_secret)
	etats = [''] * 7 #création d'une liste de 7 éléments vides

	for i in range(7):
		if mot_joueur[i] == mot_secret[i]:#si la lettre est bien placé, l'état de i devient 'vert'
			etats[i] = 'vert'
			mot_temp[i] = None

	for i in range(7):
		if etats[i] == '' and mot_joueur[i] in mot_temp: #si la lettre est dans le mot mais mal placé, l'état devient jaune
			etats[i] = 'jaune'
			mot_temp[mot_temp.index(mot_joueur[i])] = None
		elif etats[i] == '':
			etats[i] = 'gris' #si la lettre n'est dans le mot ou est deja bien placée autre part san doublon, l'état devient gris

	for i in range(7): # définition des couleurs en hexadécimal
		couleur = {
			'vert': '#6aaa64',
			'jaune': '#c9b458',
			'gris': '#787c7e'
		}[etats[i]]

		lettre_label = tk.Label( #MEP
			ligne_frame,
			text=mot_joueur[i].upper(),
			font=("Helvetica", 16, "bold"),
			width=2,
			height=1,
			bg=couleur,
			fg="white",
			relief="raised",
			bd=2
		)
		lettre_label.pack(side="left", padx=2)

	stats = charger_stats()
	stats["parties"] += 1 #ajout d'une partie au compteur

	if mot_joueur == mot_secret: #si le joueur a trouvé le bon mot
		stats["victoires"] += 1
		stats["total_tours_pour_gagner"] += (tours + 1)
		sauvegarder_stats(stats)
		messagebox.showinfo("Gagné", f"Bravo ! Vous avez trouvé le mot : {mot_secret.upper()} 🎉")
		bouton_rejouer.pack(pady=10)
	else: #si ce n'est pas le bon mot
		tours += 1
		if tours >= max_tours:
			sauvegarder_stats(stats)
			messagebox.showinfo("Perdu", f"Dommage ! Le mot était : {mot_secret.upper()}")
			bouton_rejouer.pack(pady=10) #affiche le bouton rejouer

	maj_stats_affichage()
	entree.delete(0, tk.END)

def mode_interface():
	global mot_7, mot_secret, max_tours, tours 
	global entree, resultats_frame, bouton_rejouer, stats_label #variables communes a toutes les fonctions

	with open('liste_mots.txt', 'r') as fichier:
		mots = [ligne.strip() for ligne in fichier.readlines()]

	mot_7 = [mot for mot in mots if len(mot) == 7] #prend tous les mots de 7 lettres
	mot_secret = mot_7[randint(0, len(mot_7) - 1)] #prend un mot au hasard dans ceux de 7 lettres

	max_tours = 6 #si le joueur dépasse le nombre de tour, il perd la partie
	tours = 0

	
	# Interface Tkinter des lignes 115 a 128
	fenetre = tk.Tk()
	fenetre.title("Le jeu du motus")
	fenetre.geometry("540x550")
	fenetre.resizable(False, False)
	titre = tk.Label(fenetre, text="Devinez le mot de 7 lettres", font=("Helvetica", 16))
	titre.pack(pady=10)

	entree = tk.Entry(fenetre, font=("Linux Biolinum Keyboard O", 16), justify='center')
	entree.pack()
	bouton_valider = tk.Button(fenetre, text="Valider", command=verifier_mot, font=("Helvetica", 12))
	bouton_valider.pack(pady=10)

	resultats_frame = tk.Frame(fenetre)
	resultats_frame.pack()

    # bouton rejouer
	bouton_rejouer = tk.Button(fenetre, text="Rejouer", command=rejouer, font=("Helvetica", 12, "bold"))

	# Zone stats en bas
	stats_label = tk.Label(fenetre, text="", font=("Helvetica", 10, "italic"))
	stats_label.pack(pady=20)
	maj_stats_affichage()

	fenetre.mainloop()

# Test, pour vérifier la fonctionnalité du programme.
#mode_interface()
