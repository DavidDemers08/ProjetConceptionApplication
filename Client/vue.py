import tkinter as tk
from tkinter import ttk


class Vue(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.controleur = None
        self.remplir_vue()

    def set_controleur(self, controleur):
        self.controleur = controleur

    def vider_frame(self):
        for widget in self.winfo_children():
            widget.destroy()


    def remplir_vue(self):
        self.label_nom = ttk.Label(self, text='Nom ')
        self.label_nom.grid(row=1, column=0, pady=(5, 0), sticky=tk.E)

        self.var_nom = tk.StringVar()
        self.input_nom = ttk.Entry(self, textvariable=self.var_nom, width=30)
        self.input_nom.grid(row=1, column=1, sticky=tk.E)

        self.label_mdp = ttk.Label(self, text='Mot de passe ')
        self.label_mdp.grid(row=2, column=0, pady=(5, 0), sticky=tk.E)

        self.var_mdp = tk.StringVar()
        self.input_mdp = ttk.Entry(self, textvariable=self.var_mdp, show='*', width=30)
        self.input_mdp.grid(row=2, column=1, sticky=tk.E)

        self.bouton_connexion = ttk.Button(self, text='Connexion', command=self.clic_bouton_connexion)
        self.bouton_connexion.bind('<Return>', lambda e: self.bouton_connexion.invoke())
        self.bouton_connexion.grid(row=3, column=1, pady=(20, 0), sticky=tk.E)

        self.bouton_annuler = ttk.Button(self, text='Annuler', command=self.clic_bouton_annuler)
        self.bouton_annuler.bind('<Return>', lambda e: self.bouton_annuler.invoke())
        self.bouton_annuler.grid(row=4, column=1, pady=(10, 0), sticky=tk.E)

        self.bouton_enreigister = ttk.Button(self, text='Enreigistrer', command=self.clic_bouton_enreigister)
        self.bouton_enreigister.bind('<Return>', lambda e: self.bouton_enreigister.invoke())
        self.bouton_enreigister.grid(row=5, column=1, pady=(10, 0), sticky=tk.E)

        self.label_message = ttk.Label(self, text='', foreground='red')
        self.label_message.grid(row=5, column=0, columnspan=2, sticky=tk.W)

    def clic_bouton_connexion(self):
        if self.controleur:
            # message d'erreur par controleur ou par vue?
            reponse = self.controleur.identifier_usager(self.var_nom.get(), self.var_mdp.get())
            if len(reponse):
                self.afficher_succes(reponse)
            else:
                self.afficher_erreur(f'Nom ou mot de passe incorrects')

    def clic_bouton_annuler(self):
        self.var_nom.set('')
        self.var_mdp.set('')
    def clic_bouton_enreigister(self):
        self.vider_frame()



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
