import tkinter as tk
from abc import ABC, abstractmethod
from tkinter import ttk

import Utils.utils
from Serveur.DAO.dao import Dao


class Vue(ttk.Frame, ABC):
    def __init__(self, parent, row: int, column: int, padx: int, pady: int):
        super().__init__(parent)
        self.parent = parent
        self.controleur = None
        self.row = row
        self.column = column
        self.padx = padx
        self.pady = pady
        self.grid(row=self.row, column=self.column, padx=self.padx, pady=self.pady)


    def set_controleur(self, controleur):
        self.controleur = controleur

    def vider_frame(self):
        for widget in self.winfo_children():
            widget.destroy()

    @abstractmethod
    def remplir_vue(self):
        pass
