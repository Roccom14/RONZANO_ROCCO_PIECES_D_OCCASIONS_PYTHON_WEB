# RONZANO_ROCCO_PIECES_D_OCCASIONS_PYTHON_WEB
Dossier GIT pour mon prof préféré &#9825;

-------------------------------------------------------------------------------

## Marche à suivre

##### --INSTALLATION--

Pour commencer il faut télécharger la dernière version de chaque logiciel:

- [Python](https://www.python.org/) pour votre OS
- [UwAmp](https://www.uwamp.com/fr/?page=download) (Windows) ou [Mamp](https://www.mamp.info/fr/downloads/) (MacOS) ou [Xampp](https://www.apachefriends.org/download.html) (Linux)
- [PyCharm](https://www.jetbrains.com/fr-fr/pycharm/download/) pour votre OS

##### --CONFIGURATION--

Maintenant que c'est installé il faut configurer !

1. Ouvrir PyCharm et cliquer sur "Get from Version Control".
2. Sur la nouvelle fenêtre qui vient de s'ouvrir, dans "URL:", coller le lien [GIT](https://github.com/Roccom14/RONZANO_ROCCO_PIECES_D_OCCASIONS_PYTHON_WEB.git) et finalement choisir où installer le projet.
3. Ouvrir le projet ```RONZANO_ROCCO_PIECES_D_OCCASIONS_PYTHON_WEB``` dans PyCharm, et configurer l'interpréteur python pour que le projet puisse fonctionner.
4. Pour configurer l'interpréteur, aller sur ```File -> Settings -> Project: RONZANO_ROCCO_PIECES_D_OCCASIONS_PYTHON_WEB -> Projet Interpreter``` cliquer sur le bouton molette et choisir ```Add...```.
5. Sur la nouvelle fenêtre la sélection doit être sur ```New environment``` et cliquer sur ```OK```.
6. Si une fenêtre demande si on veut installer les packages du projet venant de ```requirements.txt```, cliquer sur oui.
7. Sinon, aller dans à ```RONZANO_ROCCO_PIECES_D_OCCASIONS_PYTHON_WEB\requirements.txt``` et installer les packages manquants au bon fonctionnement en passant la souris dessus et une petite ampoule apparaît, selectionner "install package [name_package]"

  *  Si vous êtes sur MacOS, aller à ```RONZANO_ROCCO_PIECES_D_OCCASIONS_PYTHON_WEB\APP_PIECES_D_OCCASIONS\DATABASE\connect_db_context_manager.py``` et décommenter la ligne ```36```

Voilà PyCharm est prêt à fonctionner !

Maintenant il faut configurer phpMyAdmin pour que quelque chose s'affiche dans le projet, sinon c'est le vide...

8. Ouvrir UwAmp ou Mamp ou Xampp et démarrer le serveur mysql si ce n'est pas déjà le cas.

9. Dans un navigateur aller sur <http://localhost/mysql>, et se log avec
  - Username = root
  - Password = root


10. Une fois entré dans phpMyAdmin, cliquer sur la petite maison puis sous "Importer".

11. Cliquer sur ```Choisir un fichier```, une nouvelle fenêtre s'ouvre, aller sur

```..\RONZANO_ROCCO_PIECES_D_OCCASIONS_PYTHON_WEB\APP_PIECES_D_OCCASIONS\DATABASE\ronzano_rocco_pieces_d_occasions_info1c_2020.sql```

ou

```..\RONZANO_ROCCO_PIECES_D_OCCASIONS_PYTHON_WEB\Docs\ronzano_rocco_pieces_d_occasions_info1c_2020.sql```

et finalement cliquer sur "Exécuter".

Trop bien, le fichier sql a été importé !

##### --AFFICHAGE DU PROJET--

1. Dans PyCharm, sous
```RONZANO_ROCCO_PIECES_D_OCCASIONS_PYTHON_WEB\run_mon_app.py```

  Clique-droit sur ```run_mon_app.py```, dans le menu déroulant, Exécuter ```Run 'run_mon_app'```.
2. Dans le run de PyCharm, des ligne de codes défilent, et à la fin une ligne comportant <http://127.0.0.1:1148/>, cliquer sur celle-ci.
3. Un nouvel onglet dans votre navigateur vient de s'ouvrir, c'est le projet !


Hourra ! Le projet s'est affiché !



PS: Si vous avez des soucis sur le bon déroulement de l'installation ou la configuration, voici les vidéos de demo:

- Windows -> [ici](blank)
- MacOS -> [ici](blank)
- Linux -> [ici](blank)

Ou par mail à <webmaster@ronzano.ch>

Liste non exaustive d'erreurs :

| Erreur | Etat erreur | Résolution |
|:-------|:------------|:-----------|
| Flash....BD NON CONNECTÉE. Erreur : Can't connect to MySQL server on '127.0.0.1' ([WinError 10061] Aucune connexion n’a pu être établie car l’ordinateur cible l’a expressément refusée)    | Le serveur phpMyAdmin n'est pas allumé et/ou démarré | Allumer et démarrer le serveur PhpMyAdmin |
| No python intrepreter found| interpréteur Python non ou mal configuré | Il faut aller vérifier la configuration de l'interpréteur python dans PyCharm |
| Page dans le navigateur 127.0.0.1:1148 qui affiche "connection échouée" ou qui charge pas  | Le projet python n'est pas allumé et /ou démarré | il faut exécuter le "run_mon_app.py"  |

L'Occaz' &#169;&#x2122; est une marque déposée de [Ronzano & Cie Fils Sàrl](https://ronzanoandcie.ch) &#169;&#x2122;
