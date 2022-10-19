import sqlite3

FK_ON = 'PRAGMA foreign_keys = 1'

BD_GEST_MEDIA = 'gestion_media.db'

# ***************** MEMBRE *********************

CREER_MEMBRE = '''
CREATE TABLE IF NOT EXISTS membre
(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    prenom TEXT NOT NULL,
    nom TEXT NOT NULL,
    identifiant TEXT NOT NULL,
    mdp TEXT,
    titre TEXT,
    genre TEXT
)
'''
DROP_MEMBRE = 'DROP TABLE IF EXISTS membre'
INSERT_MEMBRE = 'INSERT INTO membre(prenom, nom, identifiant, mdp, titre,genre) VALUES(?, ?, ?, ?, ?, ?)'
SELECT_MEMBRES = 'SELECT * FROM membre'
SELECT_MEMBRE = 'SELECT * FROM membre WHERE identifiant=?'
SELECT_ID_MEMBRE = 'SELECT id FROM membre WHERE identifiant=?'
DELETE_MEMBRE = 'DELETE FROM membre WHERE identifiant=?'
UPDATE_MEMBRE = ''' 
UPDATE membre
    SET prenom = ?,
    nom = ?,
    titre = ?,
    identifiant = ?
WHERE id = ?
'''

# ***************** COMPAGNIE *********************

CREER_COMPAGNIE = '''
CREATE TABLE IF NOT EXISTS compagnie
(
    id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    nom TEXT UNIQUE,
    pays TEXTE,
    province TEXTE,
    region TEXTE
)
'''
DROP_COMPAGNIE = 'DROP TABLE IF EXISTS compagnie'
INSERT_COMPAGNIE = 'INSERT INTO compagnie(nom, pays, province, region) VALUES(?, ?, ?, ?)'
SELECT_COMPAGNIES = 'SELECT * FROM compagnie'
SELECT_COMPAGNIE = 'SELECT * FROM compagnie WHERE id=?'
SELECT_ID_COMPAGNIE = 'SELECT id FROM compagnie WHERE nom=?'
DELETE_COMPAGNIE = 'DELETE FROM compagnie WHERE id=?'


# ***************** MEMBRE DANS COMPAGNIE *********************

CREER_MEMBRE_DANS_COMPAGNIE = '''
CREATE TABLE IF NOT EXISTS membre_dans_compagnie
(
    id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    id_compagnie INTEGER NOT NULL,
    id_membre INTEGER NOT NULL,
    permission_membre TEXT NOT NULL,
    
    FOREIGN KEY(id_compagnie) REFERENCES compagnie(id),
    FOREIGN KEY(id_membre) REFERENCES membre(id)
)
'''
DROP_MEMBRE_DANS_COMPAGNIE = 'DROP TABLE IF EXISTS membre_dans_compagnie'
INSERT_MEMBRE_DANS_COMPAGNIE = 'INSERT INTO membre_dans_compagnie(id_compagnie, id_membre, permission_membre) VALUES(?, ?, ?)'
SELECT_ALL_MEMBRE_DANS_COMPAGNIE = 'SELECT * FROM membre_dans_compagnie'
SELECT_MEMBRE_DANS_COMPAGNIES = 'SELECT * FROM membre_dans_compagnie WHERE id_membre=?'
DELETE_MEMBRE_FROM_COMPAGNIE = 'DELETE FROM membre_dans_compagnie WHERE id_membre=?'
UPDATE_PERMISSION_MEMBRE = '''
UPDATE membre_dans_compagnie
    SET permission_membre = ?
WHERE id_membre = ? AND id_compagnie = ?
'''

# ***************** MODULES *********************

CREER_MODULE = '''
CREATE TABLE IF NOT EXISTS modules
(
    id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    nom TEXT NOT NULL,
    description TEXT,
    version NUMERIC NOT NULL,
    chemin_executable TEXT NOT NULL,
    prix_mensuel NUMERIC NOT NULL
)
'''
DROP_MODULES = 'DROP TABLE IF EXISTS modules'
INSERT_MODULES = 'INSERT INTO modules(nom, version, prix_mensuel) VALUES(?, ?)'
SELECT_MODULES = 'SELECT * FROM modules'

# ***************** ACCÈS *********************
CREER_ACCES = '''
CREATE TABLE IF NOT EXISTS acces
(
    id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    nom TEXT NOT NULL UNIQUE
)
'''
DROP_ACCES = 'DROP TABLE IF EXISTS acces'
INSERT_ACCES = 'INSERT INTO acces(nom) VALUES(?)'
SELECT_ACCES = 'SELECT * FROM acces'

# ***************** MODULE PAR ACCÈS *********************
CREER_MODULE_PAR_ACCES = '''
CREATE TABLE IF NOT EXISTS module_par_acces
(
    id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    id_module  INTEGER NOT NULL,
    id_acces INTEGER NOT NULL,
        
    FOREIGN KEY(id_module) REFERENCES module(id),
    FOREIGN KEY(id_acces) REFERENCES acces(id)
)
'''
DROP_MODULE_PAR_ACCES = 'DROP TABLE IF EXISTS module_par_acces'
INSERT_MODULE_PAR_ACCES = 'INSERT INTO module_par_acces(id_module, id_acces) VALUES(?,?)'
SELECT_MODULE_PAR_ACCES = 'SELECT * FROM module_par_acces'

# ***************** MODULE PAR ACCÈS *********************
CREER_ACCES_PAR_MEMBRE = '''
CREATE TABLE IF NOT EXISTS acces_par_membre
(
    id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    id_membre  INTEGER NOT NULL,
    id_acces INTEGER NOT NULL,

    FOREIGN KEY(id_membre) REFERENCES membre(id),
    FOREIGN KEY(id_acces) REFERENCES acces(id)
)
'''
DROP_ACCES_PAR_MEMBRE = 'DROP TABLE IF EXISTS acces_par_membre'
INSERT_ACCES_PAR_MEMBRE = 'INSERT INTO acces_par_membre(id_module, id_acces) VALUES(?,?)'
SELECT_ACCES_PAR_MEMBRE = 'SELECT * FROM acces_par_membre'


class Dao:
    __creer = [
        CREER_COMPAGNIE,
        CREER_MEMBRE,
        CREER_MODULE,
        CREER_ACCES,
        CREER_MEMBRE_DANS_COMPAGNIE,
        CREER_MODULE_PAR_ACCES,
        CREER_ACCES_PAR_MEMBRE
    ]
    __detruire = [
        DROP_ACCES_PAR_MEMBRE,
        DROP_MODULE_PAR_ACCES,
        DROP_MEMBRE_DANS_COMPAGNIE,
        DROP_ACCES,
        DROP_MODULES,
        DROP_MEMBRE,
        DROP_COMPAGNIE
    ]

    # singleton pas possible car:

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

    # ***************** AJOUTER METHODES DA0 *********************

    # ***************** SELECT
    def select_all_membres(self):
        self.cur.execute(SELECT_MEMBRES)
        return self.cur.fetchall()

    def select_all_compagnies(self):
        self.cur.execute(SELECT_COMPAGNIES)
        return self.cur.fetchall()

    def select_membres_all_compagnie(self):
        self.cur.execute(SELECT_ALL_MEMBRE_DANS_COMPAGNIE)
        return self.cur.fetchall()

    def select_id_of_compagnie(self, name):
        self.cur.execute(SELECT_ID_COMPAGNIE, (name,))
        return self.cur.fetchall()[0][0]

    def get_membre_id(self, identifiant):
        self.cur.execute(SELECT_ID_MEMBRE, (identifiant,))
        return self.cur.fetchall()[0][0]

    # ***************** INSERT
    def insert_membre(self, prenom, nom, identifiant, mdp, titre, genre, id_compagnie, permission):
        cursor = self.cur.execute(INSERT_MEMBRE, (prenom, nom, identifiant, mdp, titre, genre))
        self.cur.execute(INSERT_MEMBRE_DANS_COMPAGNIE, (id_compagnie, cursor.lastrowid, permission))
        self.conn.commit()

    def insert_compagnie(self, nom, pays, province, region):
        self.cur.execute(INSERT_COMPAGNIE, (nom, pays, province, region))
        self.conn.commit()
        # TODO j'ai besoin de l'ID de la compagnie pour ajouter l'admin
        return self.select_all_compagnies()

    def insert_membre_dans_compagnie(self, id_compagnie, id_membre, permission_membre):
        self.cur.execute(INSERT_MEMBRE_DANS_COMPAGNIE, (id_compagnie, id_membre, permission_membre))
        self.conn.commit()

    def insert_acces(self, nom):
        self.cur.execute(INSERT_ACCES, (nom,))
        self.conn.commit()

    def insert_module_par_acces(self, id_module, id_acces):
        self.cur.execute(INSERT_MODULE_PAR_ACCES, (id_module, id_acces))
        self.conn.commit()

    # ***************** DELETE
    def delete_membre(self, identifiant):
        id_membre = self.get_membre_id(identifiant)
        self.cur.execute(DELETE_MEMBRE_FROM_COMPAGNIE, (id_membre,))
        self.cur.execute(DELETE_MEMBRE, (identifiant,))

    # ***************** UPDATE
    def update_membre(self, identifiant, nom, prenom, titre, permission_membre=None, nom_compagnie=None):
        id_membre = self.get_membre_id(identifiant)
        if (permission_membre is not None) and (nom_compagnie is not None):
            self.update_permission_membre(id_membre, nom_compagnie, permission_membre)

        self.cur.execute(UPDATE_MEMBRE, (nom, prenom, titre, identifiant, id_membre))
        self.conn.commit()

    def update_permission_membre(self, id_membre, nom_compagnie, permission_membre):
        id_compagnie = self.select_id_of_compagnie(nom_compagnie)
        self.cur.execute(UPDATE_PERMISSION_MEMBRE, (permission_membre, id_membre, id_compagnie))
        self.conn.commit()

    # ***************** AUTRES
    def identifier_usager(self, nom, mdp):
        sql = '''
            SELECT
                membre.identifiant,
                membre.titre,
                compagnie.id,
                compagnie.nom
            FROM membre
            INNER JOIN membre_dans_compagnie
                ON membre_dans_compagnie.id_membre = membre.id
            INNER JOIN compagnie
                ON membre_dans_compagnie.id_compagnie = compagnie.id
            WHERE membre.identifiant = ? AND membre.mdp = ?
        '''
        self.cur.execute(sql, (nom, mdp))
        return self.cur.fetchall()

def main():
    Dao().creer_bd()
    return 0


# main

if __name__ == '__main__':
    quit(main())
