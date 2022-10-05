import tkinter as tk
from tkinter import *
from tkinter import ttk


class VueGestion(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        #self.controleur = None
        self.remplir_vue_gestion()



    def set_controleur(self, controleur):
        self.controleur = controleur

    def remplir_vue_gestion(self):

        self.data =[1,2,3,4]
        self.bouton_gestion_membre = ttk.Button(self, text='Gestion Membre', command=self.clic_bouton_membre)
        self.bouton_gestion_membre.grid(row=0, column=0, pady=(20, 0), sticky=tk.E)

        self.bouton_gestion_projet = ttk.Button(self, text='Gestion des projets ERP', command=self.clic_bouton_projets)
        self.bouton_gestion_projet.grid(row=0, column=1, pady=(20, 0), sticky=tk.E)

        self.bouton_gestion_modules = ttk.Button(self, text='Gestion modules', command=self.clic_bouton_modules)
        self.bouton_gestion_modules.grid(row=0, column=2, pady=(20, 0), sticky=tk.E)

        self.canevas_list = tk.Canvas(self,width=200,height=200, bg= 'white')
        self.canevas_list.grid(row = 1, column=0, columnspan=3, sticky=tk.S)

        self.list = tk.Listbox(self, height=5, width=5)
        for i in self.data:
            self.list.insert(i)

        self.canevas_list.create_window(0, 0, window=self.list, width=200, height=200)



        """
        self.bouton_connexion.bind('<Return>', lambda e: self.bouton_connexion.invoke())
        self.bouton_connexion.grid(row=3, column=1, pady=(20, 0), sticky=tk.E)

        self.bouton_annuler = ttk.Button(self, text='Annuler', command=self.clic_bouton_annuler)
        self.bouton_annuler.bind('<Return>', lambda e: self.bouton_annuler.invoke())
        self.bouton_annuler.grid(row=4, column=1, pady=(10, 0), sticky=tk.E)

        self.label_message = ttk.Label(self, text='', foreground='red')
        self.label_message.grid(row=5, column=0, columnspan=2, sticky=tk.W)
       """

    def clic_bouton_membre(self):
        pass
    def clic_bouton_projets(self):
        pass

    def clic_bouton_modules(self):
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

    #def list_box(self):
       # self.w = Listbox()