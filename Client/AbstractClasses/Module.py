from abc import ABC, abstractmethod
from tkinter import Tk


class Module(ABC):

    def __init__(self, controleur, master_frame):
        self.controleur = controleur
        self.master_frame = master_frame
        self.vue = None

    def show_vue(self):
        self.vue = self.set_vue()
        self.vue.set_controleur(self.controleur)
        self.vue.remplir_vue()
        #self.controleur.set_vue_gestion(self.vue)

    @abstractmethod
    def set_vue(self):
        # return l'inner class qui est un extend de Vue
        # Doit passer les params du grid dans l'instanciation de la Vue
        # Voir classe init de la classe abstract vue pour comprendre
        pass

    def vider_vue(self):
        self.vue.vider_frame()


