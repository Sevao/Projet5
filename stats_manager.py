import json
import os

STATS_FILE = "stats.json"

def charger_stats(): #si un fichier statistique existe, celui-ci est récupéré
    if os.path.exists(STATS_FILE):
        with open(STATS_FILE, "r") as f:
            return json.load(f)
    else: # si aucun fichier statistique existe, création d'un nouveau
        return {
            "parties": 0,
            "victoires": 0,
            "total_tours_pour_gagner": 0
        }

def sauvegarder_stats(stats): # sauvegarde les statistiques d'une partie à l'autre
    with open(STATS_FILE, "w") as f:
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
