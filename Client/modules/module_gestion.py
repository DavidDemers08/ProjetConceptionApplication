from tkinter import Tk

from traceback import print_exc

from Client.vues.vue_gestion_OLD import VueGestion


class ModuleGestion(Tk):
    def __init__(self, parent):
        super().__init__()
        controleur = parent

        vue = VueGestion(self, controleur)
        vue.grid(row=0, column=0, padx=10, pady=10)
        parent.set_vue(vue)


def main():
    try:
        controleur = None
        module = ModuleGestion(controleur)
        module.mainloop()
    except:
        print_exc()
        return 1
    return 0


if __name__ == '__main__':
    quit(main())
