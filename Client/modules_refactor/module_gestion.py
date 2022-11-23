from traceback import print_exc
from Client.AbstractClasses.Module import Module
from Client.AbstractClasses.Vue import Vue
import tkinter as tk
from tkinter import *
from tkinter import ttk

from Client.modules_refactor.module_paiement import ModulePaiement
from Client.vues.vue_gerer_emp import VueGererEmp


class ModuleGestion(Module):

    def __init__(self, parent):
        super().__init__(parent)

    def set_vue(self):
        return ModuleGestion.VueGestion(self, row=0, column=0, padx=10, pady=10)


    class VueGestion(Vue):

        def __init__(self, parent, row: int, column: int, padx: int, pady: int):
            super().__init__(parent, row, column, padx, pady)

            self.dictionnaire_module = {
                "Gestion Budget": ModulePaiement,
                "Gestion Inventaire": ModulePaiement,
                "Gestion Événements": ModulePaiement,
                "Gestion Propriétés": ModulePaiement
            }


        def remplir_vue(self):

            self.data = ("1", "2", "3", "4")
            self.data1 = ("allo", "bigg", "toast")

            self.bouton_gestion_membre = ttk.Button(self, text='Gestion Membre', command=self.clic_bouton_membre)
            self.bouton_gestion_membre.grid(row=0, column=0, pady=(20, 0), sticky=tk.E)

            self.bouton_gestion_projet = ttk.Button(self, text='Gestion des projets ERP',
                                                    command=self.clic_bouton_projets)
            self.bouton_gestion_projet.grid(row=0, column=1, pady=(20, 0), sticky=tk.E)

            self.bouton_gestion_modules = ttk.Button(self, text='Gestion modules', command=self.clic_bouton_modules)
            self.bouton_gestion_modules.grid(row=0, column=2, pady=(20, 0), sticky=tk.E)

            self.canevas_list = tk.Canvas(self, height=200, bg='white')

            self.canevas_list.grid(row=1, column=0, columnspan=3, sticky=tk.E)
            self.lWidth = int(self.canevas_list.winfo_width() / 3)

            self.bouton_ajouter_membre = ttk.Button(self, text='Ajouter Membre',
                                                    command=lambda: self.start_module_gerer_emp(None))
            self.bouton_gerer_employe = ttk.Button(self, text='Gerer Employe', command=self.clic_bouton_gestion_employe)



        def delete_lists(self):
            self.canevas_list.destroy()
            self.bouton_gerer_employe.grid_remove()
            self.bouton_ajouter_membre.grid_remove()
            self.canevas_list = tk.Canvas(self, height=200, width=400, bg='white')
            self.canevas_list.grid(row=1, column=0, columnspan=3, sticky=tk.E)

        def clic_bouton_membre(self):
            self.delete_lists()
            self.bouton_ajouter_membre.grid(row=2, column=0, pady=(20, 0), sticky=tk.E)
            self.bouton_gerer_employe.grid(row=2, column=2, pady=(20, 0), sticky=tk.E)
            colonnes = ('Nom', 'Identifiant', 'Permission', 'Rôle')
            self.liste = ttk.Treeview(self.canevas_list, columns=colonnes, show='headings',
                                      selectmode='browse')
            data = []
            # TODO utiliser de vrais employés
            # Ici on append dans le data de faux employés avec la boucle
            for n in range(1, 50):
                data.append((f'Employé {n}', f'Identifiant {n}', f'Accès {n}', f'Rôle {n}'))
            self.liste.heading('Nom', text='Nom')
            self.liste.heading('Identifiant', text='Identifiant')
            self.liste.heading('Permission', text='Permission')
            self.liste.heading('Rôle', text='Rôle')

            self.liste.column('Rôle', anchor='center', stretch=NO, width=110)
            self.liste.column('Identifiant', anchor='center', stretch=NO, width=110)
            self.liste.column('Permission', anchor='center', stretch=NO, width=110)
            self.liste.column('Nom', anchor='center', stretch=NO, width=110)

            for emp in data:
                self.liste.insert('', tk.END, values=emp)
            # self.liste.place(x=0, y=0)
            self.liste.grid(row=2, column=0, columnspan=3, sticky=tk.E)

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
            vue = VueGererEmp(self, params)
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
            self.delete_lists()
            colonnes = ('Compagnie', 'Projets', 'Date de Fin')
            self.liste = ttk.Treeview(self.canevas_list, columns=colonnes, show='headings',
                                      selectmode='browse')
            data = []
            # TODO utiliser de vrais employés
            # Ici on append dans le data de faux employés avec la boucle
            for n in range(1, 20):
                data.append((f'Employé {n}', f'Identifiant {n}', f'Accès {n}'))

            self.liste.heading('Compagnie', text='Compagnie')
            self.liste.heading('Projets', text='Projets')
            self.liste.heading('Date de Fin', text='Date de Fin')
            self.liste.column('Compagnie', anchor='center', stretch=NO, width=120)
            self.liste.column('Projets', anchor='center', stretch=NO, width=120)
            self.liste.column('Date de Fin', anchor='center', stretch=NO, width=120)

            for emp in data:
                self.liste.insert('', tk.END, values=emp)
            self.liste.grid(row=2, column=0, columnspan=3, sticky=tk.E)

        def clic_bouton_modules(self):
            self.delete_lists()

            colonnes = ('Modules')
            self.liste = ttk.Treeview(self.canevas_list, columns=colonnes, show='headings',
                                      selectmode='browse')
            self.liste.heading('Modules', text='Modules disponibles:')

            data = []
            data.append(('Gestion Budget',))
            data.append(('Gestion Inventaire',))
            data.append(('Gestion Événements',))
            data.append(('Gestion Propriétés',))
            self.liste.column('Modules', anchor='center')
            self.liste.column('Modules', width=300)
            for module in data:
                self.liste.insert('', tk.END, values=module)
            self.liste.grid(row=2, column=0, columnspan=2, sticky=tk.N)
            # self.liste.bind("<Double-1>", self.start_module)

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





def main():
    try:
        controleur = None
        module = ModuleGestion(controleur)
        module.show_vue()
        module.mainloop()
    except:
        print_exc()
        return 1
    return 0


if __name__ == '__main__':
    quit(main())
