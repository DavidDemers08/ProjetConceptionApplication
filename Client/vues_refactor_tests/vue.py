import tkinter as tk
from abc import ABC, abstractmethod
from tkinter import ttk

import Utils.utils
from Serveur.DAO.dao import Dao


class Vue(ttk.Frame, ABC):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.controleur = None


    def set_controleur(self, controleur):
        self.controleur = controleur

    def vider_frame(self):
        for widget in self.winfo_children():
            widget.destroy()

    @abstractmethod
    def remplir_vue(self):
        pass




