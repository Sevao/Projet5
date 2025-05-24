import tkinter as tk
from tkinter import messagebox
from random import randint
from stats_manager import *

def calculer_affichage_stats():
	stats = charger_stats()
	parties = stats["parties"]
	victoires = stats["victoires"]
	pourcentage = (victoires / parties * 100) if parties > 0 else 0
	moyenne = (stats["total_tours_pour_gagner"] / victoires) if victoires else 0

	return (
		f"🎮 Parties : {parties}    ✅ Victoires : {victoires}    "
		f"📈 Taux : {pourcentage:.1f}%    ⏱️ Moyenne : {moyenne:.1f} tours"
	)

def maj_stats_affichage():
	try:
		if stats_label.winfo_exists():
			stats_label.config(text=calculer_affichage_stats())
	except tk.TclError:
		pass # évite l’erreur si le widget a été détruit

def rejouer(fenetre, callback_accueil):
	mode_interface(max_tours, fenetre, callback_accueil)

def verifier_mot(fenetre, callback_accueil):
	global tours

	mot_joueur = entree.get().lower()
	if len(mot_joueur) != 7 or not mot_joueur.isalpha():
		messagebox.showerror("Erreur", "Le mot doit être composé de 7 lettres.")
		return

	ligne_frame = tk.Frame(resultats_frame)
	ligne_frame.pack(pady=2)

	mot_temp = list(mot_secret)
	etats = [''] * 7

	for i in range(7):
		if mot_joueur[i] == mot_secret[i]:
			etats[i] = 'vert'
			mot_temp[i] = None

	for i in range(7):
		if etats[i] == '' and mot_joueur[i] in mot_temp:
			etats[i] = 'jaune'
			mot_temp[mot_temp.index(mot_joueur[i])] = None
		elif etats[i] == '':
			etats[i] = 'gris'

	for i in range(7):
		couleur = {'vert': '#6aaa64', 'jaune': '#c9b458', 'gris': '#787c7e'}[etats[i]]
		lettre_label = tk.Label(
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
	stats["parties"] += 1

	if mot_joueur == mot_secret:
		stats["victoires"] += 1
		stats["total_tours_pour_gagner"] += (tours + 1)
		sauvegarder_stats(stats)
		messagebox.showinfo("Gagné", f"Bravo ! Vous avez trouvé le mot : {mot_secret.upper()} 🎉")
		bouton_rejouer.pack(pady=10)
		fin_de_partie(fenetre, callback_accueil)
	else:
		tours += 1
		if tours >= max_tours:
			sauvegarder_stats(stats)
			messagebox.showinfo("Perdu", f"Dommage ! Le mot était : {mot_secret.upper()}")
			bouton_rejouer.pack(pady=10)
			fin_de_partie(fenetre, callback_accueil)

	maj_stats_affichage()
	
	if entree.winfo_exists():
		entree.delete(0, tk.END)


def fin_de_partie(fenetre, callback_accueil):
	for widget in fenetre.winfo_children():
		widget.destroy()

	tk.Label(fenetre, text="Fin de la partie", font=("Helvetica", 20, "bold")).pack(pady=20)
	tk.Button(fenetre, text="Rejouer", command=lambda: rejouer(fenetre, callback_accueil), font=("Helvetica", 25)).pack(pady=20)

	if callback_accueil:
		tk.Button(fenetre, text="Accueil", command=lambda: callback_accueil(), font=("Helvetica", 25)).pack(pady=20)

	tk.Button(fenetre, text="Quitter", command=fenetre.destroy, font=("Helvetica", 15)).pack(pady=20)

def mode_interface(nbre_tours, fenetre, callback_accueil=None):
	global mot_7, mot_secret, max_tours, tours
	global entree, resultats_frame, bouton_rejouer, stats_label

	try:
		with open('liste_mots.txt', 'r') as fichier:
			mots = [ligne.strip() for ligne in fichier.readlines()]
	except FileNotFoundError:
		messagebox.showerror("Erreur", "Fichier 'liste_mots.txt' introuvable.")
		return

	mot_7 = [mot for mot in mots if len(mot) == 7]
	mot_secret = mot_7[randint(0, len(mot_7) - 1)]

	max_tours = nbre_tours
	tours = 0

	for widget in fenetre.winfo_children():
		widget.destroy()

	tk.Label(fenetre, text="Devinez le mot de 7 lettres", font=("Helvetica", 16)).pack(pady=10)

	entree = tk.Entry(fenetre, font=("Helvetica", 16), justify='center')
	entree.pack()
	entree.focus_set()
	
	entree.bind("<Return>", lambda event: verifier_mot(fenetre, callback_accueil))
	

	tk.Button(fenetre, text="Valider", command=lambda: verifier_mot(fenetre, callback_accueil), font=("Helvetica", 12)).pack(pady=10)

	resultats_frame = tk.Frame(fenetre)
	resultats_frame.pack()

	bouton_rejouer = tk.Button(fenetre, text="Rejouer", command=lambda: rejouer(fenetre, callback_accueil), font=("Helvetica", 12, "bold"))

	stats_label = tk.Label(fenetre, text="", font=("Helvetica", 10, "italic"))
	stats_label.pack(pady=20)
	maj_stats_affichage()
