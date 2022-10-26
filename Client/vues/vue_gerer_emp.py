import tkinter as tk
from tkinter import *
from tkinter import ttk


class VueGererEmp(ttk.Frame):
    def __init__(self, parent, vue_gestion, data):
        super().__init__(parent)
        self.vue_gestion = vue_gestion
        self.data_recu = data
        self.remplir_vue_gestion()

    def set_controleur(self, controleur):
        self.controleur = controleur

    def remplir_vue_gestion(self):

        self.data = [self.data_recu[0], "Belony", "carlens2000@live.ca", self.data_recu[1], self.data_recu[2]]
        options = [
            self.data_recu[2],
            "Tuesday",
            "Wednesday",
            "Thursday",
            "Friday",
            "Saturday",
            "Sunday"
        ]
        clicked = StringVar()
        clicked.set(self.data_recu[2])
        self.niveau_acces_selectionne = self.data_recu[2]

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
        self.bouton_enregistrer.place(x=250, y=280)

        self.bouton_annuler = Button(self, text="Annuler", command=self.clic_bouton_annuler)
        self.bouton_annuler.place(x=150, y=280)


    def niveau_acces_update(self, arg):
        self.niveau_acces_selectionne = arg
    def clic_bouton_annuler(self):
        self.vue_gestion.fermer_module_emp()

    def afficher_erreur(self, message):
        pass

    def afficher_succes(self, message):
        pass

    def clic_bouton_sauvegarder(self):
        nom = self.nom_input.get()
        prenom = self.prenom_input.get()
        identification = self.identifiant_input.get()
        role = self.titre_input.get()
        permission = self.niveau_acces_selectionne
        print ("nom = "+ nom + ", " +
               "prenom = "+ prenom + ", " +
               "identification = "+ identification + ", " +
               "role = "+ role + ", " +
               "permission = "+ permission)
        self.vue_gestion.fermer_module_emp()
