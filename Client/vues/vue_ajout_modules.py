
import tkinter as tk
from tkinter import ttk
from Utils.Table import Table


class VueAjoutModules(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.controleur = None
        self.liste_module = []
        ###test pour remplir liste module
        self.liste_module.append(("nom module 1", "42.45", "2001/9/11"))
        self.liste_module.append(("nom module 2", "4s2.45", "2001/91/11"))
        self.liste_module.append(("nom module 3", "42.4a5", "20011/9/11"))
        self.parent = parent
        self.remplir_vue()

    def set_controleur(self, controleur):
        self.controleur = controleur

    def vider_frame(self):
        for widget in self.winfo_children():
            widget.destroy()

    def remplir_vue(self):
        table = Table(vue=self.parent, lines_array=self.liste_module, modifiable_rows=True)
