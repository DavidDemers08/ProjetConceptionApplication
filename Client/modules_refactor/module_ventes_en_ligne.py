from traceback import print_exc

from Client.AbstractClasses.Module import Module
from Client.AbstractClasses.Vue import Vue

import tkinter as tk
from tkinter import ttk

import Utils.utils


class ModuleVentesEnLigne(Module):

    def __init__(self, controleur, master_frame):
        super().__init__(controleur, master_frame)

    def set_vue(self):
        return ModuleVentesEnLigne.VueOnlineSales(self, self.master_frame, row=0, column=0, padx=10, pady=10)

    class VueOnlineSales(Vue):

        def __init__(self, parent, master_frame, row: int, column: int, padx: int, pady: int):
            super().__init__(parent, master_frame, row, column, padx, pady)

        def remplir_vue(self):
            self.label_tittle = ttk.Label(self.master_frame, text='Ventes en ligne', borderwidth=3,
                                          relief="groove")
            self.label_tittle.grid(row=0, column=0, pady=(20, 20), padx=(20, 20), columnspan=2, sticky=tk.N)

            self.bouton_create_order = ttk.Button(self.master_frame, text='Faire une commande', width=25,
                                                  command=self.clic_bouton_create_order)
            self.bouton_create_order.bind('<Return>', lambda e: self.bouton_create_order.invoke())
            self.bouton_create_order.grid(row=1, column=0, pady=(20, 20), padx=(20, 20), columnspan=2, sticky=tk.N)

            self.bouton_launch_verify_order = ttk.Button(self.master_frame, text='Verifier une commande', width=25,
                                                         command=self.clic_bouton_verify_order)
            self.bouton_launch_verify_order.bind('<Return>', lambda e: self.bouton_launch_verify_order.invoke())
            self.bouton_launch_verify_order.grid(row=2, column=0, pady=(20, 20), padx=(20, 20), columnspan=2,
                                                 sticky=tk.N)

            self.bouton_complete_order = ttk.Button(self.master_frame, text='Completer une commande', width=25,
                                                    command=self.clic_bouton_complete_order)
            self.bouton_complete_order.bind('<Return>', lambda e: self.bouton_complete_order.invoke())
            self.bouton_complete_order.grid(row=3, column=0, pady=(20, 20), padx=(20, 20), columnspan=2, sticky=tk.N)

            self.bouton_annuler = ttk.Button(self.master_frame, text='Annuler', command=self.clic_bouton_annuler_menu)
            self.bouton_annuler.bind('<Return>', lambda e: self.bouton_annuler.invoke())
            self.bouton_annuler.grid(row=5, column=0, pady=(20, 20), padx=(20, 20), sticky=tk.E)

        def clic_bouton_annuler_menu(self):
            self.vider_frame()
            self.controleur.set_module("menu")

        def clic_bouton_annuler_ventes(self):
            self.vider_frame()
            self.controleur.set_module("Gestion Vente En Ligne")

        def clic_bouton_create_order(self):
            if self.controleur:
                self.vider_frame()
                self.remplir_vue_faire_commande()

        def clic_bouton_verify_order(self):
            if self.controleur:
                self.vider_frame()
                self.remplir_vue_verifier_commande()

        def clic_bouton_complete_order(self):
            if self.controleur:
                self.vider_frame()
                self.remplir_vue_finaliser_commande()

        # def remplir_vue(self):
        def remplir_vue_faire_commande(self):
            # TODO: ajouter optioni paiement dans utils
            # TODO: ajouter options dunite

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

            self.label_tittle = ttk.Label(self.master_frame, text='Faire une commande', borderwidth=3,
                                          relief="groove")
            self.label_tittle.grid(row=0, column=0, pady=(20, 20), padx=(20, 20), sticky=tk.N)

            self.label_unit_type = ttk.Label(self.master_frame, text='Type dunité', width=20, borderwidth=3,
                                             relief="groove")
            self.label_unit_type.grid(row=1, column=0, pady=(20, 20), padx=(20, 20), sticky=tk.N)

            self.label_unit_price = ttk.Label(self.master_frame, text="Prix d'unite", width=20, borderwidth=3,
                                              relief="groove")
            self.label_unit_price.grid(row=2, column=0, pady=(20, 20), padx=(20, 20), sticky=tk.N)

            self.unit_options_dropdown = ttk.OptionMenu(self.master_frame, self.unit_options, *UNIT_OPTIONS, )
            self.unit_options_dropdown.grid(row=1, column=3, pady=(20, 20), padx=(20, 20), columnspan=2, )

            self.unit_price = ttk.Label(self.master_frame, text=" ", width=20, borderwidth=2, relief="groove")
            self.unit_price.config(anchor=tk.CENTER)
            self.unit_price.grid(row=2, column=3, pady=(20, 20), padx=(20, 20), columnspan=2)

            self.label_date = ttk.Label(self.master_frame, text="Date", width=20, borderwidth=3,
                                        relief="groove")
            self.label_date.grid(row=3, column=0, pady=(20, 20), padx=(20, 20), sticky=tk.N)

            self.date_value = ttk.Label(self.master_frame, text=" ", width=20, borderwidth=2, relief="groove")
            self.date_value.config(anchor=tk.CENTER)
            self.date_value.grid(row=3, column=3, pady=(20, 20), padx=(20, 20), columnspan=2)

            self.label_buyer = ttk.Label(self.master_frame, text="Acheteur", width=20, borderwidth=3,
                                         relief="groove")
            self.label_buyer.grid(row=4, column=0, pady=(20, 20), padx=(20, 20), sticky=tk.N)

            self.buyer_value = ttk.Entry(self.master_frame, width=20, )
            self.buyer_value.grid(row=4, column=3, pady=(20, 20), padx=(20, 20), columnspan=2)

            self.label_payment = ttk.Label(self.master_frame, text="Paiement", width=20, borderwidth=3,
                                           relief="groove")
            self.label_payment.grid(row=5, column=0, pady=(20, 20), padx=(20, 20), sticky=tk.N)

            self.payment_options_dropdown = ttk.OptionMenu(self.master_frame, self.payment_options, *PAYMENT_OPTIONS)
            self.payment_options_dropdown.grid(row=5, column=3, pady=(20, 20), padx=(20, 20), columnspan=2)

            self.bouton_annuler = ttk.Button(self.master_frame, text='Annuler', width=25,
                                             command=self.clic_bouton_annuler_ventes)
            self.bouton_annuler.bind('<Return>', lambda e: self.bouton_annuler.invoke())
            self.bouton_annuler.grid(row=6, column=0, pady=(20, 20), padx=(20, 20), columnspan=2)

            self.bouton_order = ttk.Button(self.master_frame, text='Confirmer commande', width=25,
                                           command=self.clic_bouton_order)
            self.bouton_order.bind('<Return>', lambda e: self.bouton_order.invoke())
            self.bouton_order.grid(row=6, column=3, pady=(20, 20), padx=(20, 20), columnspan=2)

        def clic_bouton_order(self):
            pass

        def remplir_vue_verifier_commande(self):
            self.label_tittle = ttk.Label(self.master_frame, text='Verifier commande')
            self.label_tittle.grid(row=0, column=2, columnspan=2)

            self.label_order_number = ttk.Label(self.master_frame, text="Numero de Commande", width=25, borderwidth=3,
                                                relief="groove")
            self.label_order_number.grid(row=2, column=2, pady=(20, 20), padx=(20, 20), sticky=tk.N)

            self.bouton_annuler = ttk.Button(self.master_frame, text='Annuler', width=25,
                                             command=self.clic_bouton_annuler_ventes)
            self.bouton_annuler.bind('<Return>', lambda e: self.bouton_annuler.invoke())
            self.bouton_annuler.grid(row=6, column=0, pady=(20, 20), padx=(20, 20), columnspan=2)

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
            self.label_tittle.grid(row=0, column=0, columnspan=3, pady=(10, 10), sticky=tk.N)

            self.label_order_number = ttk.Label(self.master_frame, text="Numero de Commande", width=25, borderwidth=3,
                                                relief="groove")
            self.label_order_number.grid(row=1, column=0, pady=(10, 10), padx=(20, 20), sticky=tk.N)

            self.order_number_value = ttk.Label(self.master_frame, text="#Order", width=25, borderwidth=2,
                                                relief="groove")
            self.order_number_value.config(anchor=tk.CENTER)
            self.order_number_value.grid(row=1, column=2, pady=(10, 10), padx=(20, 20), )

            self.label_order_info = ttk.Label(self.master_frame, text="Valider Information", borderwidth=3,
                                              relief="groove", width=40, anchor=tk.N)
            self.label_order_info.grid(row=2, column=0, columnspan=3, pady=(10, 10), padx=(10, 10), sticky=tk.N, )

            colonne = ('Info', 'Description')
            self.liste = ttk.Treeview(self.master_frame, columns=colonne, show='headings',
                                      selectmode='browse')
            self.liste.heading('Info', text='Info')
            self.liste.column('Info', anchor=tk.N)
            self.liste.heading('Description', text='Description')
            self.liste.column('Description', anchor=tk.N)

            data = []
            for n in range(1, 10):
                data.append((f'info {n}', f'Description {n}'))
            for emp in data:
                self.liste.insert('', tk.END, values=emp)
            self.liste.grid(row=3, column=0, columnspan=3, pady=(10, 10), padx=(10, 10), )

            self.label_order_verification = ttk.Label(self.master_frame, text="Elements corrects", width=25,
                                                      borderwidth=3,
                                                      relief="groove")
            self.label_order_verification.grid(row=5, column=0, pady=(10, 10), padx=(20, 20), sticky=tk.N)

            self.order_verified = ttk.Checkbutton(self.master_frame, text='Oui', onvalue=1, offvalue=0)
            self.order_verified.grid(row=5, column=2, pady=(10, 10), padx=(20, 20), )

            self.bouton_annuler = ttk.Button(self.master_frame, text='Retour', width=25,
                                             command=self.clic_bouton_annuler_ventes)
            self.bouton_annuler.bind('<Return>', lambda e: self.bouton_annuler.invoke())
            self.bouton_annuler.grid(row=6, column=0, pady=(10, 10), padx=(20, 20))

            self.bouton_confirm = ttk.Button(self.master_frame, text='Confirmer commande', width=25,
                                             command=self.clic_bouton_confirmer_ventes)
            self.bouton_confirm.bind('<Return>', lambda e: self.bouton_annuler.invoke())
            self.bouton_confirm.grid(row=6, column=2, pady=(10, 10), padx=(20, 20))

        def clic_bouton_confirmer_ventes(self):
            # value = []
            # # value['type'] = self.unit_options_dropdown.get()
            # # value['price'] = self.unit_price.get()
            # # value['date'] = self.date_value.get()
            # value['buyer'] = self.buyer_value.get()
            # # value['payment'] = self.payment_options_dropdown.get()
            #
            # print(value)
            pass


def main():
    try:
        controleur = None
        module = ModuleVentesEnLigne(controleur)
        module.show_vue()
        module.mainloop()
    except:
        print_exc()
        return 1
    return 0


if __name__ == '__main__':
    quit(main())
