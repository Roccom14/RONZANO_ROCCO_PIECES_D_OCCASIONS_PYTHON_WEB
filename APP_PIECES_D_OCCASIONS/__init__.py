# Un objet "obj_mon_application" pour utiliser la classe Flask
# Pour les personnes qui veulent savoir ce que signifie __name__ une démonstration se trouve ici :
# https://www.studytonight.com/python/_name_-as-main-method-in-python
# __name__ garantit que la méthode run() est appelée uniquement lorsque main.py est exécuté en tant que programme principal.
# La méthode run() ne sera pas appelée si vous importez main.py dans un autre module Python.
from flask import Flask
from APP_PIECES_D_OCCASIONS.DATABASE import connect_db_context_manager


# Objet qui fait "exister" notre application
obj_mon_application = Flask(__name__, template_folder="templates")
# Flask va pouvoir crypter les cookies
obj_mon_application.secret_key = '_vogonAmiral_)?^'

# Doit se trouver ici... soit après l'instanciation de la classe "Flask"
# OM 2020.03.25 Tout commence ici par "indiquer" les routes de l'application.
from APP_PIECES_D_OCCASIONS import routes
from APP_PIECES_D_OCCASIONS.USER import routes_gestion_user
from APP_PIECES_D_OCCASIONS.GENDERS import routes_gestion_genders
from APP_PIECES_D_OCCASIONS.STUFF import routes_gestion_stuff
from APP_PIECES_D_OCCASIONS.STATE_STUFF import routes_gestion_state_stuff
from APP_PIECES_D_OCCASIONS.TYPE_PAYMENT import routes_gestion_type_payment
