from traceback import print_exc

from Client.AbstractClasses.Module import Module
from Client.AbstractClasses.Vue import Vue

import tkinter as tk
from tkinter import ttk

import Utils.utils
from Utils.Table import Table


class ModuleVehicule(Module):

    def __init__(self, controleur, master_frame):
        super().__init__(controleur, master_frame)

    def set_vue(self):
        return ModuleVehicule.VueVehicule(self, self.master_frame, row=0, column=0, padx=10, pady=10)

    class VueVehicule(Vue):
        def __init__(self, parent, master_frame, row: int, column: int, padx: int, pady: int):
            super().__init__(parent, master_frame, row, column, padx, pady)

        def remplir_vue(self):
                self.label_titre = ttk.Label(self.master_frame, text='Inventaire Vehciules')
                self.label_titre.grid(row=0, column=1, columnspan=3, padx=20, pady=20)
                self.liste_module = []

                self.button_vehicules_dispo = ttk.Button(self.master_frame, text='Vehicules Disponibles', width=25)
                self.button_vehicules_dispo.grid(row=1, column=1, padx=30, pady=20)

                self.button_entretien_vehicules = ttk.Button(self.master_frame, text='Entretien Vehicules', width=25)
                self.button_entretien_vehicules.grid(row=2, column=1, padx=30, pady=20)

                self.button_horaire_utilisation_vehicules = ttk.Button(self.master_frame, text="Horaire d'utilisation", width=25)
                self.button_horaire_utilisation_vehicules.grid(row=3, column=1, padx=30, pady=20)

                self.button_historique_vehicules = ttk.Button(self.master_frame, text='Historique de vehicules', width=25)
                self.button_historique_vehicules.grid(row=4, column=1, padx=30, pady=20)

                self.button_ajout_vehicule = ttk.Button(self.master_frame, text='Ajout de vehicules', width=25,
                                                        command=self.frame_ajout_vehicule)
                self.button_ajout_vehicule.grid(row=5, column=1, padx=30, pady=20)

                self.button_supression_vehicule = ttk.Button(self.master_frame, text='Supression de vehicules', width=25)
                self.button_supression_vehicule.grid(row=6, column=1, padx=30, pady=20)

                self.canevas_list = tk.Canvas(self.master_frame, height=500, width=500, bg='white')
                self.canevas_list.grid(row=1, rowspan=6, column=2, columnspan=3, sticky=tk.E, padx=30, pady=20)

                self.liste_module.append(("Ferrari", "Utilisé par:", "Jean-Marc"))
                table = Table(vue=self.canevas_list, lines_array=self.liste_module, start_row=2, start_column=0,
                              padx=50,
                              modifiable_rows=False)
                table.create()
                
                self.button_back = ttk.Button(self.master_frame, text='Retour',command=self.retourmenu , width=45)
                self.button_back.grid(row=7, column=1, columnspan=3, padx=40, pady=20)

        def retourmenu(self):
            self.controleur.set_module("menu")

        def lancer_gestion_vehicule(self):
            pass

        def lancer_gestion_materielle(self):
            pass

        def frame_ajout_vehicule(self):
           pass
        def clic_bouton_annuler(self):
            self.var_nom.set('')
            self.var_mdp.set('')

        def afficher_erreur(self, message):
            self.label_message['text'] = message
            self.label_message['foreground'] = 'red'
            self.label_message.after(3000, self.cacher_message)
            self.input_nom['foreground'] = 'red'
            self.input_mdp['foreground'] = 'red'

        def afficher_succes(self, message):
            self.label_message['text'] = message
            self.label_message['foreground'] = 'green'
            self.label_message.after(3000, self.cacher_message)
            self.input_nom['foreground'] = 'black'
            # self.var_nom.set('')
            self.input_mdp['foreground'] = 'black'
            # self.var_mdp.set('')

        def cacher_message(self):
            self.label_message['text'] = ''
