import tkinter as tk
from tkinter import *
from tkinter import ttk
from Client.vues.vue_gerer_emp import VueGererEmp


class VueGestion(ttk.Frame):
    def __init__(self, parent, controleur):
        super().__init__(parent)
        self.controleur = controleur
        self.remplir_modules()
        # self.dict_boutons = { 1: ttk.Button(self, text='Gestion Membre', command=self.clic_bouton_membre).grid(
        # row=0, column=0, pady=(20, 0), sticky=tk.E), 2: ttk.Button(self, text='Gestion des projets ERP',
        # command=self.clic_bouton_projets).grid(row=0, column=1, pady=(20, 0), sticky=tk.E), 3: ttk.Button(self,
        # text='Gestion modules', command=self.clic_bouton_modules).grid(row=0, column=2, pady=(20, 0), sticky=tk.E), }
        self.click_button = {
            "propriete": self.clic_bouton_propriete,
            "gestion": self.clic_bouton_membre,
            "inventaire": self.clic_bouton_inventaire,
            "evenement": self.click_bouton_evenement,
            "budget":self.click_bouton_budget(),
            "employe": self.click_bouton_employe,
            "vente_en_ligne": self.click_bouton_vente_en_ligne,
            "plaintes": self.click_bouton_plaintes,
            "materielle": self.clic_bouton_materielle
        }
        self.remplir_vue_gestion()

    def remplir_vue_gestion(self):

        self.data = ("1", "2", "3", "4")
        self.data1 = ("allo", "bigg", "toast")
        # self.listWidt
        #  =int(self.winfo_width()/3)
        # for i in self.controleur.dict_modules:
        #     # if i in self.dict_boutons.keys():
        #     #     pass
        #     pass
        compteur_column = 0
        for i in self.controleur.dict_modules.keys():
            ttk.Button(self, text=i, command=self.click_button[i]).grid(row=0, column=compteur_column,
                                                                        pady=(20, 0), sticky=tk.E)
            compteur_column += 1

        # for i in self.controleur.dict_modules.keys():
        #     ttk.Button(self, text=i, command=dic[i]).grid(row=0, column=0,
        #                                                                                   pady=(20, 0),
        #                                                                                   sticky=tk.E)
        #
        #     if self.controleur.dict_modules[i] == "gestion":
        #         ttk.Button(self, text='Gestion Membre', command=self.clic_bouton_membre).grid(row=0, column=0,
        #                                                                                       pady=(20, 0),
        #                                                                                       sticky=tk.E)
        #     if self.controleur.dict_modules[i] == "propriete":
        #         ttk.Button(self, text='Gestion Membre', command=self.clic_bouton_membre).grid(row=0, column=0,
        #                                                                                       pady=(20, 0),
        #                                                                                       sticky=tk.E)
        #     if self.controleur.dict_modules[i] == "inventaire":
        #         ttk.Button(self, text='Gestion Membre', command=self.clic_bouton_membre).grid(row=0, column=0,
        #                                                                                       pady=(20, 0),
        #                                                                                       sticky=tk.E)
        #     if self.controleur.dict_modules[i] == "evenement":
        #         ttk.Button(self, text='Gestion Membre', command=self.clic_bouton_membre).grid(row=0, column=0,
        #                                                                                       pady=(20, 0),
        #                                                                                       sticky=tk.E)
        #     if self.controleur.dict_modules[i] == "budget":
        #         ttk.Button(self, text='Gestion Membre', command=self.clic_bouton_membre).grid(row=0, column=0,
        #                                                                                       pady=(20, 0),
        #                                                                                       sticky=tk.E)
        #     if self.controleur.dict_modules[i] == "employe":
        #         ttk.Button(self, text='Gestion Membre', command=self.clic_bouton_membre).grid(row=0, column=0,
        #                                                                                       pady=(20, 0),
        #                                                                                       sticky=tk.E)
        #     if self.controleur.dict_modules[i] == "vente_en_ligne":
        #         ttk.Button(self, text='Gestion Membre', command=self.clic_bouton_membre).grid(row=0, column=0,
        #                                                                                       pady=(20, 0),
        #                                                                                       sticky=tk.E)
        #     if self.controleur.dict_modules[i] == "plaintes":
        #         ttk.Button(self, text='Gestion Membre', command=self.clic_bouton_membre).grid(row=0, column=0,
        #                                                                                       pady=(20, 0),
        #                                                                                       sticky=tk.E)
        #     if self.controleur.dict_modules[i] == "materielle":
        #         ttk.Button(self, text='Gestion Membre', command=self.clic_bouton_membre).grid(row=0, column=0,
        #                                                                                       pady=(20, 0),
        #                                                                                       sticky=tk.E)
        #     compteur_column += 1



    def delete_lists(self):
        self.canevas_list.destroy()
        self.bouton_gerer_employe.grid_remove()
        self.bouton_ajouter_membre.grid_remove()
        self.canevas_list = tk.Canvas(self, height=200, width=600, bg='white')
        self.canevas_list.grid(row=1, column=0, columnspan=3, sticky=tk.E)

    def clic_bouton_membre(self):
        self.delete_lists()
        # self.canevas_list = tk.Canvas(self, height=200, bg='white')
        # self.canevas_list.grid(row=1, column=0, columnspan=3, sticky=tk.E)
        # self.lWidth = int(self.canevas_list.winfo_width() / 3)
        self.bouton_ajouter_membre = ttk.Button(self, text='Ajouter Membre',
                                                 command=lambda: self.start_module_gerer_emp(None))
        self.bouton_gerer_employe = ttk.Button(self, text='Gerer Employe', command=self.clic_bouton_gestion_employe)


        #

        self.bouton_ajouter_membre.grid(row=2, column=0, pady=(20, 0), sticky=tk.E)
        self.bouton_gerer_employe.grid(row=2, column=2, pady=(20, 0), sticky=tk.E)
        colonnes = ('Nom', 'Identifiant', 'Permission', 'Rôle')
        self.liste = ttk.Treeview(self.canevas_list, columns=colonnes, show='headings',
                                  selectmode='browse')
        self.canevas_list.create_window(0, 0, window=self.liste, width=200, height=200)
        ttk.Button(self, text='Ajouter Membre',
                   command=lambda: self.start_module_gerer_emp(None)),
        ttk.Button(self, text='Gerer Employe', command=self.clic_bouton_gestion_employe)

        data = []
        # TODO utiliser de vrais employés
        # Ici on append dans le data de faux employés avec la boucle
        a = self.controleur.get_employes_de_compagnie(self.controleur.user_id)
        print(a)

        for n in range(1, 50):
            data.append((f'Employé {n}', f'Identifiant {n}', f'Accès {n}', f'Rôle {n}'))

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

    def populate_list(self):
        pass

    def start_module(self, arg):
        selection = self.liste.selection()
        item = self.liste.item(selection[0])
        record = item['values']
        infos_module = self.dictionnaire_module[record[0]]
        infos_module()

    def start_module_gerer_emp(self, params):
        self.gerer_emp_module = Toplevel()
        vue = VueGererEmp(self, params, self.controleur)
        vue.place(height=500, width=500)
        self.gerer_emp_module.geometry("500x500")
        self.gerer_emp_module.title("Gestion Employé")

    def clic_bouton_gestion_employe(self):
        selection = self.liste.selection()
        if selection:
            item = self.liste.item(selection[0])
            record = item['values']
            self.start_module_gerer_emp(record)

    def fermer_module_emp(self):
        self.gerer_emp_module.destroy()

    def clic_bouton_projets(self):
        # self.canevas_list.delete(self)
        self.delete_lists()
        # self.canevas_list.after(1000)

        self.liste = tk.Listbox(self.canevas_list, selectmode='browse')

        self.list_permission = tk.Listbox(self.canevas_list, selectmode='browse')
        self.list_role = tk.Listbox(self.canevas_list, selectmode='browse')

        for num in self.data1:
            self.liste.insert(END, num)
        self.liste.place(x=25, y=0)

        for num in self.data:
            self.list_permission.insert(END, num)
        self.list_permission.place(x=125, y=0)

        for num in self.data:
            self.list_role.insert(END, num)
        self.list_role.place(x=225, y=0)

    def clic_bouton_modules(self):
        self.delete_lists()

        colonnes = ('Modules',)
        self.liste = ttk.Treeview(self.canevas_list, columns=colonnes, show='headings',
                                  selectmode='browse')
        self.liste.heading('Modules', text='Modules disponibles:')

        data = []
        data.append(('Gestion Budget',))
        data.append(('Gestion Inventaire',))
        data.append(('Gestion Événements',))
        data.append(('Gestion Propriétés',))
        self.liste.column('Modules', anchor='center')
        self.liste.column('Modules', width=600)
        for module in data:
            self.liste.insert('', tk.END, values=module)
        self.liste.place(x=0, y=0)
        self.liste.bind("<Double-1>", self.start_module)

    def clic_bouton_annuler(self):
        self.var_nom.set('')
        self.var_mdp.set('')

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

    def remplir_modules(self):
        self.controleur.get_modules_with_access()

    def clic_bouton_propriete(self):
        pass

    def clic_bouton_inventaire(self):
        pass

    def click_bouton_evenement(self):
        pass

    def click_bouton_employe(self):
        pass

    def click_bouton_vente_en_ligne(self):
        pass

    def click_bouton_plaintes(self):
        pass

    def clic_bouton_materielle(self):
        pass

    def click_bouton_budget(self):
        pass