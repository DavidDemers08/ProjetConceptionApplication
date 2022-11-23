from traceback import print_exc
from tkinter import Tk
from Client.vues.vue_gestion_inventaire_vehicules import VueGestionInventaireVehicules
from Client.controleurclient import ControleurClient

class Module_Gestion(Tk):
    def __init__(self):
        super().__init__()
        controleur = ControleurClient()

        # peut-être éventuellement dans une sous-classe
        vue_gestion_inventaire_vehicules = VueGestionInventaireVehicules(self)
        vue_gestion_inventaire_vehicules.grid(row=9, column=5, padx=10, pady=10)
        vue_gestion_inventaire_vehicules.set_controleur(controleur)
        controleur.set_vue_gestion(vue_gestion_inventaire_vehicules)

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