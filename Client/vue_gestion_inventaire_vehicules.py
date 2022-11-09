import tkinter as tk
from tkinter import *
from tkinter import ttk
from Client.vues.vue_gerer_emp import VueGererEmp


class VueGestionInventaireVehicules(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.controleur = None
        self.remplir_vue_gestion_inventaire_vehicules()

    def set_controleur(self, controleur):
        self.controleur = controleur

    def remplir_vue_gestion_inventaire_vehicules(self):
        self.label_titre = ttk.Label(self, text='Inventaire Vehciules')
        self.label_titre.grid(row=0, column=1, columnspan=3, padx=20, pady=20)

        self.buttton_vehicules_dispo = ttk.Button(self, text='Vehicules Disponibles',width = 25 )
        self.buttton_vehicules_dispo.grid(row=1, column=1,  padx=30, pady=20)

        self.buttton_entretien_vehicules = ttk.Button(self, text='Entretien Vehicules',width = 25)
        self.buttton_entretien_vehicules.grid(row=2, column=1, padx=30, pady=20)

        self.buttton_horaire_utilisation_vehicules = ttk.Button(self, text="Horaire d'utilisation",width = 25)
        self.buttton_horaire_utilisation_vehicules.grid(row=3, column=1, padx=30, pady=20)

        self.buttton_historique_vehicules = ttk.Button(self, text='Historique de vehicules',width = 25)
        self.buttton_historique_vehicules.grid(row=4, column=1, padx=30, pady=20)

        self.buttton_ajout_vehicule = ttk.Button(self, text='Ajout de vehicules',width = 25)
        self.buttton_ajout_vehicule.grid(row=5, column=1, padx=30, pady=20)

        self.buttton_supression_vehicule = ttk.Button(self, text='Supression de vehicules',width = 25)
        self.buttton_supression_vehicule.grid(row=6, column=1, padx=30, pady=20)

        self.canevas_list = tk.Canvas(self, height=500,width=500, bg='white')
        self.canevas_list.grid(row=1,rowspan=6, column=2, columnspan=3, sticky=tk.E,padx=30, pady=20)

        self.buttton_back = ttk.Button(self, text='Retour',width = 45)
        self.buttton_back.grid(row=7, column=1, columnspan=3, padx=40, pady=20)





    def lancer_gestion_vehicule(self):
        pass

    def lancer_gestion_materielle(self):
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
