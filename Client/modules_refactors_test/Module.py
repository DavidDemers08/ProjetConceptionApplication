from abc import ABC, abstractmethod
from traceback import print_exc
from tkinter import Tk
from Client.vues_refactor_tests.vue import Vue


class Module(Tk, ABC):
    def __init__(self, controleur):
        super().__init__()
        self.controleur = controleur
        self.vue = None


    def show_vue(self):
        self.vue = self.set_vue()
        self.vue.grid(row=3, column=3, padx=10, pady=10)
        self.vue.set_controleur(self.controleur)
        self.controleur.set_vue_gestion(self.vue)

    @abstractmethod
    def set_vue(self):
        # return classe Vue
        pass