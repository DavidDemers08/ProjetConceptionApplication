import tkinter as tk
from tkinter import ttk
import Utils.utils
from Serveur.DAO.dao import Dao
from vue import Vue

class VueOnlineSales(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.controleur = None
        # self.remplir_vue_ventes_main()
        self.rempli_vue_faire_commande()
        self.parent= parent

    def set_controleur(self, controleur):
        self.controleur = controleur

    def vider_frame(self):
        for widget in self.winfo_children():
            widget.destroy()

    def remplir_vue_ventes_main(self):
        self.label_titre = ttk.Label(self,text='Ventes en ligne' )
        self.label_titre.grid(row=0, column=1,columnspan=2)

        self.bouton_faire_commande = ttk.Button(self, text='Faire une commande' ,width = 25)
        self.bouton_faire_commande.grid(row=1, column=1,columnspan=3, pady=(20, 0), sticky=tk.E)

        self.bouton_verifier_commande = ttk.Button(self, text='Verifier une commande',width = 25)
        self.bouton_verifier_commande.grid(row=3, column=1,columnspan=3, pady=(20, 0), sticky=tk.E)

        self.bouton_completer_commande = ttk.Button(self, text='Completer une commande',width = 25 )
        self.bouton_completer_commande.grid(row=5, column=1,columnspan=3, pady=(20, 0), sticky=tk.E)

        self.bouton_back = ttk.Button(self, text='Retour',width = 25 )
        self.bouton_back.grid(row=7, column=1,columnspan=3, pady=(20, 0), sticky=tk.E)

    def rempli_vue_faire_commande(self):
        OPTIONS = [
            "Jan",
            "Feb",
            "Mar"
        ]  # etc


        self.variable = tk.StringVar(self)
        self.variable.set(OPTIONS[0])  # default value


        self.label_titre = ttk.Label(self, text='Faire une commande')
        self.label_titre.grid(row=0, column=1, columnspan=2)

        self.label_type_unite = ttk.Label(self, text="Type d'unité",width = 20, borderwidth=2, relief="groove")
        self.label_type_unite.grid(row=1, column=1,pady=(20, 0) )

        self.unite_dropdown = ttk.OptionMenu(self, self.variable, *OPTIONS,)
        self.unite_dropdown.grid(row=1, column=2,pady=(20, 0), columnspan=3)

        self.label_prix = ttk.Label(self, text="Prix",width = 20, borderwidth=2, relief="groove")
        self.label_prix.grid(row=2, column=1, pady=(20, 0), )
        self.label_date = ttk.Label(self, text="Date",width = 20, borderwidth=2, relief="groove")
        self.label_date.grid(row=3, column=1,pady=(20, 0),  )
        self.label_acheteur = ttk.Label(self, text="Acheteur",width = 20, borderwidth=2, relief="groove")
        self.label_acheteur.grid(row=4, column=1,pady=(20, 0), )
        self.label_paeiment = ttk.Label(self, text="Paiement",width = 20, borderwidth=2, relief="groove")
        self.label_paeiment.grid(row=5, column=1,pady=(20, 0),  )

        self.button_back =  ttk.Button(self, text='Retour')
        self.button_back.grid(row=6, column=1,pady=(20, 0), columnspan=2)


