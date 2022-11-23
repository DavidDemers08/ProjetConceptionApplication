from traceback import print_exc
from tkinter import Tk

from Client.controleurclient import ControleurClient
from Client.vues.vue_gestion import VueGestion
from Client.vues.vue_gerer_emp import VueGererEmp


class Module_Gestion(Tk):
    def __init__(self):
        super().__init__()
        self.controleur = ControleurClient()
        vue_gestion = VueGestion(self, self.controleur)
        vue_gestion.grid(row=3, column=3, padx=10, pady=10)
        self.controleur.set_vue_gestion(vue_gestion)


def main():
    try:
        module = Module_Gestion()
        module.mainloop()
    except:
        print_exc()
        return 1
    return 0


if __name__ == '__main__':
    quit(main())