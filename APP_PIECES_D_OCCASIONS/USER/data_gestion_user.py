# data_gestion_user.py
# OM 2698.03.21 Permet de gérer (CRUD) les données de la table t_user
from flask import flash
from APP_PIECES_D_OCCASIONS.DATABASE.connect_db_context_manager import MaBaseDeDonnee
from APP_PIECES_D_OCCASIONS.DATABASE.erreurs import *


class GestionUser:
    def __init__(self):
        try:
            print("dans le try de gestions user")
            # OM 2020.04.11 La connexion à la base de données est-elle active ?
            # Renvoie une erreur si la connexion est perdue.
            MaBaseDeDonnee().connexion_bd.ping(False)
        except Exception as erreur:
            flash("Dans Gestion user ...terrible erreur, il faut connecter une base de donnée", "Danger")
            # DEBUG bon marché : Pour afficher un message dans la console.
            print(f"Exception grave Classe constructeur GestionGenres {erreur.args[0]}")
            raise MaBdErreurConnexion(f"{msg_erreurs['ErreurConnexionBD']['message']} {erreur.args[0]}")
        print("Classe constructeur GestionUser ")

    def user_afficher_data(self):
        try:
            # OM 2020.04.07 C'EST LA QUE VOUS ALLEZ DEVOIR PLACER VOTRE PROPRE LOGIQUE MySql
            # la commande MySql classique est "SELECT * FROM t_user"
            # Pour "lever"(raise) une erreur s'il y a des erreurs sur les noms d'attributs dans la table
            # donc, je précise les champs à afficher
            strsql_user_afficher = """SELECT id_user, firstname_user, lastname_user, mail, phone, address, city, npa, gender, date_user FROM t_user INNER JOIN t_gender ON t_user.fk_gender = t_gender.id_gender ORDER BY id_user ASC"""
            # Du fait de l'utilisation des "context managers" on accède au curseur grâce au "with".
            with MaBaseDeDonnee().connexion_bd.cursor() as mc_afficher:
                # Envoi de la commande MySql
                mc_afficher.execute(strsql_user_afficher)
                # Récupère les données de la requête.
                data_user = mc_afficher.fetchall()
                # Affichage dans la console
                print("data_user ", data_user, " Type : ", type(data_user))
                # Retourne les données du "SELECT"
                return data_user
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

    def add_user_data(self, valeurs_insertion_dictionnaire):
        try:
            print(valeurs_insertion_dictionnaire)
            # OM 2020.04.07 C'EST LA QUE VOUS ALLEZ DEVOIR PLACER VOTRE PROPRE LOGIQUE MySql

            strsql_insert_user = """INSERT INTO t_user (id_user, firstname_user, lastname_user, mail, phone, address, city, npa, fk_gender, date_user) 
                                    VALUES (NULL, %(value_firstname_user)s, %(value_lastname_user)s, %(value_mail)s, %(value_phone)s, %(value_address)s, %(value_city)s, %(value_npa)s, %(value_gender)s, %(value_date_user)s);"""
            # Du fait de l'utilisation des "context managers" on accède au curseur grâce au "with".
            # la subtilité consiste à avoir une méthode "mabd_execute" dans la classe "MaBaseDeDonnee"
            # ainsi quand elle aura terminé l'insertion des données le destructeur de la classe "MaBaseDeDonnee"
            # sera interprété, ainsi on fera automatiquement un commit
            with MaBaseDeDonnee() as mconn_bd:
                # mconn_bd.mabd_execute(strsql_insert_user, valeurs_insertion_dictionnaire)
                mconn_bd.mabd_execute(strsql_insert_user, valeurs_insertion_dictionnaire)


        except pymysql.err.IntegrityError as erreur:
            # OM 2020.04.09 On dérive "pymysql.err.IntegrityError" dans "MaBdErreurDoublon" fichier "erreurs.py"
            # Ainsi on peut avoir un message d'erreur personnalisé.
            raise MaBdErreurDoublon(f"DGG pei erreur doublon {msg_erreurs['ErreurDoublonValue']['message']} et son status {msg_erreurs['ErreurDoublonValue']['status']}")

    def edit_user_data(self, valeur_id_dictionnaire):
            try:
                print(valeur_id_dictionnaire)
                # OM 2020.04.07 C'EST LA QUE VOUS ALLEZ DEVOIR PLACER VOTRE PROPRE LOGIQUE MySql
                # Commande MySql pour afficher le user sélectionné dans le tableau dans le formulaire HTML
                str_sql_id_user = "SELECT id_user, firstname_user, lastname_user, mail, phone, address, city, npa, gender, date_user FROM t_user INNER JOIN t_gender ON t_user.fk_gender = t_gender.id_gender WHERE id_user = %(value_id_user)s"

                # Du fait de l'utilisation des "context managers" on accède au curseur grâce au "with".
                # la subtilité consiste à avoir une méthode "mabd_execute" dans la classe "MaBaseDeDonnee"
                # ainsi quand elle aura terminé l'insertion des données le destructeur de la classe "MaBaseDeDonnee"
                # sera interprété, ainsi on fera automatiquement un commit
                with MaBaseDeDonnee().connexion_bd as mconn_bd:
                    with mconn_bd as mc_cur:
                        mc_cur.execute(str_sql_id_user, valeur_id_dictionnaire)
                        data_one = mc_cur.fetchall()
                        print("valeur_id_dictionnaire...", data_one)
                        return data_one

            except Exception as erreur:
                # OM 2020.03.01 Message en cas d'échec du bon déroulement des commandes ci-dessus.
                print(f"Problème edit_user_data Data Gestions User numéro de l'erreur : {erreur}")
                # flash(f"Flash. Problèmes Data Gestions User numéro de l'erreur : {erreur}", "danger")
                # OM 2020.04.09 On dérive "Exception" par le "@obj_mon_application.errorhandler(404)" fichier "run_mon_app.py"
                # Ainsi on peut avoir un message d'erreur personnalisé.
                raise Exception(
                    "Raise exception... Problème edit_user_data d'un user Data Gestions User {erreur}")

    def update_user_data(self, valeur_update_dictionnaire):
        try:
            print(valeur_update_dictionnaire)
            # OM 2019.04.02 Commande MySql pour la MODIFICATION de la valeur "CLAVIOTTEE" dans le champ "nameEditIntituleUserHTML" du form HTML "UserEdit.html"
            # le "%s" permet d'éviter des injections SQL "simples"
            # <td><input type = "text" name = "nameEditIntituleUserHTML" value="{{ row.intitule_user }}"/></td>
            str_sql_update_user = "UPDATE t_user SET firstname_user = %(value_firstname_user)s, lastname_user = %(value_lastname_user)s , mail = %(value_mail)s, phone = %(value_phone)s, address = %(value_address)s, city = %(value_city)s, npa = %(value_npa)s, fk_gender = %(value_gender)s, date_user = %(value_date_user)s WHERE id_user = %(value_id_user)s"

            # Du fait de l'utilisation des "context managers" on accède au curseur grâce au "with".
            # la subtilité consiste à avoir une méthode "mabd_execute" dans la classe "MaBaseDeDonnee"
            # ainsi quand elle aura terminé l'insertion des données le destructeur de la classe "MaBaseDeDonnee"
            # sera interprété, ainsi on fera automatiquement un commit
            with MaBaseDeDonnee().connexion_bd as mconn_bd:
                with mconn_bd as mc_cur:
                    mc_cur.execute(str_sql_update_user, valeur_update_dictionnaire)

        except (Exception,
                pymysql.err.OperationalError,
                pymysql.ProgrammingError,
                pymysql.InternalError,
                pymysql.IntegrityError,
                TypeError) as erreur:
            # OM 2020.03.01 Message en cas d'échec du bon déroulement des commandes ci-dessus.
            print(f"Problème update_user_data Data Gestions User numéro de l'erreur : {erreur}")
            # flash(f"Flash. Problèmes Data Gestions User numéro de l'erreur : {erreur}", "danger")
            # raise Exception('Raise exception... Problème update_user_data d\'un user Data Gestions User {}'.format(str(erreur)))
            if erreur.args[0] == 1062:
                flash(f"Flash. Cette valeur existe déjà : {erreur}", "danger")
                # Deux façons de communiquer une erreur causée par l'insertion d'une valeur à double.
                flash('Doublon !!! Introduire une valeur différente')
                # Message en cas d'échec du bon déroulement des commandes ci-dessus.
                print(f"Problème update_user_data Data Gestions User numéro de l'erreur : {erreur}")

                raise Exception("Raise exception... Problème update_user_data d'un user DataGestionsUser {erreur}")

    def delete_select_user_data(self, valeur_delete_dictionnaire):
        try:
            print(valeur_delete_dictionnaire)
            # OM 2019.04.02 Commande MySql pour la MODIFICATION de la valeur "CLAVIOTTEE" dans le champ "nameEditIntituleUserHTML" du form HTML "UserEdit.html"
            # le "%s" permet d'éviter des injections SQL "simples"
            # <td><input type = "text" name = "nameEditIntituleUserHTML" value="{{ row.intitule_user }}"/></td>

            # OM 2020.04.07 C'EST LA QUE VOUS ALLEZ DEVOIR PLACER VOTRE PROPRE LOGIQUE MySql
            # Commande MySql pour afficher le user sélectionné dans le tableau dans le formulaire HTML
            str_sql_select_id_user = "SELECT id_user, firstname_user, lastname_user, mail, phone, address, city, npa, gender, date_user FROM t_user INNER JOIN t_gender ON t_user.fk_gender = t_gender.id_gender WHERE id_user = %(value_id_user)s"

            # Du fait de l'utilisation des "context managers" on accède au curseur grâce au "with".
            # la subtilité consiste à avoir une gméthode "mabd_execute" dans la classe "MaBaseDeDonnee"
            # ainsi quand elle aura terminé l'insertion des données le destructeur de la classe "MaBaseDeDonnee"
            # sera interprété, ainsi on fera automatiquement un commit
            with MaBaseDeDonnee().connexion_bd as mconn_bd:
                with mconn_bd as mc_cur:
                    mc_cur.execute(str_sql_select_id_user, valeur_delete_dictionnaire)
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
            print(f"Problème delete_select_user_data Gestions User numéro de l'erreur : {erreur}")
            # C'est une erreur à signaler à l'utilisateur de cette application WEB.
            flash(f"Flash. Problème delete_select_user_data numéro de l'erreur : {erreur}", "danger")
            raise Exception(
                "Raise exception... Problème delete_select_user_data d\'un user Data Gestions User {erreur}")

    def delete_user_data(self, valeur_delete_dictionnaire):
        try:
            print(valeur_delete_dictionnaire)
            # OM 2019.04.02 Commande MySql pour EFFACER la valeur sélectionnée par le "bouton" du form HTML "UserEdit.html"
            # le "%s" permet d'éviter des injections SQL "simples"
            # <td><input type = "text" name = "nameEditIntituleUserHTML" value="{{ row.intitule_user }}"/></td>
            str_sql_delete_user = "DELETE FROM t_user WHERE id_user = %(value_id_user)s"

            # Du fait de l'utilisation des "context managers" on accède au curseur grâce au "with".
            # la subtilité consiste à avoir une méthode "mabd_execute" dans la classe "MaBaseDeDonnee"
            # ainsi quand elle aura terminé l'insertion des données le destructeur de la classe "MaBaseDeDonnee"
            # sera interprété, ainsi on fera automatiquement un commit
            with MaBaseDeDonnee().connexion_bd as mconn_bd:
                with mconn_bd as mc_cur:
                    mc_cur.execute(str_sql_delete_user, valeur_delete_dictionnaire)
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
            print(f"Problème delete_user_data Data Gestions User numéro de l'erreur : {erreur}")
            # flash(f"Flash. Problèmes Data Gestions User numéro de l'erreur : {erreur}", "danger")
            if erreur.args[0] == 1451:
                # OM 2020.04.09 Traitement spécifique de l'erreur 1451 Cannot delete or update a parent row: a foreign key constraint fails
                # en MySql le moteur INNODB empêche d'effacer un user qui est associé à un film dans la table intermédiaire "t_user_films"
                # il y a une contrainte sur les FK de la table intermédiaire "t_user_films"
                # C'est une erreur à signaler à l'utilisateur de cette application WEB.
                # flash(f"Flash. IMPOSSIBLE d'effacer !!! Ce user est associé à des user dans la t_user_films !!! : {erreur}", "danger")
                # DEBUG bon marché : Pour afficher un message dans la console.
                print(
                    f"IMPOSSIBLE d'effacer !!! Ce user est associé à des films dans la t_user_films !!! : {erreur}")
            raise MaBdErreurDelete(f"DGG Exception {msg_erreurs['ErreurDeleteContrainte']['message']} {erreur}")

