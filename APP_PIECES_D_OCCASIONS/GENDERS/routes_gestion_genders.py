# routes_gestion_genders.py
# OM 2020.04.06 Gestions des "routes" FLASK pour les genders.

from flask import render_template, flash, redirect, url_for, request
from APP_PIECES_D_OCCASIONS import obj_mon_application
from APP_PIECES_D_OCCASIONS.GENDERS.data_gestion_genders import GestionGenders
from APP_PIECES_D_OCCASIONS.DATABASE.erreurs import *
# OM 2020.04.10 Pour utiliser les expressions régulières REGEX
import re


# ---------------------------------------------------------------------------------------------------
# OM 2020.04.07 Définition d'une "route" /genders_afficher
# cela va permettre de programmer les actions avant d'interagir
# avec le navigateur par la méthode "render_template"
# Pour tester http://127.0.0.1:1234/genders_afficher
# ---------------------------------------------------------------------------------------------------
@obj_mon_application.route("/genders_afficher/<string:order_by>/<int:id_genders_sel>", methods=['GET', 'POST'])
def genders_afficher(order_by,id_genders_sel):
    # OM 2020.04.09 Pour savoir si les données d'un formulaire sont un affichage
    # ou un envoi de donnée par des champs du formulaire HTML.
    if request.method == "GET":
        try:
            # OM 2020.04.09 Objet contenant toutes les méthodes pour gérer (CRUD) les données.
            obj_actions_genders = GestionGenders()
            # Récupére les données grâce à une requête MySql définie dans la classe GestionGenders()
            # Fichier data_gestion_genders.py
            data_genders = obj_actions_genders.gender_afficher_data(order_by,id_genders_sel)
            # DEBUG bon marché : Pour afficher un message dans la console.
            print(" data genders", data_genders, "type ", type(data_genders))

            # OM 2020.04.09 La ligns ci-après permet de donner un sentiment rassurant aux utilisateurs.
            flash("Données genders affichées !!", "Success")
        except Exception as erreur:
            print(f"RGG Erreur générale.")
            # OM 2020.04.09 On dérive "Exception" par le "@obj_mon_application.errorhandler(404)" fichier "run_mon_app.py"
            # Ainsi on peut avoir un message d'erreur personnalisé.
            # flash(f"RGG Exception {erreur}")
            raise Exception(f"RGG Erreur générale. {erreur}")
            # raise MaBdErreurOperation(f"RGG Exception {msg_erreurs['ErreurNomBD']['message']} {erreur}")

    # OM 2020.04.07 Envoie la page "HTML" au serveur.
    return render_template("genders/genders_afficher.html", data=data_genders)


# ---------------------------------------------------------------------------------------------------
# OM 2020.04.07 Définition d'une "route" /genders_add ,
# cela va permettre de programmer quelles actions sont réalisées avant de l'envoyer
# au navigateur par la méthode "render_template"
# En cas d'erreur on affiche à nouveau la page "genders_add.html"
# Pour la tester http://127.0.0.1:1234/genders_add
# ---------------------------------------------------------------------------------------------------
@obj_mon_application.route("/genders_add", methods=['GET', 'POST'])
def genders_add():
    # OM 2019.03.25 Pour savoir si les données d'un formulaire sont un affichage
    # ou un envoi de donnée par des champs utilisateurs.

    if request.method == "POST":
        try:
            # OM 2020.04.09 Objet contenant toutes les méthodes pour gérer (CRUD) les données.
            obj_actions_genders = GestionGenders()
            # OM 2020.04.09 Récupère le contenu du champ dans le formulaire HTML "genders_add.html"
            gender = request.form['gender_html']



            # OM 2019.04.04 On ne doit pas accepter des valeurs vides, des valeurs avec des chiffres,
            # des valeurs avec des caractères qui ne sont pas des lettres.
            # Accepte le trait d'union ou l'apostrophe, et l'espace entre deux mots, mais pas plus d'une occurence.
            if not re.match("^([A-Z]|[a-z\u00C0-\u00FF])[A-Za-z\u00C0-\u00FF]*['\\- ]?[A-Za-z\u00C0-\u00FF]+$",
                                gender):
                # OM 2019.03.28 Message humiliant à l'attention de l'utilisateur.
                flash(f"Une entrée...incorrecte !! Pas de chiffres, de caractères spéciaux, d'espace à double, "
                      f"de double apostrophe, de double trait union et ne doit pas être vide.", "Danger")
                # On doit afficher à nouveau le formulaire "genders_add.html" à cause des erreurs de "claviotage"
                return render_template("genders/genders_add.html")
            else:

                # Constitution d'un dictionnaire et insertion dans la BD
                valeurs_insertion_dictionnaire = {"value_gender": gender}
                obj_actions_genders.add_gender_data(valeurs_insertion_dictionnaire)

                # OM 2019.03.25 Les 2 lignes ci-après permettent de donner un sentiment rassurant aux utilisateurs.
                flash(f"Données insérées !!", "Sucess")
                print(f"Données insérées !!")
                # On va interpréter la "route" 'genders_afficher', car l'utilisateur
                # doit voir le nouveau gender qu'il vient d'insérer.
                return redirect(url_for('genders_afficher', order_by='ASC', id_genders_sel=0))

        # OM 2020.04.16 ATTENTION à l'ordre des excepts très important de respecter l'ordre.
        except pymysql.err.IntegrityError as erreur:
            # OM 2020.04.09 On dérive "pymysql.err.IntegrityError" dans "MaBdErreurDoublon" fichier "erreurs.py"
            # Ainsi on peut avoir un message d'erreur personnalisé.
            raise MaBdErreurDoublon(f"RGG pei {msg_erreurs['ErreurDoublonValue']['message']} et son status {msg_erreurs['ErreurDoublonValue']['status']}")

        # OM 2020.04.16 ATTENTION à l'ordre des excepts très important de respecter l'ordre.
        except (pymysql.err.OperationalError,
                pymysql.ProgrammingError,
                pymysql.InternalError,
                TypeError) as erreur:
            flash(f"Autre erreur {erreur}")
            raise MonErreur(f"Autre erreur")

        # OM 2020.04.16 ATTENTION à l'ordre des excepts très important de respecter l'ordre.
        except Exception as erreur:
            # OM 2020.04.09 On dérive "Exception" dans "MaBdErreurConnexion" fichier "erreurs.py"
            # Ainsi on peut avoir un message d'erreur personnalisé.
            raise MaBdErreurConnexion(f"RGG Exception {msg_erreurs['ErreurConnexionBD']['message']} et son status {msg_erreurs['ErreurConnexionBD']['status']}")
    # OM 2020.04.07 Envoie la page "HTML" au serveur.
    return render_template("genders/genders_add.html")


# ---------------------------------------------------------------------------------------------------
# OM 2020.04.07 Définition d'une "route" /genders_edit , cela va permettre de programmer quelles actions sont réalisées avant de l'envoyer
# au navigateur par la méthode "render_template".
# On change la valeur d'un gender de user par la commande MySql "UPDATE"
# ---------------------------------------------------------------------------------------------------
@obj_mon_application.route('/genders_edit', methods=['POST', 'GET'])
def genders_edit():
    # OM 2020.04.07 Les données sont affichées dans un formulaire, l'affichage de la sélection
    # d'une seule ligne choisie par le bouton "edit" dans le formulaire "genders_afficher.html"
    if request.method == 'GET':
        try:
            # Récupérer la valeur de "id_gender" du formulaire html "genders_afficher.html"
            # l'utilisateur clique sur le lien "edit" et on récupére la valeur de "id_gender"
            # grâce à la variable "id_gender_edit_html"
            # <a href="{{ url_for('genders_edit', id_gender_edit_html=row.id_gender) }}">Edit</a>
            id_gender_edit = request.values['id_gender_edit_html']

            # Pour afficher dans la console la valeur de "id_gender_edit", une façon simple de se rassurer,
            # sans utiliser le DEBUGGER
            print(id_gender_edit)

            # Constitution d'un dictionnaire et insertion dans la BD
            valeur_select_dictionnaire = {"value_id_gender": id_gender_edit}

            # OM 2020.04.09 Objet contenant toutes les méthodes pour gérer (CRUD) les données.
            obj_actions_genders = GestionGenders()

            # OM 2019.04.02 La commande MySql est envoyée à la BD
            data_id_gender = obj_actions_genders.edit_gender_data(valeur_select_dictionnaire)
            print("dataIdGender ", data_id_gender, "type ", type(data_id_gender))
            # Message ci-après permettent de donner un sentiment rassurant aux utilisateurs.
            flash(f"Vous editez le genre !!!")

        except (Exception,
                pymysql.err.OperationalError,
                pymysql.ProgrammingError,
                pymysql.InternalError,
                pymysql.IntegrityError,
                TypeError) as erreur:

            # On indique un problème, mais on ne dit rien en ce qui concerne la résolution.
            print("Problème avec la BD ! : %s", erreur)
            # OM 2020.04.09 On dérive "Exception" dans "MaBdErreurConnexion" fichier "erreurs.py"
            # Ainsi on peut avoir un message d'erreur personnalisé.
            raise MaBdErreurConnexion(f"RGG Exception {msg_erreurs['ErreurConnexionBD']['message']}"
                                      f"et son status {msg_erreurs['ErreurConnexionBD']['status']}")

    return render_template('genders/genders_edit.html', data=data_id_gender)


# ---------------------------------------------------------------------------------------------------
# OM 2020.04.07 Définition d'une "route" /genders_update , cela va permettre de programmer quelles actions sont réalisées avant de l'envoyer
# au navigateur par la méthode "render_template".
# On change la valeur d'un gender de user par la commande MySql "UPDATE"
# ---------------------------------------------------------------------------------------------------
@obj_mon_application.route('/genders_update', methods=['POST', 'GET'])
def genders_update():
    # DEBUG bon marché : Pour afficher les méthodes et autres de la classe "flask.request"
    print(dir(request))
    # OM 2020.04.07 Les données sont affichées dans un formulaire, l'affichage de la sélection
    # d'une seule ligne choisie par le bouton "edit" dans le formulaire "genders_afficher.html"
    # Une fois que l'utilisateur à modifié la valeur du gender alors il va appuyer sur le bouton "UPDATE"
    # donc en "POST"
    if request.method == 'POST':
        try:
            # DEBUG bon marché : Pour afficher les valeurs contenues dans le formulaire
            print("request.values ",request.values)

            # Récupérer la valeur de "id_gender" du formulaire html "genders_edit.html"
            # l'utilisateur clique sur le lien "edit" et on récupére la valeur de "id_gender"
            # grâce à la variable "id_gender_edit_html"
            # <a href="{{ url_for('genders_edit', id_gender_edit_html=row.id_gender) }}">Edit</a>
            id_gender_edit = request.values['id_gender_edit_html']

            # Récupère le contenu du champ "gender" dans le formulaire HTML "GendersEdit.html"
            gender = request.values['name_edit_gender_html']
            valeur_edit_list = [{'id_gender': id_gender_edit, 'gender': gender}]
            # On ne doit pas accepter des valeurs vides, des valeurs avec des chiffres,
            # des valeurs avec des caractères qui ne sont pas des lettres.
            # Accepte le trait d'union ou l'apostrophe, et l'espace entre deux mots, mais pas plus d'une occurence.
            if not re.match("^([A-Z]|[a-z\u00C0-\u00FF])[A-Za-z\u00C0-\u00FF]*['\\- ]?[A-Za-z\u00C0-\u00FF]+$", gender):
                # En cas d'erreur, conserve la saisie fausse, afin que l'utilisateur constate sa misérable faute
                # Récupère le contenu du champ "gender" dans le formulaire HTML "GendersEdit.html"
                #gender = request.values['name_edit_gender_html']
                # Message humiliant à l'attention de l'utilisateur.
                flash(f"Une entrée...incorrecte !! Pas de chiffres, de caractères spéciaux, d'espace à double, "
                      f"de double apostrophe, de double trait union et ne doit pas être vide.", "Danger")

                # On doit afficher à nouveau le formulaire "genders_edit.html" à cause des erreurs de "claviotage"
                # Constitution d'une liste pour que le formulaire d'édition "genders_edit.html" affiche à nouveau
                # la possibilité de modifier l'entrée
                # Exemple d'une liste : [{'id_gender': 13, 'gender': 'philosophique'}]
                valeur_edit_list = [{'id_gender': id_gender_edit, 'gender': gender}]

                # DEBUG bon marché :
                # Pour afficher le contenu et le type de valeurs passées au formulaire "genders_edit.html"
                print(valeur_edit_list, "type ..",  type(valeur_edit_list))
                return render_template('genders/genders_edit.html', data=valeur_edit_list)
            else:
                # Constitution d'un dictionnaire et insertion dans la BD
                valeur_update_dictionnaire = {"value_id_gender": id_gender_edit, "value_gender": gender}

                # OM 2020.04.09 Objet contenant toutes les méthodes pour gérer (CRUD) les données.
                obj_actions_genders = GestionGenders()

                # La commande MySql est envoyée à la BD
                data_id_gender = obj_actions_genders.update_gender_data(valeur_update_dictionnaire)
                # DEBUG bon marché :
                print("dataIdGender ", data_id_gender, "type ", type(data_id_gender))
                # Message ci-après permettent de donner un sentiment rassurant aux utilisateurs.
                flash(f"Editer le gender d'un film !!!")
                # On affiche les genders
                return redirect(url_for('genders_afficher', order_by='ASC', id_genders_sel=0))

        except (Exception,
                pymysql.err.OperationalError,
                pymysql.ProgrammingError,
                pymysql.InternalError,
                pymysql.IntegrityError,
                TypeError) as erreur:

            print(erreur.args)
            flash(f"problème genders update{erreur.args[0]}")
            # En cas de problème, mais surtout en cas de non respect
            # des régles "REGEX" dans le champ "name_edit_gender_html" alors on renvoie le formulaire "EDIT"
            return render_template('genders/genders_edit.html', data=valeur_edit_list)

    return render_template("genders/genders_update.html")


# ---------------------------------------------------------------------------------------------------
# OM 2020.04.07 Définition d'une "route" /genders_select_delete , cela va permettre de programmer quelles actions sont réalisées avant de l'envoyer
# au navigateur par la méthode "render_template".
# On change la valeur d'un gender de user par la commande MySql "UPDATE"
# ---------------------------------------------------------------------------------------------------
@obj_mon_application.route('/genders_select_delete', methods=['POST', 'GET'])
def genders_select_delete():

    if request.method == 'GET':
        try:

            # OM 2020.04.09 Objet contenant toutes les méthodes pour gérer (CRUD) les données.
            obj_actions_genders = GestionGenders()
            # OM 2019.04.04 Récupérer la valeur de "idGenderDeleteHTML" du formulaire html "GendersDelete.html"
            id_gender_delete = request.args.get('id_gender_delete_html')

            # Constitution d'un dictionnaire et insertion dans la BD
            valeur_delete_dictionnaire = {"value_id_gender": id_gender_delete}


            # OM 2019.04.02 La commande MySql est envoyée à la BD
            data_id_gender = obj_actions_genders.delete_select_gender_data(valeur_delete_dictionnaire)
            flash(f"EFFACER et c'est terminé pour cette \"POV\" valeur !!!")

        except (Exception,
                pymysql.err.OperationalError,
                pymysql.ProgrammingError,
                pymysql.InternalError,
                pymysql.IntegrityError,
                TypeError) as erreur:
            # Communiquer qu'une erreur est survenue.
            # DEBUG bon marché : Pour afficher un message dans la console.
            print(f"Erreur genders_delete {erreur.args[0], erreur.args[1]}")
            # C'est une erreur à signaler à l'utilisateur de cette application WEB.
            flash(f"Erreur genders_delete {erreur.args[0], erreur.args[1]}")

    # Envoie la page "HTML" au serveur.
    return render_template('genders/genders_delete.html', data = data_id_gender)


# ---------------------------------------------------------------------------------------------------
# OM 2019.04.02 Définition d'une "route" /gendersUpdate , cela va permettre de programmer quelles actions sont réalisées avant de l'envoyer
# au navigateur par la méthode "render_template".
# Permettre à l'utilisateur de modifier un gender, et de filtrer son entrée grâce à des expressions régulières REGEXP
# ---------------------------------------------------------------------------------------------------
@obj_mon_application.route('/genders_delete', methods=['POST', 'GET'])
def genders_delete():

    # OM 2019.04.02 Pour savoir si les données d'un formulaire sont un affichage ou un envoi de donnée par des champs utilisateurs.
    if request.method == 'POST':
        try:
            # OM 2020.04.09 Objet contenant toutes les méthodes pour gérer (CRUD) les données.
            obj_actions_genders = GestionGenders()
            # OM 2019.04.02 Récupérer la valeur de "id_gender" du formulaire html "GendersAfficher.html"
            id_gender_delete = request.form['id_gender_delete_html']
            # Constitution d'un dictionnaire et insertion dans la BD
            valeur_delete_dictionnaire = {"value_id_gender": id_gender_delete}

            data_genders = obj_actions_genders.delete_gender_data(valeur_delete_dictionnaire)
            # OM 2019.04.02 On va afficher la liste des genders des user
            # OM 2019.04.02 Envoie la page "HTML" au serveur. On passe un message d'information dans "message_html"

            # On affiche les genders
            return redirect(url_for('genders_afficher', order_by='ASC', id_genders_sel=0))



        except (pymysql.err.OperationalError, pymysql.ProgrammingError, pymysql.InternalError, pymysql.IntegrityError,
                TypeError) as erreur:
            # OM 2020.04.09 Traiter spécifiquement l'erreur MySql 1451
            # Cette erreur 1451, signifie qu'on veut effacer un "gender" de user qui est associé dans "t_genders_films".
            if erreur.args[0] == 1451:
                # C'est une erreur à signaler à l'utilisateur de cette application WEB.
                flash('IMPOSSIBLE d\'effacer !!! Cette valeur est associée à des user !')
                # DEBUG bon marché : Pour afficher un message dans la console.
                print(f"IMPOSSIBLE d'effacer !! Ce gender est associé à des user dans la t_genders_films !!! : {erreur}")
                # Afficher la liste des genders des user
                return redirect(url_for('genders_afficher', order_by='ASC', id_genders_sel=0))
            else:
                # Communiquer qu'une autre erreur que la 1062 est survenue.
                # DEBUG bon marché : Pour afficher un message dans la console.
                print(f"Erreur genders_delete {erreur.args[0], erreur.args[1]}")
                # C'est une erreur à signaler à l'utilisateur de cette application WEB.
                flash(f"Erreur genders_delete {erreur.args[0], erreur.args[1]}")


            # OM 2019.04.02 Envoie la page "HTML" au serveur.
    return render_template('genders/genders_afficher.html', data=data_genders)