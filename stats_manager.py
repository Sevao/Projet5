import json
import os

stats_file = "stats.json"
stats_file_duo = "stats_duo.json"

def charger_stats(): #si un fichier statistique existe, celui-ci est récupéré
    if os.path.exists(stats_file):
        with open(stats_file, "r") as f:
            return json.load(f)
    else: # si aucun fichier statistique existe, création d'un nouveau
        return {
            "parties": 0,
            "victoires": 0,
            "total_tours_pour_gagner": 0
        }

def sauvegarder_stats(stats): # sauvegarde les statistiques d'une partie à l'autre
    with open(stats_file, "w") as f:
        json.dump(stats, f)

def afficher_stats_tk(tk_messagebox): #définition et affichage des statistiques du joueur
    stats = charger_stats()
    parties = stats["parties"]
    victoires = stats["victoires"]
    pourcentage = (victoires / parties * 100) if parties else 0
    moyenne = (stats["total_tours_pour_gagner"] / victoires) if victoires else 0

    tk_messagebox.showinfo("Statistiques",
        f"Parties jouées : {parties}\n"
        f"Victoires : {victoires}\n"
        f"Taux de réussite : {pourcentage:.1f}%\n"
        f"Nombre moyen de tours pour gagner : {moyenne:.1f}"
    )
    



def charger_stats_duo():
    if os.path.exists(stats_file_duo):
        with open(stats_file_duo, "r") as f:
            return json.load(f)
    else:
        return {
            "parties": 0,
            "victoires_joueur_1": 0,
            "victoires_joueur_2": 0
        }

def sauvegarder_stats_duo(stats):
    with open(stats_file_duo, "w") as f:
        json.dump(stats, f)

def calculer_affichage_stats_duo():
    stats = charger_stats_duo()
    parties = stats["parties"]
    v1 = stats["victoires_joueur_1"]
    v2 = stats["victoires_joueur_2"]
    p1 = (v1 / parties * 100) if parties else 0
    p2 = (v2 / parties * 100) if parties else 0

    return (
        f"🎮 Parties : {parties}    🟦 J1 : {v1} victoires ({p1:.1f}%)    🟩 J2 : {v2} victoires ({p2:.1f}%)"
    )

