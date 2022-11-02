from Serveur.DAO.dao import Dao


def insert(dao):
    dao.insert_compagnie('Montreal', 'Canada', 'Quebec', 'Montréal')
    dao.insert_compagnie('Laval', 'Canada', 'Quebec', 'Montréal')
    dao.insert_compagnie('Brassard', 'Canada', 'Quebec', 'Montréal')

    dao.insert_membre('To', 'To', identifiant='toto', mdp='totototo', titre='admin', genre='homme',
                      id_compagnie=2, permission='ALL', nom_access='Dieu')
    dao.insert_membre('Ta', 'Ta', identifiant='tata', mdp='tatatata', titre='admin', genre='femme',
                      id_compagnie=1, permission='ALL', nom_access='Mike')
    dao.insert_membre('ge', 'ge', identifiant='gege', mdp='gegegege', titre='admin', genre='homme',
                      id_compagnie=1, permission='ALL', nom_access='Concierge')
    dao.insert_module('valorant', '3.19', '37.77', 'C:\\Users\\1569047\\Pictures\\Saved')
    dao.insert_module('League', '4.20', '50.80', 'C:\\Users\\1569047\\Pictures')
    achat_module(dao, 1, 1)
    achat_module(dao, 1, 2)


def achat_module(dao, id_compagnie, id_module):
    dao.insert_module_pour_compagnie(id_compagnie, id_module)


def select_main_tables(dao):
    print('\nCompagnie')
    for rangee in dao.select_all_compagnies():
        print(rangee)

    print('\nMembre')
    for rangee in dao.select_all_membres():
        print(rangee)

    print('\n Id des Membre dans compagnie')
    for rangee in dao.select_membres_all_compagnie():
        print(rangee)

    print('\nModules')
    for rangee in dao.select_all_modules():
        print(rangee)

    print('\nAccès')
    for rangee in dao.select_all_access():
        print(rangee)


def select_link_tables(dao):
    print('\nModules par compagnie')
    for rangee in dao.select_all_modules_all_compagnies():
        print(f'id: {rangee[0]} -- id_compagnie: {rangee[1]} -- id_module: {rangee[2]}')

    print('\nModule par access')
    for rangee in dao.select_all_module_par_acces():
        print(f'id: {rangee[0]} -- id_module: {rangee[1]} -- id_access: {rangee[2]}')

    print('\nAcces par membre')
    for rangee in dao.select_all_acces_membres():
        print(f'id: {rangee[0]} -- id_membre: {rangee[1]} -- id_access: {rangee[2]}')


def delete(dao):
    dao.delete_membre('toto')


def get_id(dao):
    print("\nMon id membre", dao.get_membre_id('toto'))
    print("Mon id module", dao.get_module_id('valorant', '3.19'))


def update(dao):
    # dao.update_membre(identifiant='toto', prenom='Mike', nom='Toto', titre='Champion', permission_membre='Chef', nom_compagnie='Laval')
    dao.insert_modules_pour_acces(1, [1, 2])


def main():
    bd = Dao()
    bd.creer_bd()
    insert(bd)
    update(bd)
    select_main_tables(bd)
    select_link_tables(bd)
    return 0


if __name__ == '__main__':
    quit(main())
