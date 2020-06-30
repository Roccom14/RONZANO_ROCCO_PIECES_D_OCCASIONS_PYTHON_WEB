/*
	Toutes les colonnes
*/
SELECT * FROM t_stuff AS T1
INNER JOIN t_films AS T2 ON T2.id_film = T1.fk_film
INNER JOIN t_genres AS T3 ON T3.id_genre = T1.fk_genre

/*
	Seulement certaines colonnes
*/
SELECT id_genre, intitule_genre , id_film, nom_film FROM t_stuff AS T1
INNER JOIN t_films AS T2 ON T2.id_film = T1.fk_film
INNER JOIN t_genres AS T3 ON T3.id_genre = T1.fk_genre

/* 	
	Permet d'afficher toutes les lignes de la table de droite (t_genres) (qui est écrite en sql à droite de t_stuff)
	y compris les lignes qui ne sont pas attribuées à des user.
*/
SELECT id_genre, intitule_genre , id_film, nom_film FROM t_stuff AS T1
INNER JOIN t_films AS T2 ON T2.id_film = T1.fk_film
RIGHT JOIN t_genres AS T3 ON T3.id_genre = T1.fk_genre

/* 	
	Permet d'afficher toutes les lignes de la table de droite (t_genres) (qui est écrite en sql à droite de t_stuff)
	y compris les lignes qui ne sont pas attribuées à des user.
*/
SELECT id_genre, intitule_genre , id_film, nom_film  FROM t_stuff AS T1
RIGHT JOIN t_films AS T2 ON T2.id_film = T1.fk_film
LEFT JOIN t_genres AS T3 ON T3.id_genre = T1.fk_genre


/*
	Affiche TOUS les user qui n'ont pas de genre attribués
*/
SELECT id_genre, intitule_genre , id_film, nom_film  FROM t_stuff AS T1
RIGHT JOIN t_films AS T2 ON T2.id_film = T1.fk_film
LEFT JOIN t_genres AS T3 ON T3.id_genre = T1.fk_genre


/*
	Affiche SEULEMENT les user qui n'ont pas de genre attribués
*/

SELECT id_genre, intitule_genre , id_film, nom_film  FROM t_stuff AS T1
RIGHT JOIN t_films AS T2 ON T2.id_film = T1.fk_film
LEFT JOIN t_genres AS T3 ON T3.id_genre = T1.fk_genre
WHERE T1.fk_genre IS NULL
