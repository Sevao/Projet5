#importation des modules
import tkinter as tk
from random import choice
from random import randint
from stats_manager import *

# Variables globales
mot_secret = ""
mot_7 = []
joueur = 1
temps = 15
timer_id = None
stats_label_duo = None

def afficher_resultat(mot):
    ligne = tk.Frame(resultats)
    ligne.pack(pady=2)

    etats = ['gris'] * 7
    temp = list(mot_secret)

    for i in range(7):
        if mot[i] == mot_secret[i]:
            etats[i] = 'vert'
            temp[i] = None

    for i in range(7):
        if etats[i] == 'gris' and mot[i] in temp:
            etats[i] = 'jaune'
            temp[temp.index(mot[i])] = None

    couleurs = {'vert': 'green', 'jaune': 'orange', 'gris': 'gray'}

    for i in range(7):
        tk.Label(ligne, text=mot[i].upper(), bg=couleurs[etats[i]], fg='white',
                 font=('Arial', 14), width=2).pack(side='left', padx=1)

def valider():
    global joueur
    mot = entree.get().lower()

    if len(mot) != 7 or not mot.isalpha():
        message.config(text="Mot invalide. Essayez encore.", fg='red')
        entree.delete(0, tk.END)
        return

    arreter_timer()
    afficher_resultat(mot)

    if mot == mot_secret:
        message.config(text=f"Joueur {joueur} a gagné !", fg='green')

        # Mise à jour des statistiques
        stats = charger_stats_duo()
        stats["parties"] += 1
        if joueur == 1:
            stats["victoires_joueur_1"] += 1
        else:
            stats["victoires_joueur_2"] += 1
        sauvegarder_stats_duo(stats)
        maj_stats_affichage_duo()
        return

    joueur = 2 if joueur == 1 else 1
    label_joueur.config(text=f"Joueur {joueur}")
    changer_couleur_fond()
    entree.delete(0, tk.END)
    lancer_timer()

def lancer_timer():
    global temps, timer_id
    temps = 15

    def compte():
        global temps, timer_id
        temps -= 1
        label_timer.config(text=f"Temps restant : {temps}s")
        if temps <= 0:
            message.config(text=f"Temps écoulé pour le joueur {joueur}", fg='blue')
            changer_joueur()
        else:
            timer_id = fenetre.after(1000, compte)

    timer_id = fenetre.after(1000, compte)

def changer_joueur():
    global joueur
    joueur = 2 if joueur == 1 else 1
    label_joueur.config(text=f"Joueur {joueur}")
    changer_couleur_fond()
    entree.delete(0, tk.END)
    lancer_timer()

def arreter_timer():
    global timer_id
    if timer_id:
        fenetre.after_cancel(timer_id)

def changer_couleur_fond():
    if joueur == 1:
        fenetre.config(bg='#add8e6')  # bleu clair
    else:
        fenetre.config(bg='#90ee90')  # vert clair

def nouvelle_partie():
    global mot_secret, joueur
    arreter_timer()
    mot_secret = choice(mot_7)
    joueur = 1
    label_joueur.config(text="Joueur 1")
    entree.delete(0, tk.END)
    for widget in resultats.winfo_children():
        widget.destroy()
    message.config(text="")
    changer_couleur_fond()
    lancer_timer()

def maj_stats_affichage_duo():
    try:
        if stats_label_duo and stats_label_duo.winfo_exists():
            stats_label_duo.config(text=calculer_affichage_stats_duo())
    except:
        pass

def mode_deux_joueurs(f):
    global fenetre, mot_7, label_joueur, label_timer, entree, resultats, message, stats_label_duo
    fenetre = f

    with open("liste_mots.txt", "r") as file:
        mot_7 = [mot.strip().lower() for mot in file if len(mot.strip()) == 7]

    for widget in fenetre.winfo_children():
        widget.destroy()

    label_joueur = tk.Label(fenetre, text="Joueur 1", font=("Arial", 16))
    label_joueur.pack(pady=10)

    label_timer = tk.Label(fenetre, text="Temps restant : 15s", font=("Arial", 12))
    label_timer.pack()

    entree = tk.Entry(fenetre, font=("Arial", 16), justify="center")
    entree.pack(pady=10)
    entree.bind("<Return>", lambda event: valider())

    btn_valider = tk.Button(fenetre, text="Valider", font=("Arial", 12), command=valider)
    btn_valider.pack(pady=5)

    resultats = tk.Frame(fenetre)
    resultats.pack(pady=10)

    message = tk.Label(fenetre, text="", font=("Arial", 12))
    message.pack()

    btn_rejouer = tk.Button(fenetre, text="Rejouer", font=("Arial", 12), command=nouvelle_partie)
    btn_rejouer.pack(pady=10)

    stats_label_duo = tk.Label(fenetre, text="", font=("Arial", 10, "italic"))
    stats_label_duo.pack(pady=10)
    maj_stats_affichage_duo()

    changer_couleur_fond()
    nouvelle_partie()
