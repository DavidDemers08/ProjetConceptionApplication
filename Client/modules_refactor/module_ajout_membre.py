from traceback import print_exc

from Client.AbstractClasses.Module import Module
from Client.AbstractClasses.Vue import Vue

import tkinter as tk
from tkinter import *
from tkinter import ttk
#from Client.vues.vue_gerer_emp import VueGererEmp
from Client.modules.module_paiement import ModulePaiement

"""---------------------------------------------GERER EMPLOYE----------------------------------------------"""
class ModuleAjoutEmploye(Module):

    def __init__(self, controleur, master_frame):
        super().__init__(controleur, master_frame)

    def set_vue(self):
        return ModuleAjoutEmploye.VueGererEmp(self, self.master_frame, row=1, column=1, padx=10, pady=10)

    class VueGererEmp(Vue):
        def __init__(self, parent, master_frame, row: int, column: int, padx: int, pady: int):
            super().__init__(parent, master_frame, row, column, padx, pady)

            self.data_recu = None
            """
    
            :param vue_gestion: ne pas toucher, représente la vue originale
            :param data: contient le Prénom [0],nom[1], l'identifiant[2] le mot-de-passe[3] et le titre[4] et le niveau d'acces[5] en String.
            #TODO utiliser le data pour faire une request au DAO de tout les infos sur l'employé en
            # question pour remplacer les données hardcodées sur l'employé
            """
            #self.data_recu = data
            self.permission = 1
            #self.remplir_vue_gestion()

        def remplir_vue(self):
            if self.data_recu is not None:
                # Si il y a du data recu, on modifie un employé. sinon, on crée un nouvel employé
                self.data = [self.data_recu[0], "Belony", self.data_recu[1], self.data_recu[3], self.data_recu[2],
                             "Desjardins"]
            else:
                self.data = ["", "", "", "", "", "Aucun", "Desjardins"]
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

            # TODO mettre des vrais compagnies
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

            self.titre_module = Label(self.master_frame, text="Creation Employé", font='Times 14')
            self.titre_module.place(x=150, y=10)

            self.prenom = Label(self.master_frame, text="Prénom")
            self.prenom.place(x=100, y=40)

            self.nom = Label(self.master_frame, text="Nom").place(x=100, y=70)

            self.identifiant = Label(self.master_frame, text="Identifiant")
            self.identifiant.place(x=100, y=100)

            self.titre_employe = Label(self.master_frame, text="Titre")
            self.titre_employe.place(x=100, y=130)

            self.titre_employe = Label(self.master_frame, text="Mot de passe")
            self.titre_employe.place(x=100, y=160)

            self.niveau_acces = Label(self.master_frame, text="Permission")
            self.niveau_acces.place(x=100, y=190)

            self.niveau_acces = Label(self.master_frame, text="Niveau d'accès")
            self.niveau_acces.place(x=100, y=220)

            self.prenom_input = Entry(self.master_frame, width=30)
            self.prenom_input.insert(END, self.data[0])
            self.prenom_input.place(x=200, y=40)

            self.nom_input = Entry(self.master_frame, width=30)
            self.nom_input.insert(END, self.data[1])
            self.nom_input.place(x=200, y=70)

            self.identifiant_input = Entry(self.master_frame, width=30)
            self.identifiant_input.insert(END, self.data[2])
            self.identifiant_input.place(x=200, y=100)

            self.titre_input = Entry(self.master_frame, width=30)
            self.titre_input.insert(END, self.data[3])
            self.titre_input.place(x=200, y=130)

            self.mdp_input = Entry(self.master_frame, width=30)
            self.mdp_input.insert(END, self.data[4])
            self.mdp_input.place(x=200, y=160)

            self.permission_input = Entry(self.master_frame, width=30)
            self.permission_input.insert(END, self.data[5])
            self.permission_input.place(x=200, y=190)

            self.niveau_acces_input = OptionMenu(self.master_frame, clicked, *options, command=self.niveau_acces_update)
            self.niveau_acces_input.place(x=200, y=220)
            self.bouton_enregistrer = ttk.Button(self.master_frame, text="Enregistrer",
                                                 command=self.clic_bouton_sauvegarder)
            self.bouton_enregistrer.place(x=280, y=300)

            self.bouton_annuler = ttk.Button(self.master_frame, text="Annuler", command=self.clic_bouton_annuler)
            self.bouton_annuler.place(x=120, y=300)
            if self.permission > 0:
                compteur = 0
                for i in options_compagnie:
                    try:
                        self.compagnie_input = OptionMenu(self.master_frame, clicked_compagnie, *options_compagnie[compteur][0],
                                                          command=self.compagnie_update)
                        compteur += 1
                    except:
                        compteur += 1
                self.compagnie_input.place(x=200, y=260)
                self.compagnie = ttk.Label(self.master_frame, text="Compagnie")
                self.compagnie.place(x=100, y=260)




        def compagnie_update(self, arg):
            self.compagnie_selectionnee = arg


        def niveau_acces_update(self, arg):
            self.niveau_acces_selectionne = arg


        def clic_bouton_annuler(self):
            self.controleur.set_module("GestionMembre")

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
            if len(nom) > 0 and len(prenom) > 0 and len(identification) > 0 and len(titre) > 0 and isinstance(
                    permission, int) and len(mdp) > 0:
                reponse = self.controleur.creer_usager(prenom, nom, identification, mdp, titre, genre, compagnie,
                                                       permission, acced)
                print(reponse)
                self.controleur.set_module("ModuleAjoutEmploye")

            else:
                print("Un des champs ne respecte pas les conditions")