import tkinter as tk
from tkinter import *
from tkinter import ttk


class VueGererEmp(ttk.Frame):
    def __init__(self, vue_gestion, data):
        super().__init__(vue_gestion.gerer_emp_module)
        self.vue_gestion = vue_gestion
        self.data_recu = data
        self.remplir_vue_gestion()




    def set_controleur(self, controleur):
        self.controleur = controleur

    def remplir_vue_gestion(self):
        if self.data_recu is not None:
            self.data = [self.data_recu[0], "Belony", "carlens2000@live.ca", self.data_recu[1], self.data_recu[2]]
        else: self.data = ["", "", "", "", "Aucun",]
        options = [
            "Aucun",
            "Programmeur",
            "Entrepreneur",
            "Mécanicier",
            "Ingénieur",
            "Gestionnaire",
            "Concierge"
        ]
        clicked = StringVar()
        clicked.set(options[0])
        self.niveau_acces_selectionne = self.data[4]


        self.titre_module = Label(self, text="Gestion d'Employé", font=('Times 14'))
        self.titre_module.place(x=150, y=10)

        self.prenom = Label(self,text="Prénom")
        self.prenom.place(x=100, y=60)

        self.nom = Label(self, text="Nom").place(x=100, y=100)

        self.identifiant = Label(self, text="Identifiant")
        self.identifiant.place(x=100, y=140)

        self.titre_employe = Label(self, text="Titre")
        self.titre_employe.place(x=100, y=180)

        self.niveau_acces = Label(self, text="Niveau d'accès")
        self.niveau_acces.place(x=100, y=220)

        self.prenom_input = Entry(self, width=30)
        self.prenom_input.insert(END, self.data[0])
        self.prenom_input.place(x=200, y=60)

        self.nom_input = Entry(self, width=30)
        self.nom_input.insert(END, self.data[1])
        self.nom_input.place(x=200, y=100)

        self.identifiant_input = Entry(self, width=30)
        self.identifiant_input.insert(END, self.data[2])
        self.identifiant_input.place(x=200, y=140)

        self.titre_input = Entry(self, width=30)
        self.titre_input.insert(END, self.data[3])
        self.titre_input.place(x=200, y=180)

        self.niveau_acces_input = OptionMenu(self, clicked , *options, command=self.niveau_acces_update)
        self.niveau_acces_input.place(x=200, y=220)

        self.bouton_enregistrer = Button(self, text="Enregistrer", command=self.clic_bouton_sauvegarder)
        self.bouton_enregistrer.place(x=280, y=280)

        self.bouton_annuler = Button(self, text="Annuler", command=self.clic_bouton_annuler)
        self.bouton_annuler.place(x=120, y=280)

        self.bouton_supprimer = Button(self, text="Supprimer", command=self.supprimer_emp)
        self.bouton_supprimer.place(x=200, y=280)


    def niveau_acces_update(self, arg):
        self.niveau_acces_selectionne = arg

    def clic_bouton_annuler(self):
        self.vue_gestion.fermer_module_emp()

    def afficher_erreur(self):
        pass

    def supprimer_emp(self, message):
        print('Employé supprimé!')
        self.vue_gestion.fermer_module_emp()

    def clic_bouton_sauvegarder(self):
        nom = self.nom_input.get()
        prenom = self.prenom_input.get()
        identification = self.identifiant_input.get()
        role = self.titre_input.get()
        permission = self.niveau_acces_selectionne
        if len(nom) > 0 and len(prenom) > 0 and len(identification) > 0 and len(role) > 0:
            print ("nom = "+ nom + ", " +
                   "prenom = "+ prenom + ", " +
                   "identification = "+ identification + ", " +
                   "role = "+ role + ", " +
                   "permission = "+ permission)
            self.vue_gestion.fermer_module_emp()
        else: self.afficher_erreur()
