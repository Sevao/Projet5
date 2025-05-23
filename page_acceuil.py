import tkinter as tk
from tkinter import messagebox
from random import randint
from stats_manager import *
from interface import *
from terminal import *


# Lance le jeu en version terminal après avoir fermé la fenêtre Tkinter
def lancer_terminal():
	fenetre.destroy()  # Ferme la fenêtre Tkinter
	mode_terminal()    # Lance le jeu en mode terminal


# Lance le jeu en version interface graphique après avoir fermé la fenêtre Tkinter
def lancer_interface(nbre_tours):
    mode_interface(nbre_tours, fenetre, accueil)

	
	
# Menu pour choisir le niveau de difficulté (facile, normal, difficile)
def niveaux():
	
	affichage()
	
	bouton_facile = tk.Button(fenetre, text="Mode Facile (10 tours de jeu)", command=lambda: messagebox.showinfo("Information", "Mode facile bientôt disponible."), font=("Helvetica", 25))
	bouton_facile.pack(pady=20)
	
	bouton_normal = tk.Button(fenetre, text="Mode Normal (6 tours de jeu)", command=lambda : lancer_interface(6), font=("Helvetica", 25))
	bouton_normal.pack(pady=50)
	
	bouton_difficile = tk.Button(fenetre, text="Mode Difficile (4 tours de jeu)", command=lambda : lancer_interface(4), font=("Helvetica", 25))
	bouton_difficile.pack(pady=10)
	
	
	bouton_retour = tk.Button(fenetre, text="Retour", command=joueursolo, font=("Helvetica", 15))
	bouton_retour.pack(pady=10)


# Menu pour choisir entre le jeu en terminal ou en interface graphique
def joueursolo():
	
	affichage()
		
	bouton_terminal = tk.Button(fenetre, text="Terminal de commande", command=lancer_terminal, font=("Helvetica", 25))
	bouton_terminal.pack(pady=60)

	bouton_interface = tk.Button(fenetre, text="Interface Graphique", command=niveaux, font=("Helvetica", 25))
	bouton_interface.pack(pady=55)
	
	bouton_retour = tk.Button(fenetre, text="Retour", command=accueil, font=("Helvetica", 15))
	bouton_retour.pack(pady=10)


# Menu pour le mode deux joueurs
def joueurduo():
	
	affichage()
	
	bouton_interface = tk.Button(fenetre, text="Interface Graphique", command=lambda: messagebox.showinfo("Information", "Mode 2 joueurs bientôt disponible."), font=("Helvetica", 25))
	bouton_interface.pack(pady=150)
	
	bouton_retour = tk.Button(fenetre, text="Retour", command=accueil, font=("Helvetica", 15))
	bouton_retour.pack(pady=10)



# Écran d'accueil principal avec les options 1 ou 2 joueurs
def accueil():
	
	affichage()

	bouton_1J = tk.Button(fenetre, text="1 Joueur", command=joueursolo, font=("Helvetica", 25))
	bouton_1J.pack(pady=60)

	bouton_2J = tk.Button(fenetre, text="2 Joueurs", command=joueurduo, font=("Helvetica", 25))
	bouton_2J.pack(pady=55)
	
	bouton_retour = tk.Button(fenetre, text="Quitter", command=fenetre.destroy, font=("Helvetica", 15))
	bouton_retour.pack(pady=10)
	
	
	
# Fonction utilisée pour réinitialiser l'interface (efface tous les widgets de la fenêtre, et en redefinit de nouveaux)
def affichage():
	for widget in fenetre.winfo_children():
		widget.destroy()
		
	titre = tk.Label(fenetre, text="Motus Mania", font=("Helvetica", 30))
	titre.pack(pady=10)

	sous_titre = tk.Label(fenetre, text="Trouvez le mot de 7 lettres", font=("Helvetica", 10))
	sous_titre.pack(pady=10)
	

# Configuration de la fenêtre principale Tkinter
fenetre = tk.Tk()
fenetre.title("Motus Mania")
fenetre.geometry("540x550")
fenetre.resizable(False, False)

accueil()

fenetre.mainloop()
