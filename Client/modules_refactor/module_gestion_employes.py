from traceback import print_exc

from Client.AbstractClasses.Module import Module
from Client.AbstractClasses.Vue import Vue

import tkinter as tk
from tkinter import *
from tkinter import ttk
# from Client.vues.vue_gerer_emp import VueGererEmp
from Client.modules.module_paiement import ModulePaiement


class ModuleGestionEmploye(Module):

    def __init__(self, controleur, master_frame):
        super().__init__(controleur, master_frame)

    def set_vue(self):
        return ModuleGestionEmploye.VueGestionEmploye(self, self.master_frame, row=1, column=1, padx=10, pady=10)

    class VueGestionEmploye(Vue):
        def __init__(self, parent, master_frame, row: int, column: int, padx: int, pady: int):
            super().__init__(parent, master_frame, row, column, padx, pady)

        def remplir_vue(self):
            self.canevas_list = tk.Canvas(self.master_frame, height=300, width=570, bg='white')
            self.canevas_list.grid(row=1, column=0, columnspan=3, sticky=tk.E)

            self.bouton_ajouter_membre = ttk.Button(self.master_frame, text='Ajouter Membre',
                                                    command=lambda: self.start_module_gerer_emp(None))
            self.bouton_gerer_employe = ttk.Button(self.master_frame, text='Gerer Employe',
                                                   command=self.clic_bouton_gestion_employe)

            self.bouton_retour_menu = ttk.Button(self.master_frame, text='Retour',
                                                 command=self.retour)

            #

            self.bouton_ajouter_membre.grid(row=2, column=0, pady=(20, 0), sticky=tk.E)
            self.bouton_gerer_employe.grid(row=2, column=1, pady=(20, 0), sticky=tk.E)
            self.bouton_retour_menu.grid(row=2, column=2, pady=(20, 0), sticky=tk.E)
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
            employes = self.controleur.get_employes_de_compagnie()
            if len(employes) > 0:
                for employe in employes:
                    print(employe)
                    if self.controleur.user_id != employe[0]:
                        acces = self.controleur.get_access()
                        acces = self.controleur.get_access_by_id(2)
                        # acces = self.controleur.get_access_by_id(int(employe[0]))
                        nom = employe[1] + " " + employe[2]
                        data.append((f'{nom}', f'{employe[3]}', f'{acces}', f'{employe[5]}'))

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
            # self.gerer_emp_module = Toplevel()
            self.controleur.set_module("ModuleAjoutEmploye")
            # vue = VueGererEmp(self, params, self.controleur)
            # vue.place(height=500, width=500)
            # self.gerer_emp_module.geometry("500x500")
            # self.gerer_emp_module.title("Gestion Employé")

        def retour(self):
            self.controleur.set_module("menu")
