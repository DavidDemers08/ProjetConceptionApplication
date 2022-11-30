from traceback import print_exc

from Client.AbstractClasses.Module import Module
from Client.AbstractClasses.Vue import Vue

import tkinter as tk
from tkinter import *
from tkinter import ttk
from Client.vues.vue_gerer_emp import VueGererEmp
from Client.modules.module_paiement import ModulePaiement


class ModuleMenu(Module):

    def __init__(self, controleur, master_frame):
        super().__init__(controleur, master_frame)

    def set_vue(self):
        return ModuleMenu.VueGestion(self, self.master_frame, row=0, column=0, padx=10, pady=10)

    class VueGestion(Vue):

        def __init__(self, parent, master_frame, row: int, column: int, padx: int, pady: int):
            super().__init__(parent, master_frame, row, column, padx, pady)

            self.click_button = {
                "propriete": self.clic_bouton_propriete,
                "gestion": self.clic_bouton_membre,
                "inventaire": self.clic_bouton_inventaire,
                "evenement": self.click_bouton_evenement,
                "budget": self.click_bouton_budget,
                "employe": self.click_bouton_employe,
                "vente_en_ligne": self.click_bouton_vente_en_ligne,
                "plaintes": self.click_bouton_plaintes,
                "materielle": self.clic_bouton_materielle
            }

        def remplir_vue(self):
            self.remplir_modules()
            # self.listWidt
            #  =int(self.winfo_width()/3)
            # for i in self.controleur.dict_modules:
            #     # if i in self.dict_boutons.keys():
            #     #     pass
            #     pass
            compteur_column = 0
            for i in self.controleur.dict_modules_idx.keys():
                ttk.Button(self.master_frame, text=i, command=self.click_button[i]).grid(row=0, column=compteur_column,
                                                                                         pady=(20, 0), sticky=tk.E)
                compteur_column += 1

        def delete_lists(self):
            self.canevas_list.destroy()
            self.bouton_gerer_employe.grid_remove()
            self.bouton_ajouter_membre.grid_remove()
            self.canevas_list = tk.Canvas(self.master_frame, height=200, width=600, bg='white')
            self.canevas_list.grid(row=1, column=0, columnspan=3, sticky=tk.E)

        def clic_bouton_membre(self):
            self.controleur.set_module("GestionMembre")


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

        def set_vue_module(self, module):

            self.controleur.set_module(module)


def main():
    try:
        controleur = None
        module = ModuleMenu(controleur)
        module.show_vue()
        module.mainloop()
    except:
        print_exc()
        return 1
    return 0


if __name__ == '__main__':
    quit(main())
