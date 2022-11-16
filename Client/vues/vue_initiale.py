import tkinter as tk
from tkinter import ttk

import Utils.utils
from Serveur.DAO.dao import Dao


class Vue(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.controleur = None
        self.remplir_vue()
        self.parent = parent

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

        self.bouton_enregister = ttk.Button(self, text='Enregistrer une nouvelle compagnie', command=self.clic_bouton_enregister)
        self.bouton_enregister.bind('<Return>', lambda e: self.bouton_enregister.invoke())
        self.bouton_enregister.grid(row=5, column=1, pady=(10, 0), sticky=tk.E)

        self.label_message = ttk.Label(self, text='', foreground='red')
        self.label_message.grid(row=5, column=0, columnspan=2, sticky=tk.W)

    def clic_bouton_connexion(self):
        if self.controleur:
            # message d'erreur par controleur ou par vue?
            reponse = self.controleur.identifier_usager(self.var_nom.get(), self.var_mdp.get())
            if reponse:
                self.controleur.user_id = self.controleur.get_username_id(self.var_nom.get())
                self.controleur.access = self.controleur.get_access()

                print(self.controleur.user_id)
                print(self.controleur.access)

                self.controleur.afficher_gestion()
            else:
                self.afficher_erreur(f'Nom ou mot de passe incorrects')

    def clic_bouton_annuler(self):
        self.var_nom.set('')
        self.var_mdp.set('')

    def clic_bouton_enregister(self):
        self.vider_frame()
        self.afficher_enregistrer()

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

    def fonction_facile_a_faire_vraiment(self, label, input, texte):
        label = ttk.Label(self, text=texte)
        label.grid(row=1, column=0, pady=(5, 0), sticky=tk.E)

        var = tk.StringVar()
        input = ttk.Entry(self, textvariable=var, width=30)
        input.grid(row=1, column=1, sticky=tk.E)
        return

    def afficher_enregistrer(self):
        self.label_nom_compagnie = ttk.Label(self, text='Nom Compagnie ')
        self.label_nom_compagnie.grid(row=1, column=0, pady=(5, 0), sticky=tk.E)
        self.var_nom_compagnie = tk.StringVar()
        self.input_nom_compagnie = ttk.Entry(self, textvariable=self.var_nom_compagnie, width=30)
        self.input_nom_compagnie.grid(row=1, column=1, sticky=tk.E)

        self.label_pays = ttk.Label(self, text='pays ')
        self.label_pays.grid(row=2, column=0, pady=(5, 0), sticky=tk.E)
        self.var_pays = tk.StringVar()
        self.input_pays = ttk.Entry(self, textvariable=self.var_pays, width=30)
        self.input_pays.grid(row=2, column=1, sticky=tk.E)

        self.label_province = ttk.Label(self, text='province/etat ')
        self.label_province.grid(row=3, column=0, pady=(5, 0), sticky=tk.E)
        self.var_province = tk.StringVar()
        self.input_province = ttk.Entry(self, textvariable=self.var_province, width=30)
        self.input_province.grid(row=3, column=1, sticky=tk.E)

        self.label_region = ttk.Label(self, text='region')
        self.label_region.grid(row=4, column=0, pady=(5, 0), sticky=tk.E)
        self.var_region = tk.StringVar()
        self.input_region = ttk.Entry(self, textvariable=self.var_region, width=30)
        self.input_region.grid(row=4, column=1, sticky=tk.E)

        self.bouton_enregister_ville = ttk.Button(self, text='Enregistrer', command=self.clic_bouton_enregistrer_ville)
        self.bouton_enregister_ville.bind('<Return>', lambda e: self.bouton_enregister_ville.invoke())
        self.bouton_enregister_ville.grid(row=5, column=1, pady=(10, 0), sticky=tk.E)

    def clic_bouton_enregistrer_ville(self):
        nom_compagnie = self.var_nom_compagnie.get()
        if self.controleur.rechercher_compagnie(nom_compagnie) is False:
            self.vider_frame()
            self.afficher_enregistrement_admin()
        else:
            print("Cette ville existe déjà")
            print(self.controleur.afficher_compagnies())


    def afficher_enregistrement_admin(self):
        self.label_uti_admin = ttk.Label(self, text='Nom utilisateur ')
        self.label_uti_admin.grid(row=1, column=0, pady=(5, 0), sticky=tk.E)
        self.var_uti_admin = tk.StringVar()
        self.input_uti_admin = ttk.Entry(self, textvariable=self.var_uti_admin, width=30)
        self.input_uti_admin.grid(row=1, column=1, sticky=tk.E)

        self.label_mdp_admin = ttk.Label(self, text='Mot de passe ')
        self.label_mdp_admin.grid(row=2, column=0, pady=(5, 0), sticky=tk.E)
        self.var_mdp_admin = tk.StringVar()
        self.input_mdp_admin = ttk.Entry(self, textvariable=self.var_mdp_admin, show="*", width=30)
        self.input_mdp_admin.grid(row=2, column=1, sticky=tk.E)

        self.label_verif_mdp_admin = ttk.Label(self, text='Vérifier le mot de passe ')
        self.label_verif_mdp_admin.grid(row=3, column=0, pady=(5, 0), sticky=tk.E)
        self.var_verif_mdp_admin = tk.StringVar()
        self.input_verif_mdp_admin = ttk.Entry(self, textvariable=self.var_verif_mdp_admin, show="*", width=30)
        self.input_verif_mdp_admin.grid(row=3, column=1, sticky=tk.E)

        self.label_nom_admin = ttk.Label(self, text='Nom ')
        self.label_nom_admin.grid(row=4, column=0, pady=(5, 0), sticky=tk.E)
        self.var_nom_admin = tk.StringVar()
        self.input_nom_admin = ttk.Entry(self, textvariable=self.var_nom_admin, width=30)
        self.input_nom_admin.grid(row=4, column=1, sticky=tk.E)

        self.label_prenom_admin = ttk.Label(self, text='Prenom ')
        self.label_prenom_admin.grid(row=5, column=0, pady=(5, 0), sticky=tk.E)
        self.var_prenom_admin = tk.StringVar()
        self.input_prenom_admin = ttk.Entry(self, textvariable=self.var_prenom_admin, width=30)
        self.input_prenom_admin.grid(row=5, column=1, sticky=tk.E)

        self.label_genre_admin = ttk.Label(self, text='Genre Admin (H/F)')
        self.label_genre_admin.grid(row=6, column=0, pady=(5, 0), sticky=tk.E)
        self.var_genre_admin = tk.StringVar()
        self.input_genre_admin = ttk.Entry(self, textvariable=self.var_genre_admin, width=30)
        self.input_genre_admin.grid(row=6, column=1, sticky=tk.E)

        self.bouton_enregister_admin = ttk.Button(self, text='Enregistrer Admin', command=self.clic_bouton_enregistrer_admin)
        self.bouton_enregister_admin.bind('<Return>', lambda e: self.bouton_enregister_admin.invoke())
        self.bouton_enregister_admin.grid(row=7, column=1, pady=(10, 0), sticky=tk.E)


    def clic_bouton_enregistrer_admin(self):
        nom_compagnie = self.var_nom_compagnie.get()
        pays = self.var_pays.get()
        province = self.var_province.get()
        region = self.var_region.get()
        uti_admin = self.var_uti_admin.get()
        mdp = self.var_mdp_admin.get()
        verif_mdp = self.var_verif_mdp_admin.get()
        genre = self.var_genre_admin.get()
        nom = self.var_nom_admin.get()
        prenom = self.var_prenom_admin.get()

        if mdp == verif_mdp:
            args = {Utils.utils.NOM_VILLE: nom_compagnie,
                    Utils.utils.NOM_USAGER: uti_admin,
                    Utils.utils.MDP: mdp,
                    Utils.utils.PAYS: pays,
                    Utils.utils.PROVINCE: province,
                    Utils.utils.REGION: region,
                    Utils.utils.GENRE: genre,
                    Utils.utils.NOM: nom,
                    Utils.utils.PRENOM: prenom
                    }

            if nom_compagnie and uti_admin and mdp and pays and province and region and genre and prenom and nom:
                reponse = self.controleur.creer_compte_ville(**args)
        else:
            print("Les deux cases des mots de passe ne sont pas identiques")

