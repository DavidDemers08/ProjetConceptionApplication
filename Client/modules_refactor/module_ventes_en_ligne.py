from traceback import print_exc
from Client.AbstractClasses.Module import Module
from Client.AbstractClasses.Vue import Vue
import tkinter as tk
from tkinter import ttk
from Utils.fonction_util_vue import VueGen


class Module_Ventes_En_ligne(Module):

    def __init__(self, controleur, master_frame):
        super().__init__(controleur, master_frame)

    def set_vue(self):
        return Module_Ventes_En_ligne.VueOnlineSales(self, self.master_frame, row=6, column=5, padx=10, pady=10)

    class VueOnlineSales(Vue):

        def __init__(self, parent, master_frame, row: int, column: int, padx: int, pady: int):
            super().__init__(parent, master_frame, row, column, padx, pady)

        def remplir_vue(self):
            self.label_tittle = ttk.Label(self.master_frame, text='Ventes en ligne')
            self.label_tittle.grid(row=0, column=1, columnspan=2)
            VueGen.generate_button(self.master_frame, 'create_order', 'Faire une commande', [25, None], [1, 1], [3, None], None)
            VueGen.generate_button(self.master_frame, 'launch_verify_order', 'Verifier une commande', [25, None], [3, 1], [3, None],
                                   None)
            VueGen.generate_button(self.master_frame, 'complete_order', 'Completer une commande', [25, None], [5, 1], [3, None],
                                   None)
            VueGen.generate_button(self.master_frame, 'back', 'Retour', [25, None], [7, 1], [3, None], None)

        def remplir_vue_faire_commande(self):
            UNIT_OPTIONS = [
                "Jan",
                "Feb",
                "Mar"
            ]  # etc

            PAYMENT_OPTIONS = [
                "Visa",
                "Mastercard",
                "American Express",
                "Debit",
                "Cash"
            ]

            self.unit_options = tk.StringVar(self.master_frame)
            self.unit_options.set(UNIT_OPTIONS[0])  # default value

            self.payment_options = tk.StringVar(self.master_frame)
            self.payment_options.set(PAYMENT_OPTIONS[0])

            self.tittle_label = ttk.Label(self.master_frame, text='Faire une commande')
            self.tittle_label.grid(row=0, column=1)

            VueGen.generate_label(self.master_frame, 'unit_type', "Type dunité", 20, 2, "groove", tk.CENTER, [1, 0], [None, None])
            VueGen.generate_label(self.master_frame, 'price', "Prix", 20, 2, "groove", tk.CENTER, [2, 0], [None, None])

            self.unit_options_dropdown = ttk.OptionMenu(self.master_frame, self.unit_options, *UNIT_OPTIONS, )
            self.unit_options_dropdown.grid(row=1, column=2, pady=(20, 0), columnspan=2)

            self.unit_price = ttk.Label(self.master_frame, text="prixUnite", width=20, borderwidth=2, relief="groove")
            self.unit_price.config(anchor=tk.CENTER)
            self.unit_price.grid(row=2, column=2, pady=(20, 0), columnspan=2)

            VueGen.generate_label(self.master_frame, 'date', "Date", 20, 2, "groove", tk.CENTER, [3, 0], [None, None])

            self.date_value = ttk.Label(self.master_frame, text="dateNow", width=20, borderwidth=2, relief="groove")
            self.date_value.config(anchor=tk.CENTER)
            self.date_value.grid(row=3, column=2, pady=(20, 0), columnspan=2)

            VueGen.generate_label(self.master_frame, 'buyer', "Acheteur", 20, 2, "groove", tk.CENTER, [4, 0], [None, None])

            self.buyer_value = ttk.Entry(self.master_frame, width=20, )
            self.buyer_value.grid(row=4, column=2, pady=(20, 0), columnspan=2)

            VueGen.generate_label(self.master_frame, 'payment', "Paiement", 20, 2, "groove", tk.CENTER, [5, 0], [None, None])

            self.payment_options_dropdown = ttk.OptionMenu(self.master_frame, self.payment_options, *PAYMENT_OPTIONS)
            self.payment_options_dropdown.grid(row=5, column=2, pady=(20, 0), columnspan=2)

            VueGen.generate_button(self.master_frame, 'order', 'Confirmer commande', [30, None], [6, 0], [2, None], None)
            VueGen.generate_button(self.master_frame, 'back', 'Retour', [None, None], [6, 2], [2, None], None)

        def remplir_vue_verifier_commande(self):
            colonnes = ('Nom', 'Permission', 'Rôle')
            self.label_tittle = ttk.Label(self.master_frame, text='Verifier commande')
            self.label_tittle.grid(row=0, column=2, columnspan=2)

            VueGen.generate_label(self.master_frame, 'order_number', "Numero de Commande", 25, 2, "groove", tk.CENTER, [2, 1],
                                  [None, None])

            VueGen.generate_button(self.master_frame, 'back', 'Retour', [25, None], [6, 1], [3, None], None)

            colonnes = ('Date', 'Acheté', 'Unité', 'État')
            self.liste = ttk.Treeview(self.master_frame, columns=colonnes, show='headings',
                                      selectmode='browse')

            self.liste.heading('Date', text='Date')
            self.liste.heading('Acheté', text='Acheté par :')
            self.liste.heading('Unité', text='Unité')
            self.liste.heading('État', text='État')

            self.liste.column('Date', width=120, anchor=tk.W)
            self.liste.column('Acheté', width=120, anchor=tk.W)
            self.liste.column('Unité', width=120, anchor=tk.W)
            self.liste.column('État', width=160, anchor=tk.W)

            data = []
            for n in range(1, 30):
                data.append((f'Date {n}', f'Acheté {n}', f'Unité {n}', f'État {n}'))

            for emp in data:
                self.liste.insert('', tk.END, values=emp)
            self.liste.grid(row=4, column=0, columnspan=5, pady=(20, 0))

            self.buyer_value = ttk.Entry(self.master_frame, width=20, )
            self.buyer_value.grid(row=2, column=4, pady=(20, 0))

        def remplir_vue_finaliser_commande(self):
            self.label_tittle = ttk.Label(self.master_frame, text='Finaliser une commande')
            self.label_tittle.grid(row=0, column=0, columnspan=5, sticky=tk.N)

            VueGen.generate_label(self.master_frame, 'order_number', "Numero de Commande", 25, 2, "groove", tk.CENTER, [1, 0],
                                  [None, None])

            self.order_number_value = ttk.Label(self.master_frame, text="#Order", width=25, borderwidth=2, relief="groove")
            self.order_number_value.config(anchor=tk.CENTER)
            self.order_number_value.grid(row=1, column=3, pady=(20, 0))

            VueGen.generate_label(self.master_frame, 'order_info', "Valider Information", 25, 2, "groove", tk.CENTER, [3, 0],
                                  [None, None])

            colonne = ('Info', 'Description')
            self.liste = ttk.Treeview(self.master_frame, columns=colonne, show='headings',
                                      selectmode='browse')
            self.liste.heading('Info', text='Info')
            self.liste.column('Info', width=120, anchor=tk.W)
            self.liste.heading('Description', text='Description')
            self.liste.column('Description', width=120, anchor=tk.W)

            data = []
            for n in range(1, 10):
                data.append((f'info {n}', f'Description {n}'))
            for emp in data:
                self.liste.insert('', tk.END, values=emp)
            self.liste.grid(row=3, column=3, columnspan=1, pady=(20, 0))

            VueGen.generate_label(self.master_frame, 'order_verification', "Elements corrects", 25, 2, "groove", tk.CENTER, [5, 0],
                                  [None, None])

            self.order_verified = ttk.Checkbutton(self.master_frame, text='Oui', onvalue=1, offvalue=0)
            self.order_verified.grid(row=5, column=3, pady=(20, 0))

            VueGen.generate_button(self.master_frame, 'back', 'Retour', [25, None], [6, 3], [2, None], None)
            VueGen.generate_button(self.master_frame, 'confirm', 'Confirmer', [25, None], [6, 0], [2, None], None)

        def confirm_order(self):
            value = []
            # value['type'] = self.unit_options_dropdown.get()
            # value['price'] = self.unit_price.get()
            # value['date'] = self.date_value.get()
            value['buyer'] = self.buyer_value.get()
            # value['payment'] = self.payment_options_dropdown.get()

            print(value)

        def clic_bouton_membre(self):
            self.delete_lists()
            print(self.canevas_list.winfo_width() + 1)
            colonnes = ('Nom', 'Permission', 'Rôle')
            self.liste = ttk.Treeview(self.canevas_list, columns=colonnes, show='headings',
                                      selectmode='browse')
            self.liste.heading('Nom', text='Nom')

            data = []
            for n in range(1, 50):
                data.append((f'Employé {n}', f'Accès {n}', f'Rôle {n}'))

            self.liste.heading('Permission', text='Permission')
            self.liste.heading('Rôle', text='Rôle')
            self.liste.column('Rôle', anchor='center')
            self.liste.column('Permission', anchor='center')
            self.liste.column('Nom', anchor='center')
            for emp in data:
                self.liste.insert('', tk.END, values=emp)
            self.liste.place(x=0, y=0)




def main():
    try:
        controleur = None
        module = Module_Ventes_En_ligne(controleur)
        module.show_vue()
        module.mainloop()
    except:
        print_exc()
        return 1
    return 0


if __name__ == '__main__':
    quit(main())
