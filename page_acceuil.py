import tkinter as tk
from tkinter import messagebox
from random import randint
from stats_manager import *
from interface import *
from terminal import *
from deux_joueurs import *

couleur_fond = "#ff9999"  # Rouge-rose clair

def lancer_terminal():
    fenetre.destroy()
    mode_terminal()

def lancer_interface(nbre_tours):
    mode_interface(nbre_tours, fenetre, accueil)

def quitter():
    if messagebox.askokcancel("Quitter", "Voulez-vous vraiment quitter ?"):
        fenetre.destroy()

def niveaux():
    affichage()
    tk.Button(fenetre, text="Mode Facile (10 tours de jeu)", command=lambda: lancer_interface(10), font=("Helvetica", 25), bg=couleur_fond).pack(pady=20)
    tk.Button(fenetre, text="Mode Normal (6 tours de jeu)", command=lambda: lancer_interface(6), font=("Helvetica", 25), bg=couleur_fond).pack(pady=50)
    tk.Button(fenetre, text="Mode Difficile (4 tours de jeu)", command=lambda: lancer_interface(4), font=("Helvetica", 25), bg=couleur_fond).pack(pady=10)
    tk.Button(fenetre, text="Retour", command=joueursolo, font=("Helvetica", 15), bg=couleur_fond).pack(pady=10)

def joueursolo():
    affichage()
    tk.Button(fenetre, text="Terminal de commande", command=lancer_terminal, font=("Helvetica", 25), bg=couleur_fond).pack(pady=60)
    tk.Button(fenetre, text="Interface Graphique", command=niveaux, font=("Helvetica", 25), bg=couleur_fond).pack(pady=55)
    tk.Button(fenetre, text="Retour", command=accueil, font=("Helvetica", 15), bg=couleur_fond).pack(pady=10)

def joueurduo():
    affichage()
    tk.Button(fenetre, text="Interface Graphique", command=lambda: mode_deux_joueurs(fenetre), font=("Helvetica", 25), bg=couleur_fond).pack(pady=150)
    tk.Button(fenetre, text="Retour", command=accueil, font=("Helvetica", 15), bg=couleur_fond).pack(pady=10)

def accueil():
    affichage()
    tk.Button(fenetre, text="1 Joueur", command=joueursolo, font=("Helvetica", 25), bg=couleur_fond).pack(pady=60)
    tk.Button(fenetre, text="2 Joueurs", command=joueurduo, font=("Helvetica", 25), bg=couleur_fond).pack(pady=55)
    tk.Button(fenetre, text="Quitter", command=quitter, font=("Helvetica", 15), bg=couleur_fond).pack(pady=10)

def affichage():
    for widget in fenetre.winfo_children():
        widget.destroy()
    fenetre.config(bg=couleur_fond)
    tk.Label(fenetre, text="Motus Mania", font=("Helvetica", 30), bg=couleur_fond).pack(pady=10)
    tk.Label(fenetre, text="Trouvez le mot de 7 lettres", font=("Helvetica", 10), bg=couleur_fond).pack(pady=10)

# Configuration de la fenêtre principale
fenetre = tk.Tk()
fenetre.title("Motus Mania")
fenetre.geometry("540x550")
fenetre.iconbitmap("motus.ico")

accueil()

fenetre.mainloop()
