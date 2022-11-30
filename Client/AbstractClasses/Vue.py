import tkinter as tk
from abc import ABC, abstractmethod
from tkinter import ttk

import Utils.utils
from Serveur.DAO.dao import Dao


class Vue(ABC):
    def __init__(self, parent, master_frame, row: int, column: int, padx: int, pady: int):
        self.parent = parent
        self.controleur = None
        self.row = row
        self.column = column
        self.padx = padx
        self.pady = pady
        self.master_frame = master_frame
        self.master_frame.grid(row=self.row, column=self.column, padx=self.padx, pady=self.pady)

    def set_controleur(self, controleur):
        self.controleur = controleur

    def vider_frame(self):
        for widget in self.master_frame.winfo_children():
            widget.destroy()

    @abstractmethod
    def remplir_vue(self):
        pass
