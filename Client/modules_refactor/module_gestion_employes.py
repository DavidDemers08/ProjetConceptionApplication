from traceback import print_exc

from Client.AbstractClasses.Module import Module
from Client.AbstractClasses.Vue import Vue

import tkinter as tk
from tkinter import *
from tkinter import ttk
from Client.vues.vue_gerer_emp import VueGererEmp
from Client.modules.module_paiement import ModulePaiement


class ModuleGestionEmploye(Module):

    def __init__(self, controleur, master_frame):
        super().__init__(controleur, master_frame)

    def set_vue(self):
        return ModuleGestionEmploye.VueGestionEmploye(self, self.master_frame, row=1, column=1, padx=10, pady=10)

    class VueGestionEmploye(Vue):
        def __init__(self, parent,master_frame, row: int, column: int, padx: int, pady: int):
            super().__init__(parent,master_frame, row, column, padx, pady)

        def remplir_vue(self):
            self.canevas_list = tk.Canvas(self.master_frame, height=200, width=600, bg='white')
            self.canevas_list.grid(row=1, column=0, columnspan=3, sticky=tk.E)

            self.bouton_ajouter_membre = ttk.Button(self.master_frame, text='Ajouter Membre',
                                                    command=lambda: self.start_module_gerer_emp(None))
            self.bouton_gerer_employe = ttk.Button(self.master_frame, text='Gerer Employe', command=self.clic_bouton_gestion_employe)

            #

            self.bouton_ajouter_membre.grid(row=2, column=0, pady=(20, 0), sticky=tk.E)
            self.bouton_gerer_employe.grid(row=2, column=1, pady=(20, 0), sticky=tk.E)
            colonnes = ('Nom', 'Identifiant', 'Permission', 'Rôle')
            self.liste = ttk.Treeview(self.canevas_list, columns=colonnes, show='headings',
                                      selectmode='browse')
            self.canevas_list.create_window(0, 0, window=self.liste, width=200, height=200)
            ttk.Button(self.master_frame, text='Ajouter Membre',
                       command=lambda: self.start_module_gerer_emp(None)),
            ttk.Button(self.master_frame, text='Gerer Employe', command=self.clic_bouton_gestion_employe)


            data = []
            # b = self.controleur.test()
            # print(b)
            employes = self.controleur.get_employes_de_compagnie(self.controleur.user_id)
            if len(employes) > 0:
                for employe in employes:
                    print(employe)
                    if self.controleur.user_id != employe[0]:
                        # acces = self.controleur.get_access()
                        acces = self.controleur.get_access_by_id(2)
                        acces = self.controleur.get_access_by_id(int(employe[0]))
                        nom = employe[1] + " " + employe[2]
                        data.append((f'{nom}', f'{employe[3]}', f'{acces}', f'{employe[6]}'))



            self.liste.heading('Nom', text='Nom')
            self.liste.heading('Identifiant', text='Identifiant')
            self.liste.heading('Permission', text='Permission')
            self.liste.heading('Rôle', text='Rôle')

            self.liste.column('Rôle', anchor='center', stretch=NO, width=150)
            self.liste.column('Identifiant', anchor='center', stretch=NO, width=150)
            self.liste.column('Permission', anchor='center', stretch=NO, width=150)
            self.liste.column('Nom', anchor='center', stretch=NO, width=150)

            for emp in data:
                self.liste.insert('', tk.END, values=emp)
            self.liste.place(x=0, y=0)

        def clic_bouton_gestion_employe(self):
            selection = self.liste.selection()
            if selection:
                item = self.liste.item(selection[0])
                record = item['values']
                self.start_module_gerer_emp(record)

        def start_module_gerer_emp(self, params):
            self.gerer_emp_module = Toplevel()
            vue = VueGererEmp(self, params, self.controleur)
            vue.place(height=500, width=500)
            self.gerer_emp_module.geometry("500x500")
            self.gerer_emp_module.title("Gestion Employé")

        def fermer_module_emp(self):
            self.gerer_emp_module.destroy()

        """---------------------------------------------GERER EMPLOYE----------------------------------------------"""

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

                self.titre_module = Label(self, text="Creation Employé", font=('Times 14'))
                self.titre_module.place(x=150, y=10)

                self.prenom = Label(self, text="Prénom")
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

                self.niveau_acces_input = OptionMenu(self, clicked, *options, command=self.niveau_acces_update)
                self.niveau_acces_input.place(x=200, y=220)

                if self.permission > 0:
                    compteur = 0
                    for i in options_compagnie:
                        try:
                            self.compagnie_input = OptionMenu(self, clicked_compagnie, *options_compagnie[compteur][0],
                                                              command=self.compagnie_update)
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
                if len(nom) > 0 and len(prenom) > 0 and len(identification) > 0 and len(titre) > 0 and isinstance(
                        permission, int) and len(mdp) > 0:
                    reponse = self.controleur.creer_usager(prenom, nom, identification, mdp, titre, genre, compagnie,
                                                           permission, acced)
                    print(reponse)
                    self.vue_gestion.fermer_module_emp()

                else:
                    print("Un des champs ne respecte pas les conditions")