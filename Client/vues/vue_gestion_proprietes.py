import tkinter as tk
from tkinter import *
from tkinter import ttk
from Client.vues.vue_gerer_emp import VueGererEmp
from Utils.Table import Table
from Utils.fonction_util_vue import VueGen


class VueGestionProprietes(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.controleur = None
        # self.remplir_vue()
        self.remplir_vue_attributs()

    def set_controleur(self, controleur):
        self.controleur = controleur

    def remplir_vue(self):
        self.label_titre = ttk.Label(self, text='Gestion proprietés')
        self.label_titre.grid(row=0, column=1, columnspan=3, padx=20, pady=20)

        self.canevas_list = tk.Canvas(self, height=150, bg='white')
        self.canevas_list.grid(row=1, column=1, columnspan=2, rowspan=2, sticky=tk.E)

        VueGen.generate_button(self, "add_property", "Ajouter Proprietés", [25, None], [3, 1], [None, None], None)

        VueGen.generate_button(self, "select_properties", "Selectionner Proprietés", [25, None], [4, 1], [None, None],
                               None)

        VueGen.generate_button(self, "back", "Retour", [25, None], [5, 1], [None, None], None)

    def remplir_vue_attributs(self):
        VueGen.generate_label(self, "_titre", "Attributs proprietés", 50, 3, "groove", tk.CENTER, [0, 0], [None, 3])
        # self.label_titre = ttk.Label(self, text='Attributs proprietés')
        # self.label_titre.grid(row=0, column=0, columnspan=3, padx=20, pady=20)

        VueGen.generate_label(self, "adress", "Adresse", 20, 3, "groove", tk.CENTER, [1, 0], [None, None])
        VueGen.generate_label(self, "telephone", "Numero de Telephone", 20, 3, "groove", tk.CENTER, [2, 0],
                              [None, None])
        VueGen.generate_label(self, "e_mail", "Couriel", 20, 3, "groove", tk.CENTER, [3, 0], [None, None])
        VueGen.generate_label(self, "owner", "Proprietaire", 20, 3, "groove", tk.CENTER, [4, 0], [None, None])
        VueGen.generate_label(self, "open", "Ouverture", 20, 3, "groove", tk.CENTER, [5, 0], [None, None])
        VueGen.generate_label(self, "questions", "Questions", 20, 3, "groove", tk.CENTER, [6, 0], [None, None])

        self.label_adress_result = ttk.Label(self, text='', borderwidth=3, relief="groove", width=20)
        self.label_adress_result.grid(row=1, column=2, padx=10, pady=10)
        self.label_telephone_result = ttk.Label(self, text='', borderwidth=3, relief="groove", width=20)
        self.label_telephone_result.grid(row=2, column=2, padx=10, pady=10)
        self.label_email_result = ttk.Label(self, text='', borderwidth=3, relief="groove", width=20)
        self.label_email_result.grid(row=3, column=2, padx=10, pady=10)
        self.label_owner_result = ttk.Label(self, text='', borderwidth=3, relief="groove", width=20)
        self.label_owner_result.grid(row=4, column=2, padx=10, pady=10)
        self.label_open_result = ttk.Label(self, text='', borderwidth=3, relief="groove", width=20)
        self.label_open_result.grid(row=5, column=2, padx=10, pady=10)

        # self.label_question_result = ttk.Label(self, text='',borderwidth=3,relief="groove",width=20)
        # self.label_question_result.grid(row=6, column=2,   padx=10, pady=10)

        # VueGen.generate_label(self,"adress_result","Adresse",20,3,"groove",tk.CENTER,[1,2],[None,None])
        # ueGen.generate_label(self,"telephone_result","Adresse",20,3,"groove",tk.CENTER,[2,2],[None,None])
        # VueGen.generate_label(self,"email_result","Adresse",20,3,"groove",tk.CENTER,[3,2],[None,None])
        # VueGen.generate_label(self,"owner_result","Adresse",20,3,"groove",tk.CENTER,[4,2],[None,None])
        # VueGen.generate_label(self,"adress","Adresse",20,3,"groove",tk.CENTER,[5,2],[None,None])
        # VueGen.generate_label(self,"adress","Adresse",20,3,"groove",tk.CENTER,[6,2],[None,3])

        VueGen.generate_button(self, "back", "Retour", [50, None], [7, 0], [3, None], None)
