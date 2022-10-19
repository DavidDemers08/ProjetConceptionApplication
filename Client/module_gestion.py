from traceback import print_exc
from tkinter import Tk

from Client.vue_gestion import VueGestion
from vue import Vue


class ModuleGestion(Tk):
    def __init__(self, parent):
        super().__init__()
        controleur = parent


        # peut-être éventuellement dans une sous-classe
        vue = VueGestion(self)
        vue.grid(row=0, column=0, padx=10, pady=10)
        vue.set_controleur(controleur)
        parent.set_vue(vue)
