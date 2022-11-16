import sqlite3
from Serveur.DAO.tables_requetes_SaaS import *


class DaoModule(object):
    def __init__(self, cursor, connexion, creer: list, detruire: list):
        self.cur = cursor
        self.conn = connexion
        self.__creer = creer
        self.__detruire = detruire
        self.creer_bd()

    def creer_bd(self) -> None:
        for table in self.__detruire:
            self.cur.execute(table)
        for table in self.__creer:
            self.cur.execute(table)


# Exemple de sous-classes pour les Dao modules
class Inventaire(DaoModule):

    def __init__(self, cursor, connexion, creer, detruire):
        super().__init__(cursor, connexion, creer, detruire)
