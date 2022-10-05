import tkinter as tk
from tkinter import *
from tkinter import ttk


class VueGestion(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        #self.controleur = None
        self.remplir_vue_gestion()



    def set_controleur(self, controleur):
        self.controleur = controleur

    def remplir_vue_gestion(self):

        self.data =("1","2","3","4")
        self.data1 = ("allo", "bigg","toast")
        #self.listWidt
          #  =int(self.winfo_width()/3)
        self.bouton_gestion_membre = ttk.Button(self, text='Gestion Membre', command=self.clic_bouton_membre)
        self.bouton_gestion_membre.grid(row=0, column=0, pady=(20, 0), sticky=tk.E)

        self.bouton_gestion_projet = ttk.Button(self, text='Gestion des projets ERP', command=self.clic_bouton_projets)
        self.bouton_gestion_projet.grid(row=0, column=1, pady=(20, 0), sticky=tk.E)

        self.bouton_gestion_modules = ttk.Button(self, text='Gestion modules', command=self.clic_bouton_modules)
        self.bouton_gestion_modules.grid(row=0, column=2, pady=(20, 0), sticky=tk.E)

        self.canevas_list = tk.Canvas(self,height=200, bg= 'white')

        self.canevas_list.grid(row = 1, column=0, columnspan=3, sticky=tk.E)
        self.lWidth = int(self.canevas_list.winfo_width() /3)


        self.bouton_ajouter_membre = ttk.Button(self, text='Ajouter Membre', command=self.clic_bouton_ajout_membre)
        self.bouton_ajouter_membre.grid(row=2, column=0, pady=(20, 0),sticky=tk.E)

        self.bouton_gerer_employe = ttk.Button(self, text='Gerer Employe', command=self.clic_bouton_gestion_employe)
        self.bouton_gerer_employe.grid(row=2, column=2, pady=(20, 0), sticky=tk.E)
        #self.canevas_list.create_window(0, 0, window=self.list, width=200, height=200)



    def delete_lists(self):
        self.canevas_list.destroy()
        self.canevas_list = tk.Canvas(self, height=200, bg='white')
        self.canevas_list.grid(row=1, column=0, columnspan=3, sticky=tk.E)

    def clic_bouton_membre(self):
        self.delete_lists()
        print(self.canevas_list.winfo_width()+1)
        self.list_identifiant = tk.Listbox(self.canevas_list, selectmode='browse' )
        self.list_permission = tk.Listbox(self.canevas_list, selectmode='browse' )
        self.list_role = tk.Listbox(self.canevas_list, selectmode='browse' )

        for num in self.data:
            self.list_identifiant.insert(END, num)
        self.list_identifiant.place(x=25, y=0)

        for num in self.data1:
            self.list_permission.insert(END, num)
        self.list_permission.place(x=125, y=0)

        for num in self.data:
            self.list_role.insert(END, num)
        self.list_role.place(x=225, y=0)

    def populate_list(self):
        pass

    def clic_bouton_ajout_membre(self):
        pass

    def clic_bouton_gestion_employe(self):
        pass
    def clic_bouton_projets(self):
        #self.canevas_list.delete(self)
        self.delete_lists()
        #self.canevas_list.after(1000)

        self.list_identifiant = tk.Listbox(self.canevas_list, selectmode='browse')
        self.list_permission = tk.Listbox(self.canevas_list, selectmode='browse')
        self.list_role = tk.Listbox(self.canevas_list, selectmode='browse')

        for num in self.data1:
            self.list_identifiant.insert(END, num)
        self.list_identifiant.place(x=25, y=0)

        for num in self.data:
            self.list_permission.insert(END, num)
        self.list_permission.place(x=125, y=0)

        for num in self.data:
            self.list_role.insert(END, num)
        self.list_role.place(x=225, y=0)


    def clic_bouton_modules(self):
        # self.canevas_list.delete(self)
        self.delete_lists()
        # self.canevas_list.after(1000)
        self.list_role = tk.Listbox(self.canevas_list, selectmode='browse')

        for num in self.data:
            self.list_role.insert(END, num)
        self.list_role.place(x=0, y=0)

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

    #def list_box(self):
       # self.w = Listbox()