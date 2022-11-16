from traceback import print_exc
from tkinter import ttk
import tkinter as tk
from Client.AbstractClasses.Module import Module
from Client.AbstractClasses.Vue import Vue
from Utils.Table import Table


class ModuleAjoutModules(Module):

    def __init__(self, controleur):
        super().__init__(controleur)

    def set_vue(self):
        return ModuleAjoutModules.VueAjoutModules(self, row=3, column=3, padx=10, pady=10)

    class VueAjoutModules(Vue):
        def __init__(self, parent, row: int, column: int, padx: int, pady: int):
            super().__init__(parent, row, column, padx, pady)

            self.liste_module = []
            ###test pour remplir liste module
            self.liste_module.append(["nom module 1", "42.45", "2001/9/11"])
            self.liste_module.append(["nom module 2", "4s2.45", "2001/91/11"])
            self.liste_module.append(["nom module 3", "42.4a5", "20011/9/11"])
            self.table = Table(vue=self, lines_array=self.liste_module, modifiable_rows=False)

        def remplir_vue(self):
            self.heading = ttk.Label(self, text='Ajout de Module', style='Heading.TLabel')
            self.heading.grid(column=0, row=0, columnspan=2, pady=5, sticky=tk.N)

            self.module = ttk.Label(self, text="Module")
            self.module.grid(column=0, row=1, sticky=tk.W, padx=50)
            self.prix = ttk.Label(self, text="Prix")
            self.prix.grid(column=1, row=1, sticky=tk.W, padx=50)
            self.exp_date = ttk.Label(self, text="Date d'expiration")
            self.exp_date.grid(column=2, row=1, sticky=tk.W, padx=50)

            self.remplir_grid_module()
            self.table.create()
            if self.table.modifiable_rows:
                self.parent.bind('<Return>', lambda e: self.update_liste_modules())

        def update_liste_modules(self):
            self.liste_module = self.table.update_lines()




def main():
    try:
        controleur = None
        module = ModuleAjoutModules(controleur)
        module.show_vue()
        module.mainloop()
    except:
        print_exc()
        return 1
    return 0


if __name__ == '__main__':
    quit(main())