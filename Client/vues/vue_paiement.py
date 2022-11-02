import tkinter as tk
from tkinter import ttk
from Utils.Table import Table

import Utils.utils



class VuePaiement(ttk.Frame):
    def __init__(self, parent,controleur):
        super().__init__(parent)
        self.controleur = controleur
        self.liste_module = []
        self.parent = parent
        ###test pour remplir liste module
        self.liste_module.append(["nom module 1", "42.45", "2001/9/11"])
        self.liste_module.append(["nom module 2", "412.45", "2001/91/11"])
        self.liste_module.append(["nom module 3", "421.45", "20011/9/11"])
        self.remplir_vue()


        print(self.controleur.get_module())

    def set_controleur(self, controleur):
        self.controleur = controleur

    def vider_frame(self):
        for widget in self.winfo_children():
            widget.destroy()

    def remplir_vue(self):
        self.heading = ttk.Label(self, text='Paiement', style='Heading.TLabel')
        self.heading.grid(column=0, row=0, columnspan=2, pady=5, sticky=tk.N)
        self.module = ttk.Label(self, text="Module")
        self.module.grid(column=0, row=1, sticky=tk.W, padx=50)
        self.prix = ttk.Label(self, text="Prix")
        self.prix.grid(column=1, row=1, sticky=tk.W, padx=50)
        self.exp_date= ttk.Label(self, text="Date d'expiration")
        self.exp_date.grid(column=2, row=1, sticky=tk.W, padx=50)
        self.remplir_grid_module()

    def remplir_grid_module(self):

        table = Table(vue=self, lines_array=self.liste_module,start_row=2,start_column=0,padx=50, modifiable_rows=False)
        table.create()
