import sqlite3
import traceback

from Serveur.DAO.dao_modules import *
from Serveur.DAO.tables_requetes_SaaS import *


# singleton pas possible car:
# sqlite3.ProgrammingError: SQLite objects created in a thread can only be used in that same thread.
# The object was created in thread id 12960 and this is thread id 14996.

class Dao:
    __creer = [
        CREER_COMPAGNIE,
        CREER_MEMBRE,
        CREER_MODULE,
        CREER_ACCESS,
        CREER_MEMBRE_DANS_COMPAGNIE,
        CREER_MODULE_PAR_ACCESS,
        CREER_ACCESS_PAR_MEMBRE,
        CREER_MODULE_PAR_COMPAGNIE,
        CREER_VEHICULE_PAR_COMPAGNIE
    ]
    __detruire = [
        DROP_VEHICULE_PAR_COMPAGNIE,
        DROP_MODULE_PAR_COMPAGNIE,
        DROP_ACCESS_PAR_MEMBRE,
        DROP_MODULE_PAR_ACCESS,
        DROP_MEMBRE_DANS_COMPAGNIE,
        DROP_ACCESS,
        DROP_MODULES,
        DROP_MEMBRE,
        DROP_COMPAGNIE
    ]

    def __init__(self):
        self.chemin_bd = BD_GEST_MEDIA
        self.connexion()
        # self.Inventaire = Inventaire(self.cur, self.conn, Dao.__creer, Dao.__detruire) ----> exemple de creation de
        # classe pour un module

    def __del__(self):
        self.deconnexion()

    def connexion(self):
        self.conn = sqlite3.connect(self.chemin_bd)
        self.cur = self.conn.cursor()
        self.cur.execute(FK_ON)

    def deconnexion(self):
        self.cur.close()
        self.conn.close()

    def creer_bd(self):
        for table in Dao.__detruire:
            self.cur.execute(table)
        for table in Dao.__creer:
            self.cur.execute(table)

    # ***************** AJOUTER METHODES DA0 *********************

    # ***************** SELECT
    def select_all_membres(self):
        self.cur.execute(SELECT_MEMBRES)
        return self.cur.fetchall()

    def select_id_membre_with_username(self, username):
        self.cur.execute(SELECT_ID_MEMBRE_WITH_USERNAME, (username,))
        return self.cur.fetchone()[0]

    def select_all_compagnies(self):
        self.cur.execute(SELECT_COMPAGNIES)
        return self.cur.fetchall()

    def select_id_of_compagnie(self, name):
        try:
            self.cur.execute(SELECT_ID_COMPAGNIE, (name,))
            return self.cur.fetchone()[0]
        except:
            return False

    def get_membre_id(self, identifiant):
        self.cur.execute(SELECT_ID_MEMBRE, (identifiant,))
        return self.cur.fetchone()[0]

    def get_module_id(self, nom, version):
        self.cur.execute(SELECT_ID_MODULE, (nom, version))
        return self.cur.fetchone()

    def select_all_modules_of_compagnie(self, id_compagnie):
        self.cur.execute(SELECT_ALL_MODULE_PAR_COMPAGNIE, (id_compagnie,))
        return self.cur.fetchall()

    def select_module(self, nom, version):
        id_module = self.get_module_id(nom, version)
        self.cur.execute(SELECT_MODULE, (id_module,))
        return self.cur.fetchone()

    def select_all_modules(self):
        self.cur.execute(SELECT_MODULES)
        return self.cur.fetchall()

    # retourne tous les compagnies d'un membre en particulier
    def select_all_compagnie_de_membre(self, id_membre):
        self.cur.execute(SELECT_ALL_COMPAGNIES_DE_MEMBRE, (id_membre,))
        return self.cur.fetchall()

    def delete_module(self, nom, version):
        self.cur.execute(DELETE_MODULE, (nom, version))

    # retourne tous les membres de tous les compagnies
    # (un membre peut être là plusieurs fois)
    def select_membres_all_compagnie(self):
        self.cur.execute(SELECT_ENTIRE_MEMBRE_DANS_COMPAGNIE)
        return self.cur.fetchall()

    # retourne tous les membres d'une compagnie
    def select_all_membres_de_compagnie(self, nom_compagnie):
        id_compagnie = self.select_id_of_compagnie(nom_compagnie)
        self.cur.execute(SELECT_ALL_MEMBRES_DE_COMPAGNIE, (id_compagnie,))
        return self.cur.fetchall()

    def select_nom_compagnie(self, id_compagnie):
        self.cur.execute(SELECT_NOM_COMPAGNIE, (id_compagnie,))
        return self.cur.fetchall()

    def select_all_modules_all_compagnies(self):
        self.cur.execute(SELECT_ALL_MODULE_PAR_ALL_COMPAGNIE)
        return self.cur.fetchall()

    def select_all_access(self):
        self.cur.execute(SELECT_ALL_ACCESS)
        return self.cur.fetchall()

    def select_all_module_par_acces(self):
        self.cur.execute(SELECT_ALL_MODULE_PAR_ALL_ACCESS)
        return self.cur.fetchall()

    def select_all_acces_membres(self):
        self.cur.execute(SELECT_ALL_ACCES_POUR_ALL_MEMBRES)
        return self.cur.fetchall()

    def select_all_vehicules(self):
        self.cur.execute(SELECT_ALL_VEHICULE_PAR_COMPAGNIE)
        return self.cur.fetchall()

    def get_access_id(self, nom):
        self.cur.execute(SELECT_ACCESS_ID, (nom,))
        return self.cur.fetchone()

    def insert_module_pour_compagnie(self, id_compagnie, id_module):
        self.cur.execute(INSERT_MODULE_PAR_COMPAGNIE, (id_compagnie, id_module))
        self.conn.commit()

    def insert_membre(self, prenom, nom, identifiant, mdp, titre, genre, id_compagnie: int, permission: str,
                      nom_access: str):
        try:
            cursor = self.cur.execute(INSERT_MEMBRE, (prenom, nom, identifiant, mdp, titre, genre))
            self.conn.commit()
            self.cur.execute(INSERT_MEMBRE_DANS_COMPAGNIE, (id_compagnie, cursor.lastrowid, permission))
            self.conn.commit()

            id_access_initial = self.get_access_id(nom_access)
            if id_access_initial is None:
                self.insert_acces(nom_access)
                id_access = self.get_access_id(nom_access)
                self.insert_membre_a_acces(self.cur.lastrowid, id_access)
            else:
                id_access = id_access_initial
                self.insert_membre_a_acces(self.cur.lastrowid, id_access)
            return self.cur.lastrowid
        except Exception:
            traceback.print_exc()
            return False

    def id_access_initial(self, nom_access):
        id_access_initial = self.get_access_id(nom_access)

        if id_access_initial is None:
            self.insert_acces(nom_access)
            id_access = self.get_access_id(nom_access)
            print(id_access)
            self.insert_membre_a_acces(self.cur.lastrowid, id_access)
        else:
            id_access = id_access_initial
            self.insert_membre_a_acces(self.cur.lastrowid, id_access)

    def insert_compagnie(self, nom, pays, province, region):
        try:
            self.cur.execute(INSERT_COMPAGNIE, (nom, pays, province, region))
            self.conn.commit()
            return self.cur.execute(SELECT_ID_COMPAGNIE, (nom,)).fetchone()[0]
        except:
            return False

    def insert_membre_dans_compagnie(self, id_compagnie, id_membre, permission_membre):
        self.cur.execute(INSERT_MEMBRE_DANS_COMPAGNIE, (id_compagnie, id_membre, permission_membre))
        self.conn.commit()

    def insert_acces(self, nom, modules_id: list = None):
        self.cur.execute(INSERT_ACCESS, (nom,))
        if modules_id is not None:
            self.insert_modules_pour_acces(self.cur.lastrowid, modules_id)
        self.conn.commit()

    def insert_modules_pour_acces(self, id_acces: int, modules_id: list):
        tuple_array = []
        for id_module in modules_id:
            tuple_array.append((id_module, id_acces))
        self.cur.executemany(INSERT_MODULE_PAR_ACCESS, tuple_array)
        self.conn.commit()

    def insert_vehicule_dans_compagnie(self, id_compagnie, annee_modele, marque, modele, kilometrage, type):
        self.cur.execute(INSERT_VEHICULE_PAR_COMPAGNIE, (id_compagnie, annee_modele, marque, modele, kilometrage, type))
        self.conn.commit()

    # ***************** DELETE
    def delete_membre(self, identifiant):
        id_membre = self.get_membre_id(identifiant)
        self.cur.execute(DELETE_MEMBRE_FROM_COMPAGNIE, (id_membre,))
        self.cur.execute(DELETE_MEMBRE, (identifiant,))

    def delete_access(self, nom):
        id_access = self.get_access_id(nom)
        self.cur.execute(DELETE_ACCESS, (nom, id_access))

    def delete_vehicule(self, id_vehicule, id_compagnie):
        self.cur.execute(DELETE_VEHICULE_PAR_COMPAGNIE, (id_vehicule, id_compagnie))

    # ***************** UPDATE
    def update_membre(self, id_membre, identifiant, nom, prenom, titre, permission_membre=None, nom_compagnie=None):
        if (permission_membre is not None) and (nom_compagnie is not None):
            self.update_permission_membre(id_membre, nom_compagnie, permission_membre)

        self.cur.execute(UPDATE_MEMBRE, (nom, prenom, titre, identifiant, id_membre))
        self.conn.commit()

    def update_permission_membre(self, id_membre, nom_compagnie, permission_membre):
        id_compagnie = self.select_id_of_compagnie(nom_compagnie)
        self.cur.execute(UPDATE_PERMISSION_MEMBRE, (permission_membre, id_membre, id_compagnie))
        self.conn.commit()

    def update_vehicule(self, annee_modele, marque, modele, kilometrage, type, id_vehicule, id_compagnie):
        self.cur.execute(UPDATE_VEHICULE_COMPAGNIE,
                         (annee_modele, marque, modele, kilometrage, type, id_vehicule, id_compagnie))
        self.conn.commit()

    # ***************** AUTRES
    def identifier_usager(self, nom, mdp):
        # sql = '''
        #     SELECT
        #         membre.identifiant,
        #         membre.titre,
        #         compagnie.id,
        #         compagnie.nom
        #     FROM membre
        #     INNER JOIN membre_dans_compagnie
        #         ON membre_dans_compagnie.id_membre = membre.id
        #     INNER JOIN compagnie
        #         ON membre_dans_compagnie.id_compagnie = compagnie.id
        #     WHERE membre.identifiant = ? AND membre.mdp = ?
        # '''
        return self.cur.execute(SELECT_MEMBRE, (nom, mdp)).fetchone()

    def get_all_module_not_in_compagnie(self, id_compagnie):
        sql = '''
        SELECT * FROM modules
        INNER JOIN module_par_compagnie
            ON module_par_compagnie.id_module = modules.id
        WHERE id_compagnie != ?
        '''
        return self.cur.execute(sql, (id_compagnie,)).fetchall()

    def insert_module(self, nom, version, prix_mensuel, chemin_executable, derscription="Aucune Description"):
        self.cur.execute(INSERT_MODULES, (nom, derscription, version, chemin_executable, prix_mensuel))
        self.conn.commit()

    def insert_module_pour_un_access(self, id_module, id_acces):
        self.cur.execute(INSERT_MODULE_PAR_ACCESS, (id_module, id_acces))
        self.conn.commit()

    def delete_access_pour_module(self, id_module, id_access):
        self.cur.execute(DELETE_ACCESS_POUR_MODULE, (id_module, id_access))

    # TODO faire leurs fonctions!
    # INSERT_ACCESS_PAR_MEMBRE = 'INSERT INTO access_par_membre(id_module, id_acces) VALUES(?,?)'
    # SELECT_ALL_MEMBRES_POUR_ACCESS = 'SELECT * FROM access_par_membre WHERE id_access=?'
    # DELETE_ACCESS_POUR_MEMBRE = 'DELETE FROM access_par_membre WHERE id_membre=? AND id'

    # TODO Si le Select_ID ne contient pas de valeur ajuster pour qu'il puisse compiler
    def insert_membre_a_acces(self, membre_id, id_access):
        self.cur.execute(INSERT_MEMBRE_A_ACCESS, (membre_id, id_access[0]))
        self.conn.commit()

    def ajouter_acces_super_admin(self):
        self.cur.execute(INSERT_ACCESS, ("Super_Admin",))

        self.conn.commit()
        return self.cur.fetchall()

    def ajouter_lien_acces_module_super_admin(self):

        self.liste_modules_init = ["gestion", "propriete", "inventaire", "evenement", "budget", "employe",
                                   "vente_en_ligne", "plaintes", "materielle"]

        for _ in self.liste_modules_init:
            self.cur.execute(INSERT_MODULE_PAR_ACCESS, (self.get_id_module_init(_, 1.0), self.get_id_super_admin()))

        self.conn.commit()

    def select_modules_matching_username(self, username: str):
        self.cur.execute(SELECT_MODULES_MATCHING_ACCESS_OF_USERNAME, (username,))
        return self.cur.fetchall()

    def ajouter_modules_initiaux(self):

        self.cur.executemany(INSERT_MODULES, [
            ("GestionMembre", "permet de faire la gestion du personnel", 1.0, "C:\\modules\\gestion\\membre", 0.00),
            ("AjoutModules", "permet de faire l'achat de modules", 1.0, "C:\\modules\\modules", 0.00),
            ("GestionAjout", "permet de faire la gestion des ajouts", 1.0, "C:\\modules\\gestionAjout", 0.00),
            ("ModulePayement", "permet de faire la gestion des payements des modules", 1.0, "C:\\modules\\payement", 0.00),
            ("ModuleGestionDesModules", "permet de faire la gestion des payements des modules", 1.0, "C:\\travail\\gestion\\modules", 0.00),
            ("ModulesVentesEnLIgne", "permet la gestion des ventes en ligne", 1.0, "C:\\modules\\ventesEnLignes", 0.00),

            ("propriete", "permet de montrer les propriete de la compagnie", 1.0, "le chemin de traverse2", 37.47),
            ("inventaire", "permet de faire la gestion d'inventaire de la compagnie", 1.0, "le chemin de traverse3", 40.00),
            ("evenement", "permet de faire la gestion des evenements de la compagnie", 1.0,"C:\\Users\\1569\\evenement", 9.99),
            ("budget", "permet de faire la gestion du budget de la compagnie", 1.0, "C:\\Users\\1569\\budget", 12.00),
            ("plaintes", "permet de faire la gestion des plaintes de la compagnie", 1.0, "C:\\Users\\1569\\plaintes", 99.66),
            ("materielle", "permet de faire la gestion du materiel de la compagnie", 1.0, "C:\\Users\\1569\\materielle", 23.21)
        ])

        self.conn.commit()

    def get_id_super_admin(self):
        return self.cur.execute(SELECT_ACCESS_ID, ("Super_Admin",)).fetchone()[0]

    def get_id_module_init(self, nom, version):
        return self.cur.execute(SELECT_MODULE_ID, (nom, version)).fetchone()[0]

    def select_id_access(self, user_id):
        return self.cur.execute(SELECT_ACCESS_ID_WITH_USER_ID, (user_id,)).fetchone()[0]

    def select_modules_with_access_id(self, access_id):
        return self.cur.execute(SELECT_MODULES_WITH_ACCESS_ID, (access_id,)).fetchall()

    def select_module_id_by_user_id(self, user_id):
        return self.cur.execute(SELECT_MODULE_ID_WITH_USER_ID, (user_id,)).fetchall()

    def add_test_data(self):
        try:
            #add your data
            return True
        except:
            return False

    def select_module_id_by_company_id(self, company_id):
        try:
            allo = self.cur.execute(SELECT_MODULE_ID_WITH_COMPANY_ID, (company_id,)).fetchall()
            for a in allo:
                print(a)
            return self.cur.execute(SELECT_MODULE_ID_WITH_COMPANY_ID, (company_id,)).fetchall()
        except ValueError:
            print("Erreur SQl")





def main():
    Dao().creer_bd()
    return 0


# main

if __name__ == '__main__':
    quit(main())
