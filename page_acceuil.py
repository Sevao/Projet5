import tkinter as tk
from tkinter import messagebox
from random import randint

# Interface Tkinter
fenetre = tk.Tk()
fenetre.title("Motus Mania")
fenetre.geometry("540x550")
fenetre.resizable(False, False)

titre = tk.Label(fenetre, text="Motus Mania", font=("Helvetica", 30))
titre.pack(pady=10)

sous_titre = tk.Label(fenetre, text="trouvez le mot de 7 lettres", font=("Helvetica", 10))
sous_titre.pack(pady=10)

resultats_frame = tk.Frame(fenetre)
resultats_frame.pack()

fenetre.mainloop()
