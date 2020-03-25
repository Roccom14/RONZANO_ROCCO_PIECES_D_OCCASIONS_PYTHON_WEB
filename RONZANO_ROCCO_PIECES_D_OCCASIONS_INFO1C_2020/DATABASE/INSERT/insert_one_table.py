# insert_one_table.py
# OM 2020.03.10 le but est d'insérer des valeurs en MySql dans une seule table
import pymysql
from DATABASE import connect_db


class DbInsertOneTable():

    # Constructeur, à chaque instanciation de cette classe "DbInsertOneTable()" les lignes de code de la méthode "__init__ (self)" sont interprétées.
    def __init__ (self):  # Constructeur
        print("Constructeur CLASSE DbInsertOneTable")


    def insert_one_record_one_table(self, requete_insert_mysql, valeurs_a_inserer):
        """
        Méthode qui permet d'insérer UNE seule valeur passée en paramètre.
        OM 2020.03.24
                Parametres:
                        requete_insert_mysql (class 'str'): une classe string
                        valeurs_insertion (class 'dict'): une classe dictionnaire

                Retourne:
                        pas de valeurs

        """
        try:
            # OM 2020.01.28 CONNECTION A LA BD
            self.connection_dbc = connect_db.DatabaseTools()
            self.connection_dbc.is_connection_open()

            # Pour aider à comprendre les types de données on affiche dans la console
            print("type >>> requete_insert_mysql ",type(requete_insert_mysql))
            print("type >>> valeurs_a_inserer ",type(valeurs_a_inserer))
            # OM 2020.03.11 Execute la requête avec un passage de paramètres
            self.connection_dbc.DBcursor.execute(requete_insert_mysql, {'values_insert' : valeurs_a_inserer})

            # OM 2020.03.11 L'instruction suivante est indispensable pour confirmer l'insertion des données (en cas de problèmes : rollback)
            self.connection_dbc.db.commit()
            self.connection_dbc.DBcursor.close()
        except pymysql.Error as error:
            # OM 2020.03.11 L'instruction suivante est indispensable pour annuler l'insertion des données (commande opposée : COMMIT)
            self.connection_dbc.db.rollback()
            print(" Il y a une ERREUR : %s", error)
            print("connection_dbc.db.rollback() insertOneRecord")
        except pymysql.DataError as error1:
            # OM 2020.03.11 L'instruction suivante est indispensable pour annuler l'insertion des données (commande opposée : COMMIT)
            self.connection_dbc.db.rollback()
            print(" Il y a une DataError : %s", error1)
            print("connection_dbc.db.rollback() insertOneRecord")
        except pymysql.DatabaseError as error2:
            # OM 2020.03.11 L'instruction suivante est indispensable pour annuler l'insertion des données (commande opposée : COMMIT)
            self.connection_dbc.db.rollback()
            print(" Il y a une DatabaseError : %s", error2)
            print("connection_dbc.db.rollback() insertOneRecord")
        except pymysql.Warning as error3:
            # OM 2020.03.11 L'instruction suivante est indispensable pour annuler l'insertion des données (commande opposée : COMMIT)
            self.connection_dbc.db.rollback()
            print(" Il y a une Warning : %s", error3)
            print("connection_dbc.db.rollback() insertOneRecord")
        except pymysql.MySQLError as error4:
            # OM 2020.03.11 L'instruction suivante est indispensable pour annuler l'insertion des données (commande opposée : COMMIT)
            self.connection_dbc.db.rollback()
            print(" Il y a une MySQLError : %s", error4)
            print("connection_dbc.db.rollback() insertOneRecord")
        except pymysql.IntegrityError as error5:
            # OM 2020.03.11 L'instruction suivante est indispensable pour annuler l'insertion des données (commande opposée : COMMIT)
            self.connection_dbc.db.rollback()
            print(" Il y a une IntegrityError : %s", error5)
            print("connection_dbc.db.rollback() insertOneRecord")
        except:
            # OM 2020.03.11 L'instruction suivante est indispensable pour annuler l'insertion des données (commande opposée : COMMIT)
            self.connection_dbc.db.rollback()
            print("Unknown error occurred")
        finally:
            print("C'est terminé....finally self.DBcursor.close()")
            self.DBcursor.close()



    def insert_one_record_many_values_one_table(self, requete_insert_mysql, valeurs_insertion):
        """
        Méthode qui permet d'insérer les valeurs passées en paramètres.
        OM 2020.03.24
                Parametres:
                        requete_insert_mysql (class 'str'): une classe string
                        valeurs_insertion (class 'dict'): une classe dictionnaire

                Retourne:
                        pas de valeurs

        """
        try:
            # OM 2020.01.28 CONNECTION A LA BD
            self.connection_dbc = connect_db.DatabaseTools().connect_ma_bd()
            # Ouvre un curseur, c'est indispensable pour se déplacer dans les champs de la BD.
            self.DBcursor = self.connection_dbc.db.cursor()
            print(type(requete_insert_mysql))
            print(type(valeurs_insertion))
            print(self.insert_one_record_many_values_one_table.__doc__)
            # OM 2020.03.11 Execute la requête avec un passage de paramètres
            # self.DBcursor.execute(requete_insert_mysql, {'values_insert' : valeurs_a_inserer, 'values_insert_2' : values_2})
            self.DBcursor.execute(requete_insert_mysql, valeurs_insertion)

            # OM 2020.03.11 L'instruction suivante est indispensable pour confirmer l'insertion des données (en cas de problèmes : rollback)
            self.connection_dbc.db.commit()
            self.DBcursor.close()
        except pymysql.Error as error:
            # OM 2020.03.11 L'instruction suivante est indispensable pour annuler l'insertion des données (commande opposée : COMMIT)
            self.connection_dbc.db.rollback()
            print(" Il y a une ERREUR : %s", error)
            print("connection_dbc.db.rollback() insertOneRecord")
        except pymysql.DataError as error1:
            # OM 2020.03.11 L'instruction suivante est indispensable pour annuler l'insertion des données (commande opposée : COMMIT)
            self.connection_dbc.db.rollback()
            print(" Il y a une DataError : %s", error1)
            print("connection_dbc.db.rollback() insertOneRecord")
        except pymysql.DatabaseError as error2:
            # OM 2020.03.11 L'instruction suivante est indispensable pour annuler l'insertion des données (commande opposée : COMMIT)
            self.connection_dbc.db.rollback()
            print(" Il y a une DatabaseError : %s", error2)
            print("connection_dbc.db.rollback() insertOneRecord")
        except pymysql.Warning as error3:
            # OM 2020.03.11 L'instruction suivante est indispensable pour annuler l'insertion des données (commande opposée : COMMIT)
            self.connection_dbc.db.rollback()
            print(" Il y a une Warning : %s", error3)
            print("connection_dbc.db.rollback() insertOneRecord")
        except pymysql.MySQLError as error4:
            # OM 2020.03.11 L'instruction suivante est indispensable pour annuler l'insertion des données (commande opposée : COMMIT)
            self.connection_dbc.db.rollback()
            print(" Il y a une MySQLError : %s", error4)
            print("connection_dbc.db.rollback() insertOneRecord")
        except pymysql.IntegrityError as error5:
            # OM 2020.03.11 L'instruction suivante est indispensable pour annuler l'insertion des données (commande opposée : COMMIT)
            self.connection_dbc.db.rollback()
            print(" Il y a une IntegrityError : %s", error5)
            print("connection_dbc.db.rollback() insertOneRecord")
        except:
            # OM 2020.03.11 L'instruction suivante est indispensable pour annuler l'insertion des données (commande opposée : COMMIT)
            self.connection_dbc.db.rollback()
            print("Unknown error occurred")
        finally:
            print("C'est terminé....finally self.DBcursor.close()")
            self.DBcursor.close()