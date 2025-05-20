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
    print('Mode 1 Joueur activé')
    bouton_1J.destroy()
    bouton_2J.destroy()

    bouton_terminal = tk.Button(fenetre, text="Terminal de commande", command=lancer_terminal, font=("Helvetica", 25))
    bouton_terminal.pack(pady=100)

    bouton_Interface = tk.Button(fenetre, text="Interface Graphique", command=lancer_interface, font=("Helvetica", 25))
    bouton_Interface.pack(pady=10)

    resultats_frame = tk.Frame(fenetre)
    resultats_frame.pack()

def joueurduo():
    print('Mode 2 Joueurs activé')
    bouton_1J.destroy()
    bouton_2J.destroy()
    
    bouton_Interface = tk.Button(fenetre, text="Interface Graphique", command=lambda: messagebox.showinfo("Information", "Mode solo activé."), font=("Helvetica", 25))
    bouton_Interface.pack(pady=150)

    resultats_frame = tk.Frame(fenetre)
    resultats_frame.pack()

# Interface Tkinter
fenetre = tk.Tk()
fenetre.title("Motus Mania")
fenetre.geometry("540x550")
fenetre.resizable(False, False)

titre = tk.Label(fenetre, text="Motus Mania", font=("Helvetica", 30))
titre.pack(pady=10)

sous_titre = tk.Label(fenetre, text="Trouvez le mot de 7 lettres", font=("Helvetica", 10))
sous_titre.pack(pady=10)


bouton_1J = tk.Button(fenetre, text="1 Joueur", command=joueursolo, font=("Helvetica", 25))
bouton_1J.pack(pady=100)

bouton_2J = tk.Button(fenetre, text="2 Joueurs", command=joueurduo, font=("Helvetica", 25))
bouton_2J.pack(pady=10)

resultats_frame = tk.Frame(fenetre)
resultats_frame.pack()

fenetre.mainloop()
