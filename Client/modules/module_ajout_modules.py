from tkinter import Tk
from traceback import print_exc

from Client.vues.vue_ajout_modules import VueAjoutModules
from Client.controleurclient import ControleurClient


class ModuleAjoutModules(Tk):
    def __init__(self):
        super().__init__()
        controleur = ControleurClient()
        vue_ajout_modules = VueAjoutModules(self)
        vue_ajout_modules.grid(row=3, column=3, padx=10, pady=10)
        vue_ajout_modules.set_controleur(controleur)
        controleur.set_vue(vue_ajout_modules)


def main():
    try:
        module = ModuleAjoutModules()
        module.mainloop()
    except:
        print_exc()
        return 1
    return 0


if __name__ == '__main__':
    quit(main())