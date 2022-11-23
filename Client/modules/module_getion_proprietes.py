from traceback import print_exc
from tkinter import Tk
from Client.vues.vue_gestion_proprietes import VueGestionProprietes
#from vue_gerer_emp import VueGererEmp
from Client.controleurclient import ControleurClient

class ModuleGestionProprietes(Tk):
    def __init__(self):
        super().__init__()
        self.controleur = ControleurClient()

        vue = VueGestionProprietes(self)
        vue.grid(row=0, column=0)
        vue.set_controleur(self.controleur)
        self.controleur.set_vue_gestion(vue)

def main():
    try:
        module = ModuleGestionProprietes()
        module.mainloop()
    except:
        print_exc()
        return 1
    return 0

if __name__ == '__main__':
    quit(main())