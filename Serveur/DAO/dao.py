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
    permission TEXT NOT NULL,
    titre TEXT
    id_compagnie INTEGER NOT NULL,
    FOREIGN KEY (id_compagnie) REFERENCES compagnie(id)
)
'''
DROP_MEMBRE = 'DROP TABLE IF EXISTS membre'
INSERT_MEMBRE = 'INSERT INTO membre(prenom, nom, identifiant, mdp, titre, permission, id_compagnie) VALUES(?, ?, ?, ?, ?, ?, ?)'
SELECT_MEMBRE = 'SELECT * FROM membre'

# ***************** COMPAGNIE *********************

CREER_COMPAGNIE = '''
CREATE TABLE IF NOT EXISTS compagnie
(
    id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    nom TEXT UNIQUE,
    pays TEXTE,
    province TEXTE,
    region TEXTE,
    super_admin_id INTEGER NOT NULL,
    FOREIGN KEY (super_admin_id) REFERENCES membre(id)
)
'''
DROP_COMPAGNIE = 'DROP TABLE IF EXISTS compagnie'
INSERT_COMPAGNIE = 'INSERT INTO compagnie(nomcompagnie) VALUES(?)'
SELECT_COMPAGNIE = 'SELECT * FROM compagnie'

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
)'''
DROP_MODULES = 'DROP TABLE IF EXISTS modules'
INSERT_MODULES = 'INSERT INTO modules(nom, version, prix_mensuel) VALUES(?, ?)'
SELECT_MODULES = 'SELECT * FROM modules'


class Dao():
    __creer = [
        CREER_MODULE,
        CREER_COMPAGNIE,
        CREER_MEMBRE
    ]
    __detruire = [
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

    # ***************** AJOUTER METHODE DA0 *********************
    def insert_membre(self, prenom, nom, identifiant, mdp, titre, permission, id_compagnie):
        self.cur.execute(INSERT_MEMBRE, (prenom, nom, identifiant, mdp, titre, permission, id_compagnie))
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
                compagnie.id,
                compagnie.nom
            FROM membre
            INNER JOIN compagnie
            ON membre.compagnie = compagnie.id
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
