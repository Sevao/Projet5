import tkinter as tk
from tkinter import messagebox
from random import randint
from stats_manager import *
from interface import *
from terminal import *


def lancer_terminal():
	fenetre.destroy()  # Ferme la fenêtre Tkinter
	mode_terminal()    # Lance le jeu en mode terminal
	
def lancer_interface() :
	fenetre.destroy()  # Ferme la fenêtre Tkinter
	mode_interface()   # Lance le jeu en mode terminal
	
	
	
def joueursolo():
	
	affichage()
		
	bouton_terminal = tk.Button(fenetre, text="Terminal de commande", command=lancer_terminal, font=("Helvetica", 25))
	bouton_terminal.pack(pady=60)

	bouton_interface = tk.Button(fenetre, text="Interface Graphique", command=lancer_interface, font=("Helvetica", 25))
	bouton_interface.pack(pady=55)
	
	bouton_retour = tk.Button(fenetre, text="Retour", command=accueil, font=("Helvetica", 15))
	bouton_retour.pack(pady=10)



def joueurduo():
	
	affichage()
	
	bouton_interface = tk.Button(fenetre, text="Interface Graphique", command=lambda: messagebox.showinfo("Information", "Mode 2 joueurs bientôt disponible."), font=("Helvetica", 25))
	bouton_interface.pack(pady=150)
	
	bouton_retour = tk.Button(fenetre, text="Retour", command=accueil, font=("Helvetica", 15))
	bouton_retour.pack(pady=10)




def accueil():
	
	affichage()

	bouton_1J = tk.Button(fenetre, text="1 Joueur", command=joueursolo, font=("Helvetica", 25))
	bouton_1J.pack(pady=100)

	bouton_2J = tk.Button(fenetre, text="2 Joueurs", command=joueurduo, font=("Helvetica", 25))
	bouton_2J.pack(pady=10)
	
	

def affichage():
	for widget in fenetre.winfo_children():
		widget.destroy()
		
	titre = tk.Label(fenetre, text="Motus Mania", font=("Helvetica", 30))
	titre.pack(pady=10)

	sous_titre = tk.Label(fenetre, text="Trouvez le mot de 7 lettres", font=("Helvetica", 10))
	sous_titre.pack(pady=10)
	
# Interface Tkinter
fenetre = tk.Tk()
fenetre.title("Motus Mania")
fenetre.geometry("540x550")
fenetre.resizable(False, False)

accueil()

fenetre.mainloop()
