import json
import os

stats_file = "stats.json"
stats_file_duo = "stats_duo.json"

# Charge les statistiques solo depuis le fichier, ou crée une structure vide si le fichier n'existe pas
def charger_stats():
    if os.path.exists(stats_file):
        with open(stats_file, "r") as f:
            return json.load(f)
    else:
        # Retourne un dictionnaire initialisé si aucun fichier statistique n'existe encore
        return {
            "parties": 0,
            "victoires": 0,
            "total_tours_pour_gagner": 0
        }

# Sauvegarde les statistiques solo dans un fichier JSON
def sauvegarder_stats(stats):
    with open(stats_file, "w") as f:
        json.dump(stats, f)

# Affiche les statistiques solo dans une boîte de dialogue Tkinter
def afficher_stats_tk(tk_messagebox):
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

# Charge les statistiques du mode duo depuis le fichier, ou crée une structure vide si le fichier n'existe pas
def charger_stats_duo():
    if os.path.exists(stats_file_duo):
        with open(stats_file_duo, "r") as f:
            return json.load(f)
    else:
        # Structure initiale pour le mode deux joueurs
        return {
            "parties": 0,
            "victoires_joueur_1": 0,
            "victoires_joueur_2": 0
        }

# Sauvegarde les statistiques duo dans un fichier JSON
def sauvegarder_stats_duo(stats):
    with open(stats_file_duo, "w") as f:
        json.dump(stats, f)

# Calcule une chaîne formatée affichant les statistiques du mode duo
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
