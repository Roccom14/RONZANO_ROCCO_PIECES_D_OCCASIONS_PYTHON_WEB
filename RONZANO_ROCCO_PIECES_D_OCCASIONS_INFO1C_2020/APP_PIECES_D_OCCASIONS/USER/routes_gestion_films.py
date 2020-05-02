# routes_gestion_films.py
# OM 2020.04.06 Gestions des "routes" FLASK pour les films.

import pymysql
from flask import render_template, flash, request
from APP_FILMS import obj_mon_application
from APP_FILMS.FILMS.data_gestion_films import GestionFilms
from APP_FILMS.DATABASE.connect_db_context_manager import MaBaseDeDonnee

# OM 2020.04.16 Afficher un avertissement sympa...mais contraignant
# Pour la tester http://127.0.0.1:1234/avertissement_sympa_pour_geeks
@obj_mon_application.route("/avertissement_sympa_pour_geeks")
def avertissement_sympa_pour_geeks():
    # OM 2020.04.07 Envoie la page "HTML" au serveur.
    return render_template("films/AVERTISSEMENT_SYMPA_POUR_LES_GEEKS_films.html")




# OM 2020.04.16 Afficher les films
# Pour la tester http://127.0.0.1:1234/films_afficher
@obj_mon_application.route("/films_afficher")
def films_afficher():
    # OM 2020.04.09 Pour savoir si les données d'un formulaire sont un affichage
    # ou un envoi de donnée par des champs du formulaire HTML.
    if request.method == "GET":
        try:
            # OM 2020.04.09 Objet contenant toutes les méthodes pour gérer (CRUD) les données.
            obj_actions_films = GestionFilms()
            # Récupére les données grâce à une requête MySql définie dans la classe GestionFilms()
            # Fichier data_gestion_films.py
            data_films = obj_actions_films.films_afficher_data()
            # DEBUG bon marché : Pour afficher un message dans la console.
            print(" data films", data_films, "type ", type(data_films))

            # OM 2020.04.09 La ligns ci-après permet de donner un sentiment rassurant aux utilisateurs.
            flash("Données films affichées !!", "Success")
        except Exception as erreur:
            print(f"RGF Erreur générale.")
            # OM 2020.04.09 On dérive "Exception" par le "@obj_mon_application.errorhandler(404)" fichier "run_mon_app.py"
            # Ainsi on peut avoir un message d'erreur personnalisé.
            # flash(f"RGG Exception {erreur}")
            raise Exception(f"RGF Erreur générale. {erreur}")

    # OM 2020.04.07 Envoie la page "HTML" au serveur.
    return render_template("films/films_afficher.html", data=data_films)


# OM 2020.04.06 Pour une simple démo. On insère deux fois des valeurs dans la table films
# Une fois de manière fixe, vous devez changer les valeurs pour voir le résultat dans la table "t_films"
# La 2ème il faut entrer la valeur du titre du film par le clavier, il ne doit pas être vide.
# Pour les autres valeurs elles doivent être changées ci-dessous.
# Une des valeurs est "None" ce qui en MySql donne "NULL" pour l'attribut "t_films.cover_link_film"
# Pour la tester http://127.0.0.1:1234/films_add
@obj_mon_application.route("/films_add")
def films_add():
    # obj_ma_db = MaBaseDeDonnee().__enter__()
    # print("obj_ma_db.open -->  ", obj_ma_db.open)
    # OM 2020.04.06 La connection à la BD doit être ouverte
    #if obj_ma_db.open:
    try:
        obj_actions_films = GestionFilms()
        valeurs_fixes_insertion_dictionnaire = {"value_nom_film": "Film 100000",
                                                "value_duree_film": "567",
                                                "value_description_film": "C'est un film qui montre ooh oui... les'",
                                                "value_cover_link_film": "http://sdfsfsf.sdfdsf.tk",
                                                'value_date_sortie_film': "1945-04-06"}
        obj_actions_films.add_film(valeurs_fixes_insertion_dictionnaire)
        # OM 2020.04.06 Entrée d'un titre de film au clavier pour les essais c'est mieux qu'une valeur aléatoire
        # Si l'utilisateur "claviote" seulement "ENTREE", alors on redemande de "clavioter" une chaîne de caractères
        #
        nom_film_keyboard = None
        while not nom_film_keyboard:
            nom_film_keyboard = input("Titre du film ?")

        # Pour des essais il y a une valeur avec la valeur "None"... lorsqu'elle va être insèrée en MySql
        # ce sera la valeur NULL
        valeurs_fixes_insertion_dictionnaire = {"value_nom_film": nom_film_keyboard,
                                                "value_duree_film": "567",
                                                "value_description_film": "C'est un film qui montre... les'",
                                                "value_cover_link_film": None,
                                                'value_date_sortie_film': "1945-04-06"}
        obj_actions_films.add_film(valeurs_fixes_insertion_dictionnaire)
        flash("Ajout de 2 films, OK !", "Sucess")
        return render_template("home.html")
    except (Exception, pymysql.err.Error) as erreur:
        flash(f"FLASH ! Gros problème dans l'insertion de 2 films  ! {erreur}", "Danger")
        return render_template("home.html")
