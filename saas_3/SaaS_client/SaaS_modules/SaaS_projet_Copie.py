## -*- Encoding: UTF-8 -*-
import urllib.request
import urllib.parse 
import json 

from tkinter import *
from tkinter.simpledialog import *
from tkinter import ttk

import sys

class Vue():
    def __init__(self,parent):
        self.parent=parent
        self.root=Tk()
        self.cadreapp=Frame(self.root)
        self.canevas=Canvas(self.cadreapp,width=800,height=600)
        self.canevas.create_text(400,300,anchor=CENTER,text="Bienvenue a SaaS PROJET")
        self.canevas.pack()
        self.cadreapp.pack()

class Controleur():
    def __init__(self):
        self.vue=Vue(self)
        self.vue.root.mainloop()

if __name__ == '__main__':
    c=Controleur()