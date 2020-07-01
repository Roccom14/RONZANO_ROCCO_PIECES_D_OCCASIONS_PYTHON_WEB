# data_gestion_user.py
# OM 2698.03.21 Permet de gérer (CRUD) les données de la table t_user
from flask import flash
from APP_PIECES_D_OCCASIONS.DATABASE.connect_db_context_manager import MaBaseDeDonnee
from APP_PIECES_D_OCCASIONS.DATABASE.erreurs import *


class GestionStuff:
    def __init__(self):
        try:
            print("dans le try de gestions stuff")
            # OM 2020.04.11 La connexion à la base de données est-elle active ?
            # Renvoie une erreur si la connexion est perdue.
            MaBaseDeDonnee().connexion_bd.ping(False)
        except Exception as erreur:
            flash("Dans Gestion stuff ...terrible erreur, il faut connecter une base de donnée", "Danger")
            # DEBUG bon marché : Pour afficher un message dans la console.
            print(f"Exception grave Classe constructeur GestionStuff {erreur.args[0]}")
            raise MaBdErreurConnexion(f"{msg_erreurs['ErreurConnexionBD']['message']} {erreur.args[0]}")
        print("Classe constructeur GestionStuff ")

    def stuff_afficher_data(self):
        try:
            # OM 2020.04.07 C'EST LA QUE VOUS ALLEZ DEVOIR PLACER VOTRE PROPRE LOGIQUE MySql
            # la commande MySql classique est "SELECT * FROM t_user"
            # Pour "lever"(raise) une erreur s'il y a des erreurs sur les noms d'attributs dans la table
            # donc, je précise les champs à afficher
            strsql_stuff_afficher = """SELECT * FROM t_stuff 
                                        INNER JOIN t_user ON t_stuff.fk_user = t_user.id_user 
                                        INNER JOIN t_state_stuff ON t_stuff.fk_state_stuff = t_state_stuff.id_state_stuff 
                                        INNER JOIN t_type_payment ON t_stuff.fk_type_payment = t_type_payment.id_type_payment ORDER BY id_stuff ASC"""
            # Du fait de l'utilisation des "context managers" on accède au curseur grâce au "with".
            with MaBaseDeDonnee().connexion_bd.cursor() as mc_afficher:
                # Envoi de la commande MySql
                mc_afficher.execute(strsql_stuff_afficher)
                # Récupère les données de la requête.
                data_stuff = mc_afficher.fetchall()
                # Affichage dans la console
                print("data_stuff ", data_stuff, " Type : ", type(data_stuff))
                # Retourne les données du "SELECT"
                return data_stuff
        except pymysql.Error as erreur:
            print(f"DGF gad pymysql errror {erreur.args[0]} {erreur.args[1]}")
            raise  MaBdErreurPyMySl(f"DGG fad pymysql errror {msg_erreurs['ErreurPyMySql']['message']} {erreur.args[0]} {erreur.args[1]}")
        except Exception as erreur:
            print(f"DGF gad Exception {erreur.args}")
            raise MaBdErreurConnexion(f"DGG fad Exception {msg_erreurs['ErreurConnexionBD']['message']} {erreur.args}")
        except pymysql.err.IntegrityError as erreur:
            # OM 2020.04.09 On dérive "pymysql.err.IntegrityError" dans "MaBdErreurDoublon" fichier "erreurs.py"
            # Ainsi on peut avoir un message d'erreur personnalisé.
            raise MaBdErreurConnexion(f"DGF fad pei {msg_erreurs['ErreurConnexionBD']['message']} {erreur.args[1]}")

    def add_stuff_data(self, valeurs_insertion_dictionnaire):
        try:
            print(valeurs_insertion_dictionnaire)
            # OM 2020.04.07 C'EST LA QUE VOUS ALLEZ DEVOIR PLACER VOTRE PROPRE LOGIQUE MySql

            strsql_insert_stuff = """INSERT INTO t_stuff (id_stuff, name_stuff, description_stuff, price_stuff, 
                                        type_stuff, quantity_stuff, fk_user, fk_state_stuff, fk_type_payment, date_add_stuff, date_bought_stuff) 
                                    VALUES (NULL, %(value_name_stuff)s, %(value_description_stuff)s, 
                                    %(value_price_stuff)s, %(value_type_stuff)s, %(value_quantity_stuff)s,
                                    %(value_user)s, %(value_state_stuff)s, %(value_type_payment)s,
                                    %(value_date_add_stuff)s, %(value_date_bought_stuff)s);"""
            # Du fait de l'utilisation des "context managers" on accède au curseur grâce au "with".
            # la subtilité consiste à avoir une méthode "mabd_execute" dans la classe "MaBaseDeDonnee"
            # ainsi quand elle aura terminé l'insertion des données le destructeur de la classe "MaBaseDeDonnee"
            # sera interprété, ainsi on fera automatiquement un commit
            with MaBaseDeDonnee() as mconn_bd:
                # mconn_bd.mabd_execute(strsql_insert_user, valeurs_insertion_dictionnaire)
                mconn_bd.mabd_execute(strsql_insert_stuff, valeurs_insertion_dictionnaire)


        except pymysql.err.IntegrityError as erreur:
            # OM 2020.04.09 On dérive "pymysql.err.IntegrityError" dans "MaBdErreurDoublon" fichier "erreurs.py"
            # Ainsi on peut avoir un message d'erreur personnalisé.
            raise MaBdErreurDoublon(f"DGG pei erreur doublon {msg_erreurs['ErreurDoublonValue']['message']} et son status {msg_erreurs['ErreurDoublonValue']['status']}")

    def edit_stuff_data(self, valeur_id_dictionnaire):
            try:
                print(valeur_id_dictionnaire)
                # OM 2020.04.07 C'EST LA QUE VOUS ALLEZ DEVOIR PLACER VOTRE PROPRE LOGIQUE MySql
                # Commande MySql pour afficher le user sélectionné dans le tableau dans le formulaire HTML
                str_sql_id_stuff = """SELECT * FROM t_stuff 
                                        INNER JOIN t_user ON t_stuff.fk_user = t_user.id_user 
                                        INNER JOIN t_state_stuff ON t_stuff.fk_state_stuff = t_state_stuff.id_state_stuff 
                                        INNER JOIN t_type_payment ON t_stuff.fk_type_payment = t_type_payment.id_type_payment WHERE id_stuff = %(value_id_stuff)s"""

                # Du fait de l'utilisation des "context managers" on accède au curseur grâce au "with".
                # la subtilité consiste à avoir une méthode "mabd_execute" dans la classe "MaBaseDeDonnee"
                # ainsi quand elle aura terminé l'insertion des données le destructeur de la classe "MaBaseDeDonnee"
                # sera interprété, ainsi on fera automatiquement un commit
                with MaBaseDeDonnee().connexion_bd as mconn_bd:
                    with mconn_bd as mc_cur:
                        mc_cur.execute(str_sql_id_stuff, valeur_id_dictionnaire)
                        data_one = mc_cur.fetchall()
                        print("valeur_id_dictionnaire...", data_one)
                        return data_one

            except Exception as erreur:
                # OM 2020.03.01 Message en cas d'échec du bon déroulement des commandes ci-dessus.
                print(f"Problème edit_stuff_data Data Gestions stuff numéro de l'erreur : {erreur}")
                # flash(f"Flash. Problèmes Data Gestions User numéro de l'erreur : {erreur}", "danger")
                # OM 2020.04.09 On dérive "Exception" par le "@obj_mon_application.errorhandler(404)" fichier "run_mon_app.py"
                # Ainsi on peut avoir un message d'erreur personnalisé.
                raise Exception(
                    "Raise exception... Problème edit_user_data d'un user Data Gestions Stuff {erreur}")

    def update_stuff_data(self, valeur_update_dictionnaire):
        try:
            print(valeur_update_dictionnaire)
            # OM 2019.04.02 Commande MySql pour la MODIFICATION de la valeur "CLAVIOTTEE" dans le champ "nameEditIntituleUserHTML" du form HTML "UserEdit.html"
            # le "%s" permet d'éviter des injections SQL "simples"
            # <td><input type = "text" name = "nameEditIntituleUserHTML" value="{{ row.intitule_user }}"/></td>
            str_sql_update_stuff = """UPDATE t_stuff SET name_stuff = %(value_name_stuff)s, description_stuff = %(value_description_stuff)s, price_stuff = %(value_price_stuff)s, type_stuff = %(value_type_stuff)s, quantity_stuff = %(value_quantity_stuff)s, fk_user = %(value_user)s, fk_state_stuff = %(value_state_stuff)s, fk_type_payment = %(value_type_payment)s, date_add_stuff = %(value_date_add_stuff)s, date_bought_stuff = %(value_date_bought_stuff)s WHERE id_stuff = %(value_id_stuff)s"""

            # Du fait de l'utilisation des "context managers" on accède au curseur grâce au "with".
            # la subtilité consiste à avoir une méthode "mabd_execute" dans la classe "MaBaseDeDonnee"
            # ainsi quand elle aura terminé l'insertion des données le destructeur de la classe "MaBaseDeDonnee"
            # sera interprété, ainsi on fera automatiquement un commit
            with MaBaseDeDonnee().connexion_bd as mconn_bd:
                with mconn_bd as mc_cur:
                    mc_cur.execute(str_sql_update_stuff, valeur_update_dictionnaire)

        except (Exception,
                pymysql.err.OperationalError,
                pymysql.ProgrammingError,
                pymysql.InternalError,
                pymysql.IntegrityError,
                TypeError) as erreur:
            # OM 2020.03.01 Message en cas d'échec du bon déroulement des commandes ci-dessus.
            print(f"Problème update_stuff_data Data Gestions Stuff numéro de l'erreur : {erreur}")
            # flash(f"Flash. Problèmes Data Gestions User numéro de l'erreur : {erreur}", "danger")
            # raise Exception('Raise exception... Problème update_user_data d\'un user Data Gestions User {}'.format(str(erreur)))
            if erreur.args[0] == 1062:
                flash(f"Flash. Cette valeur existe déjà : {erreur}", "danger")
                # Deux façons de communiquer une erreur causée par l'insertion d'une valeur à double.
                flash('Doublon !!! Introduire une valeur différente')
                # Message en cas d'échec du bon déroulement des commandes ci-dessus.
                print(f"Problème update_stuff_data Data Gestions Stuff numéro de l'erreur : {erreur}")

                raise Exception("Raise exception... Problème update_stuff_data d'un user DataGestionsStuff {erreur}")

    def delete_select_stuff_data(self, valeur_delete_dictionnaire):
        try:
            print(valeur_delete_dictionnaire)
            # OM 2019.04.02 Commande MySql pour la MODIFICATION de la valeur "CLAVIOTTEE" dans le champ "nameEditIntituleUserHTML" du form HTML "UserEdit.html"
            # le "%s" permet d'éviter des injections SQL "simples"
            # <td><input type = "text" name = "nameEditIntituleUserHTML" value="{{ row.intitule_user }}"/></td>

            # OM 2020.04.07 C'EST LA QUE VOUS ALLEZ DEVOIR PLACER VOTRE PROPRE LOGIQUE MySql
            # Commande MySql pour afficher le user sélectionné dans le tableau dans le formulaire HTML
            str_sql_select_id_stuff = """SELECT id_stuff, name_stuff, description_stuff, price_stuff, type_stuff, quantity_stuff, firstname_user, lastname_user, state_stuff, type_payment, date_add_stuff, date_bought_stuff FROM t_stuff 
                                        INNER JOIN t_user ON t_stuff.fk_user = t_user.id_user 
                                        INNER JOIN t_state_stuff ON t_stuff.fk_state_stuff = t_state_stuff.id_state_stuff 
                                        INNER JOIN t_type_payment ON t_stuff.fk_type_payment = t_type_payment.id_type_payment WHERE id_stuff = %(value_id_stuff)s"""

            # Du fait de l'utilisation des "context managers" on accède au curseur grâce au "with".
            # la subtilité consiste à avoir une gméthode "mabd_execute" dans la classe "MaBaseDeDonnee"
            # ainsi quand elle aura terminé l'insertion des données le destructeur de la classe "MaBaseDeDonnee"
            # sera interprété, ainsi on fera automatiquement un commit
            with MaBaseDeDonnee().connexion_bd as mconn_bd:
                with mconn_bd as mc_cur:
                    mc_cur.execute(str_sql_select_id_stuff, valeur_delete_dictionnaire)
                    data_one = mc_cur.fetchall()
                    print("valeur_id_dictionnaire...", data_one)
                    return data_one

        except (Exception,
                pymysql.err.OperationalError,
                pymysql.ProgrammingError,
                pymysql.InternalError,
                pymysql.IntegrityError,
                TypeError) as erreur:
            # DEBUG bon marché : Pour afficher un message dans la console.
            print(f"Problème delete_select_stuff_data Gestions Stuff numéro de l'erreur : {erreur}")
            # C'est une erreur à signaler à l'utilisateur de cette application WEB.
            flash(f"Flash. Problème delete_select_stuff_data numéro de l'erreur : {erreur}", "danger")
            raise Exception(
                "Raise exception... Problème delete_select_stuff_data d\'un stuff Data Gestions Stuff {erreur}")

    def delete_stuff_data(self, valeur_delete_dictionnaire):
        try:
            print(valeur_delete_dictionnaire)
            # OM 2019.04.02 Commande MySql pour EFFACER la valeur sélectionnée par le "bouton" du form HTML "UserEdit.html"
            # le "%s" permet d'éviter des injections SQL "simples"
            # <td><input type = "text" name = "nameEditIntituleUserHTML" value="{{ row.intitule_user }}"/></td>
            str_sql_delete_stuff = "DELETE FROM t_stuff WHERE id_stuff = %(value_id_stuff)s"

            # Du fait de l'utilisation des "context managers" on accède au curseur grâce au "with".
            # la subtilité consiste à avoir une méthode "mabd_execute" dans la classe "MaBaseDeDonnee"
            # ainsi quand elle aura terminé l'insertion des données le destructeur de la classe "MaBaseDeDonnee"
            # sera interprété, ainsi on fera automatiquement un commit
            with MaBaseDeDonnee().connexion_bd as mconn_bd:
                with mconn_bd as mc_cur:
                    mc_cur.execute(str_sql_delete_stuff, valeur_delete_dictionnaire)
                    data_one = mc_cur.fetchall()
                    print("valeur_id_dictionnaire...", data_one)
                    return data_one
        except (Exception,
                pymysql.err.OperationalError,
                pymysql.ProgrammingError,
                pymysql.InternalError,
                pymysql.IntegrityError,
                TypeError) as erreur:
            # DEBUG bon marché : Pour afficher un message dans la console.
            print(f"Problème delete_stuff_data Data Gestions Stuff numéro de l'erreur : {erreur}")
            # flash(f"Flash. Problèmes Data Gestions Stuff numéro de l'erreur : {erreur}", "danger")
            if erreur.args[0] == 1451:
                # OM 2020.04.09 Traitement spécifique de l'erreur 1451 Cannot delete or update a parent row: a foreign key constraint fails
                # en MySql le moteur INNODB empêche d'effacer un user qui est associé à un film dans la table intermédiaire "t_user_films"
                # il y a une contrainte sur les FK de la table intermédiaire "t_user_films"
                # C'est une erreur à signaler à l'utilisateur de cette application WEB.
                # flash(f"Flash. IMPOSSIBLE d'effacer !!! Ce user est associé à des user dans la t_user_films !!! : {erreur}", "danger")
                # DEBUG bon marché : Pour afficher un message dans la console.
                print(
                    f"IMPOSSIBLE d'effacer !!! Ce stuff est associé à des users dans la t_user !!! : {erreur}")
            raise MaBdErreurDelete(f"DGG Exception {msg_erreurs['ErreurDeleteContrainte']['message']} {erreur}")

