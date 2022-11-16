import tkinter as tk
from tkinter import *
from tkinter import ttk

import Utils.utils


class VueGererEmp(ttk.Frame):
    def __init__(self, vue_gestion, data, controleur):
        """

        :param vue_gestion: ne pas toucher, représente la vue originale
        :param data: contient le Prénom [0],nom[1], l'identifiant[2] le mot-de-passe[3] et le titre[4] et le niveau d'acces[5] en String.
        #TODO utiliser le data pour faire une request au DAO de tout les infos sur l'employé en
        # question pour remplacer les données hardcodées sur l'employé
        """
        super().__init__(vue_gestion.gerer_emp_module)
        self.controleur = controleur
        self.vue_gestion = vue_gestion
        self.data_recu = data
        self.permission = 1
        self.remplir_vue_gestion()
        


    def remplir_vue_gestion(self):
        if self.data_recu is not None:
            # Si il y a du data recu, on modifie un employé. sinon, on crée un nouvel employé
            self.data = [self.data_recu[0], "Belony", self.data_recu[1], self.data_recu[3], self.data_recu[2], "Desjardins"]
        else: self.data = ["", "", "", "","", "Aucun","Desjardins"]
        # TODO mettre des vrais niveaux d'accès
        options = [
            self.data_recu[2] if self.data_recu else "Aucun",
            "Programmeur",
            "Entrepreneur",
            "Mécanicier",
            "Ingénieur",
            "Gestionnaire",
            "Concierge"
        ]
        clicked = StringVar()
        clicked.set(options[0])

        #TODO mettre des vrais compagnies
        options_compagnie_id = self.controleur.get_all_id_compagnie_utilisateur(self.controleur.user_id)[0]
        options_compagnie = []
        compteur = 0

        for id_com in options_compagnie_id:
            options_compagnie.append(self.controleur.get_name_compagnie_byid(id_com))

        clicked_compagnie = StringVar()
        for i in options_compagnie:
            try:
                if options_compagnie[compteur][0][0] != "":
                    clicked_compagnie.set(options_compagnie[compteur][0][0])
                    compteur += 1
            except:
                compteur += 1

        self.niveau_acces_selectionne = self.data[4]
        self.compagnie_selectionnee = self.data[5]

        self.titre_module = Label(self, text="Creation Employé", font=('Times 14'))
        self.titre_module.place(x=150, y=10)

        self.prenom = Label(self,text="Prénom")
        self.prenom.place(x=100, y=40)

        self.nom = Label(self, text="Nom").place(x=100, y=70)

        self.identifiant = Label(self, text="Identifiant")
        self.identifiant.place(x=100, y=100)

        self.titre_employe = Label(self, text="Titre")
        self.titre_employe.place(x=100, y=130)

        self.titre_employe = Label(self, text="Mot de passe")
        self.titre_employe.place(x=100, y=160)

        self.niveau_acces = Label(self, text="Permission")
        self.niveau_acces.place(x=100, y=190)

        self.niveau_acces = Label(self, text="Niveau d'accès")
        self.niveau_acces.place(x=100, y=220)

        self.prenom_input = Entry(self, width=30)
        self.prenom_input.insert(END, self.data[0])
        self.prenom_input.place(x=200, y=40)

        self.nom_input = Entry(self, width=30)
        self.nom_input.insert(END, self.data[1])
        self.nom_input.place(x=200, y=70)

        self.identifiant_input = Entry(self, width=30)
        self.identifiant_input.insert(END, self.data[2])
        self.identifiant_input.place(x=200, y=100)

        self.titre_input = Entry(self, width=30)
        self.titre_input.insert(END, self.data[3])
        self.titre_input.place(x=200, y=130)

        self.mdp_input = Entry(self, width=30)
        self.mdp_input.insert(END, self.data[4])
        self.mdp_input.place(x=200, y=160)

        self.permission_input = Entry(self, width=30)
        self.permission_input.insert(END, self.data[5])
        self.permission_input.place(x=200, y=190)

        self.niveau_acces_input = OptionMenu(self, clicked , *options, command=self.niveau_acces_update)
        self.niveau_acces_input.place(x=200, y=220)

        if self.permission > 0:
            compteur = 0
            for i in options_compagnie:
                try:
                    self.compagnie_input = OptionMenu(self, clicked_compagnie, *options_compagnie[compteur][0], command=self.compagnie_update)
                    compteur += 1
                except:
                    compteur += 1
            self.compagnie_input.place(x=200, y=260)
            self.compagnie = Label(self, text="Compagnie")
            self.compagnie.place(x=100, y=260)

        self.bouton_enregistrer = Button(self, text="Enregistrer", command=self.clic_bouton_sauvegarder)
        self.bouton_enregistrer.place(x=280, y=300)

        self.bouton_annuler = Button(self, text="Annuler", command=self.clic_bouton_annuler)
        self.bouton_annuler.place(x=120, y=300)


    def compagnie_update(self, arg):
        self.compagnie_selectionnee = arg

    def niveau_acces_update(self, arg):
        self.niveau_acces_selectionne = arg

    def clic_bouton_annuler(self):
        self.vue_gestion.fermer_module_emp()

    def supprimer_emp(self, evt):
        identification = self.identifiant_input.get()
        # représente l'identifiant
        # TODO utiliser l'identifiant pour supprimer l'employé de la base de donnée
        print('Employé supprimé!')
        self.vue_gestion.fermer_module_emp()

    def afficher_erreur(self):
        pass

    def clic_bouton_sauvegarder(self):
        prenom = self.prenom_input.get()
        nom = self.nom_input.get()
        identification = self.identifiant_input.get()
        titre = self.titre_input.get()
        mdp = self.mdp_input.get()
        acced = self.niveau_acces_selectionne
        genre = ""
        # TODO a changer le id
        compagnie = 1
        try:
            permission = int(self.permission_input.get())

        except:
            args = None
            permission = ""

        # TODO utiliser l'identifiant comme clé pour update ou ajouter les informations de l'employé dans la base de donnée
        if len(nom) > 0 and len(prenom) > 0 and len(identification) > 0 and len(titre) > 0 and isinstance(permission,int) and len(mdp) > 0:
            reponse = self.controleur.creer_usager(prenom,nom,identification,mdp,titre,genre,compagnie,permission,acced)
            print(reponse)
            self.vue_gestion.fermer_module_emp()

        else:
            print("Un des champs ne respecte pas les conditions")