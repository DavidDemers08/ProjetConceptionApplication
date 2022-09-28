import sqlite3

FK_ON = 'PRAGMA foreign_keys = 1'

BD_GEST_MEDIA = 'gestion_media.db'

# ***************** CLIENT *********************

CREER_CLIENT = '''
CREATE TABLE IF NOT EXISTS client
(
    idclient INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    nom TEXT,
    courriel TEXT,
    tel TEXT,
    compagnie TEXT,
    adresse TEXT,
    rue TEXT,
    ville TEXT
)'''
DROP_CLIENT = 'DROP TABLE IF EXISTS client'
INSERT_CLIENT = 'INSERT INTO client(nom, courriel, tel, compagnie, adresse, rue, ville) VALUES(?, ?, ?, ?, ?, ?, ?)'
SELECT_CLIENT = 'SELECT * FROM client'

# ***************** PROJET *********************

CREER_PROJET = '''
CREATE TABLE IF NOT EXISTS projet
(
    idprojet INTEGER PRIMARY KEY AUTOINCREMENT,
    nomdeprojet TEXT UNIQUE,
    client NUMERIC,
    chargedeprojet NUMERIC,
    datedelancement DATE,
    datedefinprevue DATE
)'''
DROP_PROJET = 'DROP TABLE IF EXISTS projet'
INSERT_PROJET = 'INSERT INTO projet(nomdeprojet, client, chargedeprojet, datedelancement, datedefinprevue) VALUES(?, ?, ?, ?, ?)'
SELECT_PROJET = 'SELECT * FROM projet'

# ***************** MODULES *********************

CREER_MODULES = '''
CREATE TABLE IF NOT EXISTS modules
(
    idmodule INTEGER PRIMARY KEY AUTOINCREMENT,
    monmodule TEXT NOT NULL,
    version NUMERIC NOT NULL
)'''
DROP_MODULES = 'DROP TABLE IF EXISTS modules'
INSERT_MODULES = 'INSERT INTO modules(monmodule, version) VALUES(?, ?)'
SELECT_MODULES = 'SELECT * FROM modules'

# ***************** COMPAGNIE *********************

CREER_COMPAGNIE = '''
CREATE TABLE IF NOT EXISTS compagnie
(
    idcompagnie INTEGER PRIMARY KEY AUTOINCREMENT,
    nomcompagnie TEXT UNIQUE
)
'''
DROP_COMPAGNIE = 'DROP TABLE IF EXISTS compagnie'
INSERT_COMPAGNIE = 'INSERT INTO compagnie(nomcompagnie) VALUES(?)'
SELECT_COMPAGNIE = 'SELECT * FROM compagnie'

# ***************** MEMBRE *********************

CREER_MEMBRE = '''
CREATE TABLE IF NOT EXISTS membre
(
    idmembre INTEGER PRIMARY KEY AUTOINCREMENT,
    compagnie NUMERIC NOT NULL REFERENCES compagnie(idcompagnie),
    identifiant TEXT NOT NULL,
    mdp TEXT,
    permission TEXT NOT NULL,
    titre TEXT
)
'''
DROP_MEMBRE = 'DROP TABLE IF EXISTS membre'
INSERT_MEMBRE = 'INSERT INTO membre(compagnie, identifiant, mdp, permission, titre) VALUES(?, ?, ?, ?, ?)'
SELECT_MEMBRE = 'SELECT * FROM membre'

class Dao():
    __creer = [
        CREER_CLIENT,
        CREER_PROJET,
        CREER_MODULES,
        CREER_COMPAGNIE,
        CREER_MEMBRE
    ]
    __detruire = [
        DROP_CLIENT,
        DROP_PROJET,
        DROP_MODULES,
        DROP_MEMBRE,
        DROP_COMPAGNIE
    ]
    
    #singleton pas possible car:
    
    # sqlite3.ProgrammingError: SQLite objects created in a thread can only be used in that same thread. The object was created in thread id 12960 and this is thread id 14996.  
    def __init__(self):
        self.chemin_bd = BD_GEST_MEDIA
        self.connexion()    

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

    def insert_membre(self, compagnie, identifiant, mdp, permission, titre):
        self.cur.execute(INSERT_MEMBRE, (compagnie, identifiant, mdp, permission, titre))
        self.conn.commit()

    def insert_compagnie(self, nomcompagnie):
        self.cur.execute(INSERT_COMPAGNIE, (nomcompagnie,))
        self.conn.commit()

    def select_membre(self):
        self.cur.execute(SELECT_MEMBRE)
        return self.cur.fetchall()

    def select_compagnie(self):
        self.cur.execute(SELECT_COMPAGNIE)
        return self.cur.fetchall()

    def identifier_usager(self, nom, mdp):
        sql = '''
            SELECT
                membre.identifiant,
                membre.permission,
                membre.titre,
                compagnie.idcompagnie,
                compagnie.nomcompagnie
            FROM membre
            INNER JOIN compagnie
            ON membre.compagnie = compagnie.idcompagnie
            WHERE membre.identifiant = ? AND membre.mdp = ?  
        '''
        self.cur.execute(sql, (nom, mdp))
        return self.cur.fetchall()


def main():
    Dao().creer_bd()
    return 0
#main

if __name__ == '__main__':
    quit(main())
