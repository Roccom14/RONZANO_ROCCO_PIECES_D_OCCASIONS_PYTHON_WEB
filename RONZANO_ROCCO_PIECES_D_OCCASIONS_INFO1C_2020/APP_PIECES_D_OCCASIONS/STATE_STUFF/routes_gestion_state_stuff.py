# routes_gestion_genders.py
# OM 2020.04.06 Gestions des "routes" FLASK pour les state_stuff.

from flask import render_template, flash, redirect, url_for, request
from APP_PIECES_D_OCCASIONS import obj_mon_application
from APP_PIECES_D_OCCASIONS.GENDERS.data_gestion_genders import GestionGenders
from APP_PIECES_D_OCCASIONS.DATABASE.erreurs import *
from APP_PIECES_D_OCCASIONS.STATE_STUFF.data_gestion_state_stuff import GestionStateStuff
# OM 2020.04.10 Pour utiliser les expressions régulières REGEX
import re


# ---------------------------------------------------------------------------------------------------
# OM 2020.04.07 Définition d'une "route" /genders_afficher
# cela va permettre de programmer les actions avant d'interagir
# avec le navigateur par la méthode "render_template"
# Pour tester http://127.0.0.1:1234/genders_afficher
# ---------------------------------------------------------------------------------------------------


@obj_mon_application.route("/state_stuff_afficher/<string:order_by>/<int:id_state_stuff_sel>", methods=['GET', 'POST'])
def state_stuff_afficher(order_by, id_state_stuff_sel):
    # OM 2020.04.09 Pour savoir si les données d'un formulaire sont un affichage
    # ou un envoi de donnée par des champs du formulaire HTML.
    if request.method == "GET":
        try:
            # OM 2020.04.09 Objet contenant toutes les méthodes pour gérer (CRUD) les données.
            obj_actions_state_stuff = GestionStateStuff()
            # Récupére les données grâce à une requête MySql définie dans la classe GestionGenders()
            # Fichier data_gestion_genders.py
            data_state_stuff = obj_actions_state_stuff.state_stuff_afficher_data(order_by,id_state_stuff_sel)
            # DEBUG bon marché : Pour afficher un message dans la console.
            print(" data state_stuff", data_state_stuff, "type ", type(data_state_stuff))

            # OM 2020.04.09 La ligns ci-après permet de donner un sentiment rassurant aux utilisateurs.
            flash("Données state_stuff affichées !!", "Success")
        except Exception as erreur:
            print(f"RGG Erreur générale.")
            # OM 2020.04.09 On dérive "Exception" par le "@obj_mon_application.errorhandler(404)" fichier "run_mon_app.py"
            # Ainsi on peut avoir un message d'erreur personnalisé.
            # flash(f"RGG Exception {erreur}")
            raise Exception(f"RGG Erreur générale. {erreur}")
            # raise MaBdErreurOperation(f"RGG Exception {msg_erreurs['ErreurNomBD']['message']} {erreur}")

    # OM 2020.04.07 Envoie la page "HTML" au serveur.
    return render_template("state_stuff/state_stuff_afficher.html", data=data_state_stuff)


# ---------------------------------------------------------------------------------------------------
# OM 2020.04.07 Définition d'une "route" /genders_add ,
# cela va permettre de programmer quelles actions sont réalisées avant de l'envoyer
# au navigateur par la méthode "render_template"
# En cas d'erreur on affiche à nouveau la page "genders_add.html"
# Pour la tester http://127.0.0.1:1234/genders_add
# ---------------------------------------------------------------------------------------------------
@obj_mon_application.route("/state_stuff_add", methods=['GET', 'POST'])
def state_stuff_add():
    # OM 2019.03.25 Pour savoir si les données d'un formulaire sont un affichage
    # ou un envoi de donnée par des champs utilisateurs.
    if request.method == "POST":
        try:
            # OM 2020.04.09 Objet contenant toutes les méthodes pour gérer (CRUD) les données.
            obj_actions_state_stuff = GestionStateStuff()
            # OM 2020.04.09 Récupère le contenu du champ dans le formulaire HTML "state_stuff_add.html"
            state_stuff = request.form['state_stuff_html']

            # OM 2019.04.04 On ne doit pas accepter des valeurs vides, des valeurs avec des chiffres,
            # des valeurs avec des caractères qui ne sont pas des lettres.
            # Accepte le trait d'union ou l'apostrophe, et l'espace entre deux mots, mais pas plus d'une occurence.
            if not re.match("^([A-Z]|[a-z\u00C0-\u00FF])[A-Za-z\u00C0-\u00FF]*['\\- ]?[A-Za-z\u00C0-\u00FF]+$",
                                state_stuff):
                # OM 2019.03.28 Message humiliant à l'attention de l'utilisateur.
                flash(f"Une entrée...incorrecte !! Pas de chiffres, de caractères spéciaux, d'espace à double, "
                      f"de double apostrophe, de double trait union et ne doit pas être vide.", "Danger")
                # On doit afficher à nouveau le formulaire "genders_add.html" à cause des erreurs de "claviotage"
                return render_template("state_stuff/state_stuff_add.html")
            else:

                # Constitution d'un dictionnaire et insertion dans la BD
                valeurs_insertion_dictionnaire = {"value_state_stuff": state_stuff}
                obj_actions_state_stuff.add_state_stuff_data(valeurs_insertion_dictionnaire)

                # OM 2019.03.25 Les 2 lignes ci-après permettent de donner un sentiment rassurant aux utilisateurs.
                flash(f"Données insérées !!", "Sucess")
                print(f"Données insérées !!")
                # On va interpréter la "route" 'genders_afficher', car l'utilisateur
                # doit voir le nouveau state_stuff qu'il vient d'insérer.
                return redirect(url_for('state_stuff_afficher', order_by='ASC', id_state_stuff_sel=0))

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
    return render_template("state_stuff/state_stuff_add.html")


# ---------------------------------------------------------------------------------------------------
# OM 2020.04.07 Définition d'une "route" /genders_edit , cela va permettre de programmer quelles actions sont réalisées avant de l'envoyer
# au navigateur par la méthode "render_template".
# On change la valeur d'un state_stuff de user par la commande MySql "UPDATE"
# ---------------------------------------------------------------------------------------------------
@obj_mon_application.route('/state_stuff_edit', methods=['POST', 'GET'])
def state_stuff_edit():
    # OM 2020.04.07 Les données sont affichées dans un formulaire, l'affichage de la sélection
    # d'une seule ligne choisie par le bouton "edit" dans le formulaire "genders_afficher.html"
    if request.method == 'GET':
        try:
            # Récupérer la valeur de "id_gender" du formulaire html "genders_afficher.html"
            # l'utilisateur clique sur le lien "edit" et on récupére la valeur de "id_gender"
            # grâce à la variable "id_gender_edit_html"
            # <a href="{{ url_for('genders_edit', id_gender_edit_html=row.id_gender) }}">Edit</a>
            id_state_stuff_edit = request.values['id_state_stuff_edit_html']

            # Pour afficher dans la console la valeur de "id_gender_edit", une façon simple de se rassurer,
            # sans utiliser le DEBUGGER
            print(id_state_stuff_edit)

            # Constitution d'un dictionnaire et insertion dans la BD
            valeur_select_dictionnaire = {"value_id_state_stuff": id_state_stuff_edit}

            # OM 2020.04.09 Objet contenant toutes les méthodes pour gérer (CRUD) les données.
            obj_actions_state_stuff = GestionStateStuff()

            # OM 2019.04.02 La commande MySql est envoyée à la BD
            data_id_state_stuff = obj_actions_state_stuff.edit_state_stuff_data(valeur_select_dictionnaire)
            print("dataIdStateStuff ", data_id_state_stuff, "type ", type(data_id_state_stuff))
            # Message ci-après permettent de donner un sentiment rassurant aux utilisateurs.
            flash(f"Editer le state_stuff d'un stuff !!!")

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

    return render_template('state_stuff/state_stuff_edit.html', data=data_id_state_stuff)


# ---------------------------------------------------------------------------------------------------
# OM 2020.04.07 Définition d'une "route" /genders_update , cela va permettre de programmer quelles actions sont réalisées avant de l'envoyer
# au navigateur par la méthode "render_template".
# On change la valeur d'un state_stuff de user par la commande MySql "UPDATE"
# ---------------------------------------------------------------------------------------------------
@obj_mon_application.route('/state_stuff_update', methods=['POST', 'GET'])
def state_stuff_update():
    # DEBUG bon marché : Pour afficher les méthodes et autres de la classe "flask.request"
    print(dir(request))
    # OM 2020.04.07 Les données sont affichées dans un formulaire, l'affichage de la sélection
    # d'une seule ligne choisie par le bouton "edit" dans le formulaire "genders_afficher.html"
    # Une fois que l'utilisateur à modifié la valeur du state_stuff alors il va appuyer sur le bouton "UPDATE"
    # donc en "POST"
    if request.method == 'POST':
        try:
            # DEBUG bon marché : Pour afficher les valeurs contenues dans le formulaire
            print("request.values ", request.values)

            # Récupérer la valeur de "id_gender" du formulaire html "genders_edit.html"
            # l'utilisateur clique sur le lien "edit" et on récupére la valeur de "id_gender"
            # grâce à la variable "id_gender_edit_html"
            # <a href="{{ url_for('genders_edit', id_gender_edit_html=row.id_gender) }}">Edit</a>
            id_state_stuff_edit = request.values['id_state_stuff_edit_html']

            # Récupère le contenu du champ "state_stuff" dans le formulaire HTML "GendersEdit.html"
            state_stuff = request.values['name_edit_state_stuff_html']
            valeur_edit_list = [{'id_state_stuff': id_state_stuff_edit, 'state_stuff': state_stuff}]
            # On ne doit pas accepter des valeurs vides, des valeurs avec des chiffres,
            # des valeurs avec des caractères qui ne sont pas des lettres.
            # Accepte le trait d'union ou l'apostrophe, et l'espace entre deux mots, mais pas plus d'une occurence.
            if not re.match("^([A-Z]|[a-z\u00C0-\u00FF])[A-Za-z\u00C0-\u00FF]*['\\- ]?[A-Za-z\u00C0-\u00FF]+$", state_stuff):
                # En cas d'erreur, conserve la saisie fausse, afin que l'utilisateur constate sa misérable faute
                # Récupère le contenu du champ "state_stuff" dans le formulaire HTML "GendersEdit.html"
                #state_stuff = request.values['name_edit_gender_html']
                # Message humiliant à l'attention de l'utilisateur.
                flash(f"Une entrée...incorrecte !! Pas de chiffres, de caractères spéciaux, d'espace à double, "
                      f"de double apostrophe, de double trait union et ne doit pas être vide.", "Danger")

                # On doit afficher à nouveau le formulaire "genders_edit.html" à cause des erreurs de "claviotage"
                # Constitution d'une liste pour que le formulaire d'édition "genders_edit.html" affiche à nouveau
                # la possibilité de modifier l'entrée
                # Exemple d'une liste : [{'id_gender': 13, 'state_stuff': 'philosophique'}]
                valeur_edit_list = [{'id_state_stuff': id_state_stuff_edit, 'state_stuff': state_stuff}]

                # DEBUG bon marché :
                # Pour afficher le contenu et le type de valeurs passées au formulaire "genders_edit.html"
                print(valeur_edit_list, "type ..",  type(valeur_edit_list))
                return render_template('state_stuff/state_stuff_edit.html', data=valeur_edit_list)
            else:
                # Constitution d'un dictionnaire et insertion dans la BD
                valeur_update_dictionnaire = {"value_id_state_stuff": id_state_stuff_edit, "value_state_stuff": state_stuff}

                # OM 2020.04.09 Objet contenant toutes les méthodes pour gérer (CRUD) les données.
                obj_actions_state_stuff = GestionStateStuff()

                # La commande MySql est envoyée à la BD
                data_id_state_stuff = obj_actions_state_stuff.update_state_stuff_data(valeur_update_dictionnaire)
                # DEBUG bon marché :
                print("dataIdStateStuff ", data_id_state_stuff, "type ", type(data_id_state_stuff))
                # Message ci-après permettent de donner un sentiment rassurant aux utilisateurs.
                flash(f"Editer le state_stuff d'un film !!!")
                # On affiche les state_stuff
                return redirect(url_for('state_stuff_afficher', order_by='ASC', id_state_stuff_sel=0))

        except (Exception,
                pymysql.err.OperationalError,
                pymysql.ProgrammingError,
                pymysql.InternalError,
                pymysql.IntegrityError,
                TypeError) as erreur:

            print(erreur.args)
            flash(f"problème state_stuff update{erreur.args[0]}")
            # En cas de problème, mais surtout en cas de non respect
            # des régles "REGEX" dans le champ "name_edit_gender_html" alors on renvoie le formulaire "EDIT"
            return render_template('state_stuff/state_stuff_edit.html', data=valeur_edit_list)

    return render_template("state_stuff/state_stuff_update.html")


# ---------------------------------------------------------------------------------------------------
# OM 2020.04.07 Définition d'une "route" /genders_select_delete , cela va permettre de programmer quelles actions sont réalisées avant de l'envoyer
# au navigateur par la méthode "render_template".
# On change la valeur d'un state_stuff de user par la commande MySql "UPDATE"
# ---------------------------------------------------------------------------------------------------
@obj_mon_application.route('/state_stuff_select_delete', methods=['POST', 'GET'])
def state_stuff_select_delete():

    if request.method == 'GET':
        try:

            # OM 2020.04.09 Objet contenant toutes les méthodes pour gérer (CRUD) les données.
            obj_actions_state_stuff = GestionStateStuff()
            # OM 2019.04.04 Récupérer la valeur de "idGenderDeleteHTML" du formulaire html "StateStuffDelete.html"
            id_state_stuff_delete = request.args.get('id_state_stuff_delete_html')

            # Constitution d'un dictionnaire et insertion dans la BD
            valeur_delete_dictionnaire = {"value_id_state_stuff": id_state_stuff_delete}


            # OM 2019.04.02 La commande MySql est envoyée à la BD
            data_id_state_stuff = obj_actions_state_stuff.delete_select_state_stuff_data(valeur_delete_dictionnaire)
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
    return render_template('state_stuff/state_stuff_delete.html', data=data_id_state_stuff)


# ---------------------------------------------------------------------------------------------------
# OM 2019.04.02 Définition d'une "route" /gendersUpdate , cela va permettre de programmer quelles actions sont réalisées avant de l'envoyer
# au navigateur par la méthode "render_template".
# Permettre à l'utilisateur de modifier un state_stuff, et de filtrer son entrée grâce à des expressions régulières REGEXP
# ---------------------------------------------------------------------------------------------------
@obj_mon_application.route('/state_stuff_delete', methods=['POST', 'GET'])
def state_stuff_delete():

    # OM 2019.04.02 Pour savoir si les données d'un formulaire sont un affichage ou un envoi de donnée par des champs utilisateurs.
    if request.method == 'POST':
        try:
            # OM 2020.04.09 Objet contenant toutes les méthodes pour gérer (CRUD) les données.
            obj_actions_state_stuff = GestionStateStuff()
            # OM 2019.04.02 Récupérer la valeur de "id_gender" du formulaire html "GendersAfficher.html"
            id_state_stuff_delete = request.form['id_state_stuff_delete_html']
            # Constitution d'un dictionnaire et insertion dans la BD
            valeur_delete_dictionnaire = {"value_id_state_stuff": id_state_stuff_delete}

            data_state_stuff = obj_actions_state_stuff.delete_state_stuff_data(valeur_delete_dictionnaire)
            # OM 2019.04.02 On va afficher la liste des state_stuff des user
            # OM 2019.04.02 Envoie la page "HTML" au serveur. On passe un message d'information dans "message_html"

            # On affiche les state_stuff
            return redirect(url_for('state_stuff_afficher', order_by='ASC', id_state_stuff_sel=0))



        except (pymysql.err.OperationalError, pymysql.ProgrammingError, pymysql.InternalError, pymysql.IntegrityError,
                TypeError) as erreur:
            # OM 2020.04.09 Traiter spécifiquement l'erreur MySql 1451
            # Cette erreur 1451, signifie qu'on veut effacer un "state_stuff" de user qui est associé dans "t_genders_films".
            if erreur.args[0] == 1451:
                # C'est une erreur à signaler à l'utilisateur de cette application WEB.
                flash('IMPOSSIBLE d\'effacer !!! Cette valeur est associée à des user !')
                # DEBUG bon marché : Pour afficher un message dans la console.
                print(f"IMPOSSIBLE d'effacer !! Ce state_stuff est associé à des user dans la t_stuff !!! : {erreur}")
                # Afficher la liste des state_stuff des user
                return redirect(url_for('state_stuff_afficher', order_by='ASC', id_state_stuff_sel=0))
            else:
                # Communiquer qu'une autre erreur que la 1062 est survenue.
                # DEBUG bon marché : Pour afficher un message dans la console.
                print(f"Erreur genders_delete {erreur.args[0], erreur.args[1]}")
                # C'est une erreur à signaler à l'utilisateur de cette application WEB.
                flash(f"Erreur genders_delete {erreur.args[0], erreur.args[1]}")


            # OM 2019.04.02 Envoie la page "HTML" au serveur.
    return render_template('state_stuff/state_stuff_afficher.html', data=data_state_stuff)