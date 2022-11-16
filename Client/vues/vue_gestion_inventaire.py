import tkinter as tk
from tkinter import *
from tkinter import ttk
from Client.vues.vue_gerer_emp import VueGererEmp


class VueGestionInventaire(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.controleur = None
        self.remplir_vue_gestion_inventaire()

    def set_controleur(self, controleur):
        self.controleur = controleur

    def remplir_vue_gestion_inventaire(self):
        self.label_titre = ttk.Label(self, text='Gestion Inventaire')
        self.label_titre.grid(row=1, column=1, columnspan=3, padx=20, pady=20)

        self.buttton_gestion_vehicule = ttk.Button(self, text='Vehicule', command=self.lancer_gestion_vehicule)
        self.buttton_gestion_vehicule.grid(row=2, column=2,  padx=40, pady=20)

        self.buttton_gestion_materielle = ttk.Button(self, text='Materielle', command=self.lancer_gestion_materielle)
        self.buttton_gestion_materielle.grid(row=4, column=2,  padx=40, pady=20)


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
