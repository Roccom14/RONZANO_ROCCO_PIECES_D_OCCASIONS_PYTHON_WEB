# routes_gestion_stuff.py
# OM 2020.04.06 Gestions des "routes" FLASK pour les stuff.
import re
import pymysql
from flask import render_template, flash, request, redirect, url_for
from APP_PIECES_D_OCCASIONS import obj_mon_application
from APP_PIECES_D_OCCASIONS.DATABASE.erreurs import msg_erreurs, MaBdErreurDoublon, MonErreur, MaBdErreurConnexion
from APP_PIECES_D_OCCASIONS.GENDERS.data_gestion_genders import GestionGenders
from APP_PIECES_D_OCCASIONS.STATE_STUFF.data_gestion_state_stuff import GestionStateStuff
from APP_PIECES_D_OCCASIONS.TYPE_PAYMENT.data_gestion_type_payment import GestionTypePayment
from APP_PIECES_D_OCCASIONS.USER.data_gestion_user import GestionUser
from APP_PIECES_D_OCCASIONS.STUFF.data_gestion_stuff import GestionStuff
from APP_PIECES_D_OCCASIONS.DATABASE.connect_db_context_manager import MaBaseDeDonnee


# OM 2020.04.16 Afficher un avertissement sympa...mais contraignant
# Pour la tester http://127.0.0.1:1234/avertissement_sympa_pour_geeks
# @obj_mon_application.route("/avertissement_sympa_pour_geeks")
def avertissement_sympa_pour_geeks():
    # OM 2020.04.07 Envoie la page "HTML" au serveur.
    return render_template("user/AVERTISSEMENT_SYMPA_POUR_LES_GEEKS_user.html")


# OM 2020.04.16 Afficher les user
# Pour la tester http://127.0.0.1:1234/user_afficher
@obj_mon_application.route("/stuff_afficher")
def stuff_afficher():
    # OM 2020.04.09 Pour savoir si les données d'un formulaire sont un affichage
    # ou un envoi de donnée par des champs du formulaire HTML.
    if request.method == "GET":
        try:
            # OM 2020.04.09 Objet contenant toutes les méthodes pour gérer (CRUD) les données.
            obj_actions_stuff = GestionStuff()
            # Récupére les données grâce à une requête MySql définie dans la classe GestionUser()
            # Fichier data_gestion_user.py
            data_stuff = obj_actions_stuff.stuff_afficher_data()
            # DEBUG bon marché : Pour afficher un message dans la console.
            print(" data stuff", data_stuff, "type ", type(data_stuff))

            # OM 2020.04.09 La ligns ci-après permet de donner un sentiment rassurant aux utilisateurs.
            flash("Données stuff affichées !!", "Success")
        except Exception as erreur:
            print(f"RGF Erreur générale.")
            # OM 2020.04.09 On dérive "Exception" par le "@obj_mon_application.errorhandler(404)" fichier "run_mon_app.py"
            # Ainsi on peut avoir un message d'erreur personnalisé.
            # flash(f"RGG Exception {erreur}")
            raise Exception(f"RGF Erreur générale. {erreur}")

    # OM 2020.04.07 Envoie la page "HTML" au serveur.
    return render_template("stuff/stuff_afficher.html", data=data_stuff)


# ---------------------------------------------------------------------------------------------------
# OM 2020.04.07 Définition d'une "route" /user_add ,
# cela va permettre de programmer quelles actions sont réalisées avant de l'envoyer
# au navigateur par la méthode "render_template"
# En cas d'erreur on affiche à nouveau la page "user_add.html"
# Pour la tester http://127.0.0.1:1234/user_add
# ---------------------------------------------------------------------------------------------------
@obj_mon_application.route("/stuff_add", methods=['GET', 'POST'])
def stuff_add():
    # OM 2019.03.25 Pour savoir si les données d'un formulaire sont un affichage
    # ou un envoi de donnée par des champs utilisateurs.
    obj_actions_user = GestionUser()
    obj_actions_state_stuff = GestionStateStuff()
    obj_actions_type_payment = GestionTypePayment()
    data_user = obj_actions_user.user_afficher_data()
    data_state_stuff = obj_actions_state_stuff.state_stuff_afficher_data(valeur_order_by='ASC', id_state_stuff_sel=0)
    data_type_payment = obj_actions_type_payment.type_payment_afficher_data(valeur_order_by='ASC', id_type_payment_sel=0)
    if request.method == "POST":
        try:
            # OM 2020.04.09 Objet contenant toutes les méthodes pour gérer (CRUD) les données.
            obj_actions_stuff = GestionStuff()
            # OM 2020.04.09 Récupère le contenu du champ dans le formulaire HTML "user_add.html"
            name_stuff = request.form['name_stuff_html']
            description_stuff = request.form['description_stuff_html']
            price_stuff = request.form['price_stuff_html']
            type_stuff = request.form['type_stuff_html']
            quantity_stuff = request.form['quantity_stuff_html']
            user = request.form['user_select']
            state_stuff = request.form['state_stuff_select']
            type_payment = request.form['type_payment_select']
            date_add_stuff = request.form['date_add_stuff_html']
            date_bought_stuff = request.form['date_bought_stuff_html']

            # OM 2019.04.04 On ne doit pas accepter des valeurs vides, des valeurs avec des chiffres,
            # des valeurs avec des caractères qui ne sont pas des lettres.
            # Accepte le trait d'union ou l'apostrophe, et l'espace entre deux mots, mais pas plus d'une occurence.
            if not re.match("^([A-Z]|[a-z\u00C0-\u00FF])[A-Za-z\u00C0-\u00FF]*['\\- ]?[A-Za-z\u00C0-\u00FF]+$",
                            type_stuff):
                # OM 2019.03.28 Message humiliant à l'attention de l'utilisateur.
                flash(f"Une entrée...incorrecte !! Pas de chiffres, de caractères spéciaux, d'espace à double, "
                      f"de double apostrophe, de double trait union et ne doit pas être vide.", "Danger")
                # On doit afficher à nouveau le formulaire "user_add.html" à cause des erreurs de "claviotage"
                return redirect(url_for("stuff_add"))
            else:

                # Constitution d'un dictionnaire et insertion dans la BD
                valeurs_insertion_dictionnaire = {"value_name_stuff": name_stuff,
                                                  "value_description_stuff": description_stuff,
                                                  "value_price_stuff": price_stuff,
                                                  "value_type_stuff": type_stuff,
                                                  "value_quantity_stuff": quantity_stuff,
                                                  "value_user": user,
                                                  "value_state_stuff": state_stuff,
                                                  "value_type_payment": type_payment,
                                                  "value_date_add_stuff": date_add_stuff,
                                                  "value_date_bought_stuff": date_bought_stuff}

                obj_actions_stuff.add_stuff_data(valeurs_insertion_dictionnaire)

                # OM 2019.03.25 Les 2 lignes ci-après permettent de donner un sentiment rassurant aux utilisateurs.
                flash(f"Données insérées !!", "Sucess")
                print(f"Données insérées !!")
                # On va interpréter la "route" 'user_afficher', car l'utilisateur
                # doit voir le nouveau firstname_user qu'il vient d'insérer.
                return redirect(url_for('stuff_afficher'))

        # OM 2020.04.16 ATTENTION à l'ordre des excepts très important de respecter l'ordre.
        # except pymysql.err.IntegrityError as erreur:
            # OM 2020.04.09 On dérive "pymysql.err.IntegrityError" dans "MaBdErreurDoublon" fichier "erreurs.py"
            # Ainsi on peut avoir un message d'erreur personnalisé.
            #raise MaBdErreurDoublon(
                # f"RGG pei {msg_erreurs['ErreurDoublonValue']['message']} et son status {msg_erreurs['ErreurDoublonValue']['status']}")

        # OM 2020.04.16 ATTENTION à l'ordre des excepts très important de respecter l'ordre.
        #except (pymysql.err.OperationalError,
            #     pymysql.ProgrammingError,
            #     pymysql.InternalError,
            #     TypeError) as erreur:
            # flash(f"Autre erreur {erreur}")
            #raise MonErreur(f"Autre erreur")

        # OM 2020.04.16 ATTENTION à l'ordre des excepts très important de respecter l'ordre.
        except Exception as erreur:
            # OM 2020.04.09 On dérive "Exception" dans "MaBdErreurConnexion" fichier "erreurs.py"
            # Ainsi on peut avoir un message d'erreur personnalisé.
            raise MaBdErreurConnexion(
                f"RGG Exception {msg_erreurs['ErreurConnexionBD']['message']} et son status {msg_erreurs['ErreurConnexionBD']['status']}")
    # OM 2020.04.07 Envoie la page "HTML" au serveur.
    return render_template("stuff/stuff_add.html",
                           data_user=data_user,
                           data_state_stuff=data_state_stuff,
                           data_type_payment=data_type_payment)


# ---------------------------------------------------------------------------------------------------
# OM 2020.04.07 Définition d'une "route" /user_edit , cela va permettre de programmer quelles actions sont réalisées avant de l'envoyer
# au navigateur par la méthode "render_template".
# On change la valeur d'un firstname_user de user par la commande MySql "UPDATE"
# ---------------------------------------------------------------------------------------------------
@obj_mon_application.route('/stuff_edit', methods=['POST', 'GET'])
def stuff_edit():
    # OM 2020.04.07 Les données sont affichées dans un formulaire, l'affichage de la sélection
    # d'une seule ligne choisie par le bouton "edit" dans le formulaire "user_afficher.html"

    obj_actions_user = GestionUser()
    obj_actions_state_stuff = GestionStateStuff()
    obj_actions_type_payment = GestionTypePayment()
    data_user = obj_actions_user.user_afficher_data()
    data_state_stuff = obj_actions_state_stuff.state_stuff_afficher_data(valeur_order_by='ASC', id_state_stuff_sel=0)
    data_type_payment = obj_actions_type_payment.type_payment_afficher_data(valeur_order_by='ASC', id_type_payment_sel=0)

    if request.method == 'GET':
        try:
            # Récupérer la valeur de "id_user" du formulaire html "user_afficher.html"
            # l'utilisateur clique sur le lien "edit" et on récupére la valeur de "id_user"
            # grâce à la variable "id_user_edit_html"
            # <a href="{{ url_for('user_edit', id_user_edit_html=row.id_user) }}">Edit</a>
            id_stuff_edit = request.values['id_stuff_edit_html']

            # Pour afficher dans la console la valeur de "id_user_edit", une façon simple de se rassurer,
            # sans utiliser le DEBUGGER
            print(id_stuff_edit)

            # Constitution d'un dictionnaire et insertion dans la BD
            valeur_select_dictionnaire = {"value_id_stuff": id_stuff_edit}

            # OM 2020.04.09 Objet contenant toutes les méthodes pour gérer (CRUD) les données.
            obj_actions_stuff = GestionStuff()

            # OM 2019.04.02 La commande MySql est envoyée à la BD
            data_id_stuff = obj_actions_stuff.edit_stuff_data(valeur_select_dictionnaire)
            print("dataIdStuff ", data_id_stuff, "type ", type(data_id_stuff))
            # Message ci-après permettent de donner un sentiment rassurant aux utilisateurs.
            flash(f"Editer le stuff !!!")

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

    return render_template("stuff/stuff_edit.html",
                           data_user=data_user,
                           data_state_stuff=data_state_stuff,
                           data_type_payment=data_type_payment,
                           data=data_id_stuff)


# ---------------------------------------------------------------------------------------------------
# OM 2020.04.07 Définition d'une "route" /user_update , cela va permettre de programmer quelles actions sont réalisées avant de l'envoyer
# au navigateur par la méthode "render_template".
# On change la valeur d'un firstname_user de user par la commande MySql "UPDATE"
# ---------------------------------------------------------------------------------------------------
@obj_mon_application.route('/stuff_update', methods=['POST', 'GET'])
def stuff_update():
    # DEBUG bon marché : Pour afficher les méthodes et autres de la classe "flask.request"
    print(dir(request))
    # OM 2020.04.07 Les données sont affichées dans un formulaire, l'affichage de la sélection
    # d'une seule ligne choisie par le bouton "edit" dans le formulaire "user_afficher.html"
    # Une fois que l'utilisateur à modifié la valeur du firstname_user alors il va appuyer sur le bouton "UPDATE"
    # donc en "POST"
    obj_actions_user = GestionUser()
    obj_actions_state_stuff = GestionStateStuff()
    obj_actions_type_payment = GestionTypePayment()
    data_user = obj_actions_user.user_afficher_data()
    data_state_stuff = obj_actions_state_stuff.state_stuff_afficher_data(valeur_order_by='ASC', id_state_stuff_sel=0)
    data_type_payment = obj_actions_type_payment.type_payment_afficher_data(valeur_order_by='ASC', id_type_payment_sel=0)

    if request.method == 'POST':
        try:
            # DEBUG bon marché : Pour afficher les valeurs contenues dans le formulaire
            print("request.values ", request.values)

            # Récupérer la valeur de "id_user" du formulaire html "user_edit.html"
            # l'utilisateur clique sur le lien "edit" et on récupére la valeur de "id_user"
            # grâce à la variable "id_user_edit_html"
            # <a href="{{ url_for('user_edit', id_user_edit_html=row.id_user) }}">Edit</a>
            id_stuff_edit = request.values['id_stuff_edit_html']

            # Récupère le contenu du champ "firstname_user" dans le formulaire HTML "UserEdit.html"
            name_stuff = request.form['edit_name_stuff_html']
            description_stuff = request.form['edit_description_stuff_html']
            price_stuff = request.form['edit_price_stuff_html']
            type_stuff = request.form['edit_type_stuff_html']
            quantity_stuff = request.form['edit_quantity_stuff_html']
            user = request.form['edit_user_select']
            state_stuff = request.form['edit_state_stuff_select']
            type_payment = request.form['edit_type_payment_select']
            date_add_stuff = request.form['edit_date_add_stuff_html']
            date_bought_stuff = request.form['edit_date_bought_stuff_html']
            valeur_edit_list = [{'id_stuff': id_stuff_edit, 'name_stuff': name_stuff,
                                 'description_stuff': description_stuff, 'price_stuff': price_stuff,
                                 'type_stuff': type_stuff, 'quantity_stuff': quantity_stuff, 'fk_user': user,
                                 'fk_state_stuff': state_stuff, 'fk_type_payment': type_payment,
                                 'date_add_stuff': date_add_stuff, 'date_bought_stuff': date_bought_stuff}]

            # On ne doit pas accepter des valeurs vides, des valeurs avec des chiffres,
            # des valeurs avec des caractères qui ne sont pas des lettres.
            # Accepte le trait d'union ou l'apostrophe, et l'espace entre deux mots, mais pas plus d'une occurence.
            if not re.match("^([A-Z]|[a-z\u00C0-\u00FF])[A-Za-z\u00C0-\u00FF]*['\\- ]?[A-Za-z\u00C0-\u00FF]+$",
                            type_stuff):
                # En cas d'erreur, conserve la saisie fausse, afin que l'utilisateur constate sa misérable faute
                # Récupère le contenu du champ "firstname_user" dans le formulaire HTML "UserEdit.html"
                # firstname_user = request.values['name_edit_user_html']
                # Message humiliant à l'attention de l'utilisateur.
                flash(f"Une entrée...incorrecte !! Pas de chiffres, de caractères spéciaux, d'espace à double, "
                      f"de double apostrophe, de double trait union et ne doit pas être vide.", "Danger")

                # On doit afficher à nouveau le formulaire "user_edit.html" à cause des erreurs de "claviotage"
                # Constitution d'une liste pour que le formulaire d'édition "user_edit.html" affiche à nouveau
                # la possibilité de modifier l'entrée
                # Exemple d'une liste : [{'id_user': 13, 'firstname_user': 'philosophique'}]
                valeur_edit_list = [{'id_stuff': id_stuff_edit, 'name_stuff': name_stuff,
                                     'description_stuff': description_stuff, 'price_stuff': price_stuff,
                                     'type_stuff': type_stuff, 'quantity_stuff': quantity_stuff, 'fk_user': user,
                                     'fk_state_stuff': state_stuff, 'fk_type_payment': type_payment,
                                     'date_add_stuff': date_add_stuff, 'date_bought_stuff': date_bought_stuff}]
                # DEBUG bon marché :
                # Pour afficher le contenu et le type de valeurs passées au formulaire "user_edit.html"
                print(valeur_edit_list, "type ..", type(valeur_edit_list))
                return render_template('stuff/stuff_edit.html', data=valeur_edit_list)
            else:
                # Constitution d'un dictionnaire et insertion dans la BD
                valeur_update_dictionnaire = {"value_id_stuff": id_stuff_edit,
                                               "value_name_stuff": name_stuff,
                                               "value_description_stuff": description_stuff,
                                               "value_price_stuff": price_stuff,
                                               "value_type_stuff": type_stuff,
                                               "value_quantity_stuff": quantity_stuff,
                                               "value_user": user,
                                               "value_state_stuff": state_stuff,
                                               "value_type_payment": type_payment,
                                               "value_date_add_stuff": date_add_stuff,
                                               "value_date_bought_stuff": date_bought_stuff}

                # OM 2020.04.09 Objet contenant toutes les méthodes pour gérer (CRUD) les données.
                obj_actions_stuff = GestionStuff()

                # La commande MySql est envoyée à la BD
                data_id_stuff = obj_actions_stuff.update_stuff_data(valeur_update_dictionnaire)
                # DEBUG bon marché :
                print("dataIdStuff ", data_id_stuff, "type ", type(data_id_stuff))
                # Message ci-après permettent de donner un sentiment rassurant aux utilisateurs.
                flash(f"Editer le stuff !!!")
                # On affiche les user
                return redirect(url_for('stuff_afficher'))

        except (Exception,
                pymysql.err.OperationalError,
                pymysql.ProgrammingError,
                pymysql.InternalError,
                pymysql.IntegrityError,
                TypeError) as erreur:

            print(erreur.args)
            flash(f"problème stuff update{erreur.args[0]}")
            # En cas de problème, mais surtout en cas de non respect
            # des régles "REGEX" dans le champ "name_edit_user_html" alors on renvoie le formulaire "EDIT"
            return render_template('stuff/stuff_edit.html', data=valeur_edit_list)

    return render_template("stuff/stuff_update.html",
                           data_user=data_user,
                           data_state_stuff=data_state_stuff,
                           data_type_payment=data_type_payment)


# ---------------------------------------------------------------------------------------------------
# OM 2020.04.07 Définition d'une "route" /user_select_delete , cela va permettre de programmer quelles actions sont réalisées avant de l'envoyer
# au navigateur par la méthode "render_template".
# On change la valeur d'un firstname_user de user par la commande MySql "UPDATE"
# ---------------------------------------------------------------------------------------------------
@obj_mon_application.route('/stuff_select_delete', methods=['POST', 'GET'])
def stuff_select_delete():
    if request.method == 'GET':
        try:

            # OM 2020.04.09 Objet contenant toutes les méthodes pour gérer (CRUD) les données.
            obj_actions_stuff = GestionStuff()
            # OM 2019.04.04 Récupérer la valeur de "idUserDeleteHTML" du formulaire html "UserDelete.html"
            id_stuff_delete = request.args.get('id_stuff_delete_html')

            # Constitution d'un dictionnaire et insertion dans la BD
            valeur_delete_dictionnaire = {"value_id_stuff": id_stuff_delete}

            # OM 2019.04.02 La commande MySql est envoyée à la BD
            data_id_stuff = obj_actions_stuff.delete_select_stuff_data(valeur_delete_dictionnaire)
            flash(f"EFFACER et c'est terminé pour cette \"POV\" valeur !!!")

        except (Exception,
                pymysql.err.OperationalError,
                pymysql.ProgrammingError,
                pymysql.InternalError,
                pymysql.IntegrityError,
                TypeError) as erreur:
            # Communiquer qu'une erreur est survenue.
            # DEBUG bon marché : Pour afficher un message dans la console.
            print(f"Erreur user_delete {erreur.args[0], erreur.args[1]}")
            # C'est une erreur à signaler à l'utilisateur de cette application WEB.
            flash(f"Erreur user_delete {erreur.args[0], erreur.args[1]}")

    # Envoie la page "HTML" au serveur.
    return render_template('stuff/stuff_delete.html', data=data_id_stuff)


# ---------------------------------------------------------------------------------------------------
# OM 2019.04.02 Définition d'une "route" /userUpdate , cela va permettre de programmer quelles actions sont réalisées avant de l'envoyer
# au navigateur par la méthode "render_template".
# Permettre à l'utilisateur de modifier un firstname_user, et de filtrer son entrée grâce à des expressions régulières REGEXP
# ---------------------------------------------------------------------------------------------------
@obj_mon_application.route('/stuff_delete', methods=['POST', 'GET'])
def stuff_delete():
    # OM 2019.04.02 Pour savoir si les données d'un formulaire sont un affichage ou un envoi de donnée par des champs utilisateurs.
    if request.method == 'POST':
        try:
            # OM 2020.04.09 Objet contenant toutes les méthodes pour gérer (CRUD) les données.
            obj_actions_stuff = GestionStuff()
            # OM 2019.04.02 Récupérer la valeur de "id_user" du formulaire html "UserAfficher.html"
            id_stuff_delete = request.form['id_stuff_delete_html']
            # Constitution d'un dictionnaire et insertion dans la BD
            valeur_delete_dictionnaire = {"value_id_stuff": id_stuff_delete}

            data_stuff = obj_actions_stuff.delete_stuff_data(valeur_delete_dictionnaire)
            # OM 2019.04.02 On va afficher la liste des user des user
            # OM 2019.04.02 Envoie la page "HTML" au serveur. On passe un message d'information dans "message_html"

            # On affiche les user
            return redirect(url_for('stuff_afficher'))



        except (pymysql.err.OperationalError, pymysql.ProgrammingError, pymysql.InternalError, pymysql.IntegrityError,
                TypeError) as erreur:
            # OM 2020.04.09 Traiter spécifiquement l'erreur MySql 1451
            # Cette erreur 1451, signifie qu'on veut effacer un "firstname_user" de user qui est associé dans "t_user_films".
            if erreur.args[0] == 1451:
                # C'est une erreur à signaler à l'utilisateur de cette application WEB.
                flash('IMPOSSIBLE d\'effacer !!! Cette valeur est associée à des user !')
                # DEBUG bon marché : Pour afficher un message dans la console.
                print(
                    f"IMPOSSIBLE d'effacer !! Ce firstname_user est associé à des user dans la t_user_films !!! : {erreur}")
                # Afficher la liste des user des user
                return redirect(url_for('stuff_afficher'))
            else:
                # Communiquer qu'une autre erreur que la 1062 est survenue.
                # DEBUG bon marché : Pour afficher un message dans la console.
                print(f"Erreur stuff_delete {erreur.args[0], erreur.args[1]}")
                # C'est une erreur à signaler à l'utilisateur de cette application WEB.
                flash(f"Erreur stuff_delete {erreur.args[0], erreur.args[1]}")

            # OM 2019.04.02 Envoie la page "HTML" au serveur.
    return render_template('stuff/stuff_afficher.html', data=data_stuff)
