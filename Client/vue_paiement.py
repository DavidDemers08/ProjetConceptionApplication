import tkinter as tk
from tkinter import ttk

import Utils.utils



class VuePaiement(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.controleur = None
        self.liste_module = []
        ###test pour remplir liste module
        self.liste_module.append(("nom module 1", "42.45", "2001/9/11"))
        self.liste_module.append(("nom module 2", "4s2.45", "2001/91/11"))
        self.liste_module.append(("nom module 3", "42.4a5", "20011/9/11"))
        self.remplir_vue()
        self.parent = parent


    def set_controleur(self, controleur):
        self.controleur = controleur

    def vider_frame(self):
        for widget in self.winfo_children():
            widget.destroy()

    def remplir_vue(self):
        self.heading = ttk.Label(self, text='Paiement', style='Heading.TLabel')
        self.heading.grid(column=3, row=0, columnspan=2, pady=5, sticky=tk.N)
        self.module = ttk.Label(self, text="Module")
        self.module.grid(column=0, row=1, sticky=tk.W, padx=50)
        self.prix = ttk.Label(self, text="Prix")
        self.prix.grid(column=3, row=1, sticky=tk.W, padx=50)
        self.exp_date= ttk.Label(self, text="Date d'expiration")
        self.exp_date.grid(column=5, row=1, sticky=tk.W, padx=50)
        self.remplir_grid_module()

    def remplir_grid_module(self):
        compteur_row = 2
        for module in self.liste_module:
            nom_module = ttk.Label(self, text=module[0])
            nom_module.grid(column=0, row=compteur_row,  padx=50, sticky=tk.N)
            prix_module = ttk.Label(self, text=module[1])
            prix_module.grid(column=3, row=compteur_row, padx=50, sticky=tk.N)
            date_module = ttk.Label(self, text=module[2])
            date_module.grid(column=5, row=compteur_row, padx=50, sticky=tk.N)
            compteur_row += 1
