import tkinter as tk
from tkinter import messagebox
from random import randint

# Interface Tkinter
fenetre = tk.Tk()
fenetre.title("Le jeu du motus")
fenetre.geometry("540x550")
fenetre.resizable(False, False)

titre = tk.Label(fenetre, text="Devinez le mot de 7 lettres", font=("Helvetica", 16))
titre.pack(pady=10)

entree = tk.Entry(fenetre, font=("Helvetica", 16), justify='center')
entree.pack()

bouton_valider = tk.Button(fenetre, text="Valider", command=verifier_mot, font=("Helvetica", 12))
bouton_valider.pack(pady=10)

resultats_frame = tk.Frame(fenetre)
resultats_frame.pack()

bouton_rejouer = tk.Button(fenetre, text="Rejouer", command=rejouer, font=("Helvetica", 12, "bold"))

# Zone stats en bas
stats_label = tk.Label(fenetre, text="", font=("Helvetica", 10, "italic"))
stats_label.pack(pady=20)
maj_stats_affichage()

fenetre.mainloop()
