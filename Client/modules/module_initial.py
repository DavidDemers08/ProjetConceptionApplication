from traceback import print_exc
from tkinter import Tk

from Client.controleur_client import Controleur_Client
from Client.vues.vue_initiale import Vue


class Module(Tk):
    def __init__(self):
        super().__init__()
        controleur = Controleur_Client()

        vue = Vue(self)
        vue.grid(row=0, column=0, padx=10, pady=10)
        vue.set_controleur(controleur)
        controleur.set_vue(vue)
        controleur.creation_modules()


def main():
    try:
        module = Module()
        module.mainloop()
    except:
        print_exc()
        return 1
    return 0


if __name__ == '__main__':
    quit(main())
