from traceback import print_exc
from tkinter import Tk
from vue_gestion import VueGestion
from controleur_client import Controleur_Client

class Module_Gestion(Tk):
    def __init__(self):
        super().__init__()
        controleur = Controleur_Client()

        # peut-être éventuellement dans une sous-classe
        vue_gestion = VueGestion(self)
        vue_gestion.grid(row=3, column=3, padx=10, pady=10)
        vue_gestion.set_controleur(controleur)
        controleur.set_vue_gestion(vue_gestion)

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