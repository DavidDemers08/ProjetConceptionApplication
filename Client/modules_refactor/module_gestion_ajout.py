from traceback import print_exc
from Client.AbstractClasses.Module import Module
from Client.AbstractClasses.Vue import Vue
import tkinter as tk
from tkinter import *
from tkinter import ttk


class Module_Gestion(Module):

    def __init__(self, controleur):
        super().__init__(controleur)

    def set_vue(self):
        return Module_Gestion.VueGestionAjout(self, row=9, column=4, padx=10, pady=10)

    class VueGestionAjout(Vue):

        def __init__(self, parent, row: int, column: int, padx: int, pady: int):
            super().__init__(parent, row, column, padx, pady)

        def remplir_vue(self):
            self.photo_pwd = PhotoImage(file=r"..\Media\Images\show_pwd.png", width=20, height=20)
            self.titre_module = ttk.Label(self, text='Ajout Membre')
            self.titre_module.grid(row=0, column=1, sticky=tk.W)
            self.label_nom = ttk.Label(self, text='Nom :', width=25)
            self.label_nom.grid(row=1, column=0, pady=(20, 0), sticky=tk.E)
            self.entry_nom = ttk.Entry(self, )
            self.entry_nom.grid(row=1, column=2, pady=(20, 0), sticky=tk.E)
            self.label_prenom = ttk.Label(self, text='Prenom :', width=25)
            self.label_prenom.grid(row=2, column=0, pady=(20, 0), sticky=tk.E)
            self.entry_prenom = ttk.Entry(self)
            self.entry_prenom.grid(row=2, column=2, pady=(20, 0), sticky=tk.E)
            self.label_identifiant = ttk.Label(self, text='Identifiant :', width=25)
            self.label_identifiant.grid(row=3, column=0, pady=(20, 0), sticky=tk.E)
            self.entry_indentifiant = ttk.Entry(self)
            self.entry_indentifiant.grid(row=3, column=2, pady=(20, 0), sticky=tk.E)
            self.label_mdp = ttk.Label(self, text='Mot de passe :', width=25)
            self.label_mdp.grid(row=4, column=0, pady=(20, 0), sticky=tk.E)
            self.entry_mdp = ttk.Entry(self, show='*')
            self.entry_mdp.grid(row=4, column=2, pady=(20, 0), sticky=tk.E)
            self.view_mdp = ttk.Button(self, image=self.photo_pwd)
            self.view_mdp.grid(row=4, column=3, sticky=tk.E)

            self.label_confirmation_mdp = ttk.Label(self, text='Confirmation mot de passe:', width=25)
            self.label_confirmation_mdp.grid(row=5, column=0, pady=(20, 0), sticky=tk.E)
            self.entry_confirmation_mdp = ttk.Entry(self, show='*')
            self.entry_confirmation_mdp.grid(row=5, column=2, pady=(20, 0), sticky=tk.E)
            self.view_mdp_conf = ttk.Button(self, image=self.photo_pwd)
            self.view_mdp_conf.grid(row=5, column=3, sticky=tk.E)

            self.label_permission = ttk.Label(self, text='Permission:', width=25)
            self.label_permission.grid(row=6, column=0, pady=(20, 0), sticky=tk.E)
            self.entry_permisson = ttk.Entry(self)
            self.entry_permisson.grid(row=6, column=2, pady=(20, 0), sticky=tk.E)

            self.label_titre = ttk.Label(self, text='Titre :', width=25)
            self.label_titre.grid(row=7, column=0, pady=(20, 0), sticky=tk.E)
            self.entry_titre = ttk.Entry(self)
            self.entry_titre.grid(row=7, column=2, pady=(20, 0), sticky=tk.E)

            self.label_genre = ttk.Label(self, text='Genre :', width=25)
            self.label_genre.grid(row=8, column=0, pady=(20, 0), sticky=tk.E)
            self.current_var = tk.StringVar()

            self.combo_genre = ttk.Combobox(self, textvariable=self.current_var)
            self.combo_genre['values'] = ('********', 'Masculin', 'Feminin', 'Non-binaire', 'Prefere ne pas repondre')
            self.combo_genre.current(0)
            self.combo_genre['state'] = 'readonly'
            self.combo_genre.grid(row=8, column=2, pady=(20, 0), sticky=tk.E)
            self.current_value = self.current_var.get()

            self.entry_indetifiant = ttk.Entry(self)
            self.entry_indetifiant.grid(row=3, column=2, pady=(20, 0), sticky=tk.E)

            self.bouton_gestion_membre = ttk.Button(self, text='Sauvegarder', command=self.get_data)
            self.bouton_gestion_membre.grid(row=9, column=2, pady=(20, 0), sticky=tk.E)

            self.bouton_gestion_projet = ttk.Button(self, text='Annuler', command=self.clic_anuller)
            self.bouton_gestion_projet.grid(row=9, column=0, pady=(20, 0), sticky=tk.W)

        def delete_lists(self):
            self.canevas_list.destroy()
            self.canevas_list = tk.Canvas(self, height=200, bg='white')
            self.canevas_list.grid(row=1, column=0, columnspan=3, sticky=tk.E)

        def clic_sauvegarde(self):
            self.open_popup()

        def get_data(self):
            info = {}

            info['nom'] = self.entry_nom.get()

            info['prenom'] = self.entry_prenom.get()
            info['identifiant'] = self.entry_indentifiant.get()
            info['mdp'] = self.entry_mdp.get()
            info['confirmer_mdp'] = self.entry_confirmation_mdp.get()
            info['permission'] = self.entry_permisson.get()
            info['titre'] = self.entry_titre.get()
            info['genre'] = self.combo_genre.get()

            self.validate_info(info)
            print(info)

        def validate_info(self, info):
            for key in info.keys():
                if info[key] == '':
                    pass
                else:
                    print(info[key])

        def open_popup(self):
            # popup = tk.messagebox.showinfo('Sauvegarde','Sauvegarde effectue avec succes')
            popup = tk.Tk()
            popup.geometry('300x100')
            popup.wm_title("Sauvegarde")

            label = ttk.Label(popup, text='Sauvegarde effectue avec succes', background='black', foreground='white',
                              justify=tk.CENTER)
            label.pack()
            B1 = ttk.Button(popup, text="Okay", command=popup.destroy)
            B1.pack()

        def clic_anuller(self):
            pass

        def clic_bouton_annuler(self):
            self.var_nom.set('')
            self.var_mdp.set('')

        def clic_bouton_modules(self):
            # self.canevas_list.delete(self)
            self.delete_lists()
            # self.canevas_list.after(1000)
            self.list_role = tk.Listbox(self.canevas_list, selectmode='browse')

            for num in self.data:
                self.list_role.insert(END, num)
            self.list_role.place(x=0, y=0)

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

        # def list_box(self):
        # self.w = Listbox()




def main():
    try:
        controleur = None
        module = Module_Gestion(controleur)
        module.show_vue()
        module.mainloop()
    except:
        print_exc()
        return 1
    return 0


if __name__ == '__main__':
    quit(main())
