from traceback import print_exc

from Client.AbstractClasses.Module import Module
from Client.AbstractClasses.Vue import Vue

import tkinter as tk
from tkinter import ttk

import Utils.utils


class ModuleInventaire(Module):

    def __init__(self, controleur, master_frame):
        super().__init__(controleur, master_frame)

    def set_vue(self):
        return ModuleInventaire.VueInventaire(self, self.master_frame, row=0, column=0, padx=10, pady=10)

    class VueInventaire(Vue):
        def __init__(self, parent, master_frame, row: int, column: int, padx: int, pady: int):
            super().__init__(parent, master_frame, row, column, padx, pady)

        def remplir_vue(self):
            self.label_titre = ttk.Label(self.master_frame, text='Gestion Inventaire')
            self.label_titre.grid(row=1, column=1, columnspan=3, padx=20, pady=20)

            self.buttton_gestion_vehicule = ttk.Button(self.master_frame, text='Vehicule', command=self.lancer_gestion_vehicule)
            self.buttton_gestion_vehicule.grid(row=2, column=2, padx=40, pady=20)

            self.buttton_gestion_materielle = ttk.Button(self.master_frame, text='Materielle',
                                                         command=self.lancer_gestion_materielle)
            self.button_retour = ttk.Button(self.master_frame, text='Retour',
                                                         command=self.retour_menu)
            self.buttton_gestion_materielle.grid(row=4, column=2, padx=40, pady=20)
            self.button_retour.grid(row=5, column=2, padx=40, pady=20)


        def lancer_gestion_vehicule(self):
            self.controleur.set_module("ModuleVehicule")

        def lancer_gestion_materielle(self):
            pass

        def retour_menu(self):
            self.controleur.set_module("menu")
