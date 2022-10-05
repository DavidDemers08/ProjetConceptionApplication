from Serveur.DAO.dao import Dao


def insert(dao):
    dao.insert_compagnie('Montreal', 'Canada', 'Quebec', 'Montréal')
    dao.insert_compagnie('Laval', 'Canada', 'Quebec', 'Montréal')
    dao.insert_compagnie('Brassard', 'Canada', 'Quebec', 'Montréal')

    dao.insert_membre('To', 'To', identifiant='toto', mdp='totototo', titre='admin', genre='homme',
                      id_compagnie=2, permission='ALL')
    dao.insert_membre('Ta', 'Ta', identifiant='tata', mdp='tatatata', titre='admin', genre='femme',
                      id_compagnie=1, permission='ALL')


def select(dao):
    print('\nCompagnie')
    for rangee in dao.select_all_compagnies():
        print(rangee)

    print('\nMembre')
    for rangee in dao.select_all_membres():
        print(rangee)

    print('\nMembre dans compagnie')
    for rangee in dao.select_membres_all_compagnie():
        print(rangee)


def main():
    bd = Dao()
    bd.creer_bd()
    insert(bd)
    select(bd)

    print('\nIdentifier l\'usager')
    print(bd.identifier_usager('toto', 'totototo'))

    return 0


if __name__ == '__main__':
    quit(main())
