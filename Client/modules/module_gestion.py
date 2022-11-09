from tkinter import Tk

#from Client.controleur_client import Controleur_Client
from Client.vues.vue_gestion import VueGestion


class ModuleGestion(Tk):
    def __init__(self, parent ):
        super().__init__()
        controleur = parent

        vue = VueGestion(self, controleur)
        vue.grid(row=0, column=0, padx=10, pady=10)
        parent.set_vue(vue)
        print(controleur.username)
