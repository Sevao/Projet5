import tkinter as tk
from tkinter import messagebox
from random import randint

# Interface Tkinter
fenetre = tk.Tk()
fenetre.title("Le jeu du motus")
fenetre.geometry("540x550")
fenetre.resizable(False, False)

titre = tk.Label(fenetre, text="Motus Mania", font=("Helvetica", 16))
titre.pack(pady=10)



resultats_frame = tk.Frame(fenetre)
resultats_frame.pack()

fenetre.mainloop()
