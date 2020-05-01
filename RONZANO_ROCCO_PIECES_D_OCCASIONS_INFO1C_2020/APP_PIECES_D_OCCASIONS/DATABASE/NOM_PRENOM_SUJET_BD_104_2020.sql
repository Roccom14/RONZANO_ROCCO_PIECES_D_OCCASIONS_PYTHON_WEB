-- OM 2020.02.12 
-- FICHIER MYSQL POUR FAIRE FONCTIONNER LES EXEMPLES
-- DE REQUETES MYSQL
-- Database: NOM_PRENOM_SUJET_BD_104_2020

-- Détection si une autre base de donnée du même nom existe

DROP DATABASE IF EXISTS NOM_PRENOM_SUJET_BD_104_2020;

-- Création d'un nouvelle base de donnée

CREATE DATABASE IF NOT EXISTS NOM_PRENOM_SUJET_BD_104_2020;

-- Utilisation de cette base de donnée

USE NOM_PRENOM_SUJET_BD_104_2020;
-- --------------------------------------------------------

--
-- Structure de la table `t_films`
--

CREATE TABLE `t_films` (
  `id_film` int(11) NOT NULL,
  `nom_film` varchar(255) DEFAULT NULL,
  `duree_film` int(11) DEFAULT NULL,
  `description_film` text COMMENT 'Résume du film',
  `cover_link_film` text COMMENT 'lien photo couverture du film',
  `date_sortie_film` date DEFAULT NULL COMMENT 'date sortie du film'
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Contenu de la table `t_films`
--

INSERT INTO `t_films` (`id_film`, `nom_film`, `duree_film`, `description_film`, `cover_link_film`, `date_sortie_film`) VALUES
(3, 'Django', 132, 'Dans le sud des États-Unis, deux ans avant la guerre de Sécession, le Dr King Schultz, un chasseur de primes allemand, fait l’acquisition de Django, un esclave qui peut l’aider à traquer les frères Brittle, les meurtriers qu’il recherche. Schultz promet à Django de lui rendre sa liberté lorsqu’il aura capturé les Brittle – morts ou vifs.', 'data:image/jpeg;base64,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', '2012-05-09'),
(4, 'The Revenant', 156, 'Le film est partiellement adapté du roman Le Revenant de Michael Punke2 et est fondé sur une histoire vraie, celle de l\'exploit accompli en 1823 par le trappeur Hugh Glass.', 'http://fr.web.img3.acsta.net/pictures/15/11/10/09/30/165611.jpg', '2015-12-16'),
(5, 'Lion', 120, 'Saroo, un enfant indien de cinq ans très pauvre qui habite avec sa mère, son grand frère et sa petite sœur dans le quartier de Ganesh Talai à Khandwa dans l\'État du Madhya Pradesh, va aider son grand frère Guddu à la gare de Khandwa. De là, ils prennent un train pour une autre ville.', '\\static\\images\\AFFICHES_FILMS\\Lion_01_BlueVelvetWorld.jpg', '2017-09-10'),
(11, 'Police Story', 146, 'Une opération de la police de Hong Kong durant une transaction illégale de drogue amène plusieurs membres d\'un groupe criminel sous les verrous.\r\n\r\nIncertain de pouvoir faire condamner le chef Chu Tu, le commissaire Li décide de lever les accusations sur Selina Fong, une femme récemment arrivé dans l\'organisation, et de la considérer comme une témoin de l\'affaire. Cette tactique vise à pousser le Chu Tu à commettre une erreur, en le laissant croire que Selina va coopérer. Elle est alors libéré, et l\'inspecteur Chan Ka Kui se voit confier sa protection.', 'https://images-na.ssl-images-amazon.com/images/I/71j2lJAhamL._SL1500_.jpg', '1985-12-14'),
(12, 'Ip Man', 149, 'Film biographique sur la vie de Ip Man, un maître de Kung-Fu spécialisé dans le style Wing Chun et qui fut le mâitre de Bruce Lee. Dans les années 30, Ip Man vit à Foshan dans le sud de la Chine, lors de l\'occupation japonaise. Face à ses indéniables talents en matière d\'arts martiaux, les japonais lui demandent d\'entraîner les soldats, ce qu\'il refuse catégoriquement. Il va alors devoir lutter pour sa survie.', 'https://www.nautiljon.com/images/asian-movie/00/15/ip_man_2_1251.jpg', '2010-08-05'),
(13, 'Kiss of the Dragon', 140, 'Liu Jiang (Jet Li) est un agent des services secrets chinois, envoyé en mission à Paris pour aider la police française, et plus particulièrement l\'inspecteur J.P. Richard (Tchéky Karyo), à arrêter un grand caïd de la drogue. Cependant, alors que deux prostituées rencontrent le suspect, l\'une d\'elle sous l\'emprise de la drogue ', 'http://static.tvtropes.org/pmwiki/pub/images/139f00258917517753bdfb8459319a69.jpg', '2001-06-02'),
(14, 'the transporter', 132, 'Frank Martin, ancien soldat des forces spéciales de reconnaissance, prête ses services de conducteur expert à quiconque le paie. Ses règles personnelles principales consistent à ne pas s\'impliquer personnellement dans les affaires auxquelles il participe, de façon purement instrumentale.', 'https://medias.unifrance.org/medias/40/8/2088/format_affiche/le-transporteur.jpg', '2002-09-02'),
(15, 'The Raid ', 200, 'Au cœur des quartiers pauvres de Jakarta, se trouve une citadelle imprenable dans laquelle se cache le plus dangereux trafiquant du pays. Une équipe de policiers d’élite est envoyée donner l’assaut lors d’un raid secret mené aux premières lueurs du jour.', 'https://images-na.ssl-images-amazon.com/images/I/917rCB5kk8L._SY445_.jpg', '2012-03-22'),
(16, 'ong bak', 148, 'Nong Pradu, un village paisible niché dans une vallée boisée de Thaïlande, est en deuil après le vol de son Bouddha sacré : Ong-Bak. Ting, entraîné secrètement au Muay Thai, art ancien de boxe thaï, se désigne pour aller le récupérer dans la fournaise de Bangkok.', 'https://static.fnac-static.com/multimedia/FR/Images_Produits/FR/fnac.com/Visual_Principal_340/8/2/9/3283451106928/tsp20120928130643/Ong-bak.jpg', '2003-09-23'),
(17, 'Warrior', 220, 'Ancien Marine brisé, Tommy Conlon rentre au pays et demande à son père de le préparer pour un tournoi d’arts martiaux mixtes qui lui permettrait de gagner une fortune. Personne ne sait ce qu’il espère faire de cet argent.', 'http://www.gstatic.com/tv/thumb/movieposters/8063104/p8063104_p_v8_ah.jpg', '2011-09-11'),
(18, 'rolow', 34, 'Les Wilson comptaient passer quelques jours dans leur maison sur la plage, mais voilà que des invités indésirables se présentent. Ils constatent rapidement que ces étrangers leur ressemblent et qu’ils sont eux-mêmes leurs pires ennemis.', NULL, '2018-04-10'),
(19, 'Andréa au travail', NULL, 'film intellectuel', NULL, NULL);

-- --------------------------------------------------------

--
-- Structure de la table `t_genres`
--

CREATE TABLE `t_genres` (
  `id_genre` int(11) NOT NULL,
  `intitule_genre` varchar(50) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Contenu de la table `t_genres`
--

INSERT INTO `t_genres` (`id_genre`, `intitule_genre`) VALUES
(1, 'action'),
(15, 'anime'),
(4, 'aventure'),
(16, 'cartoon'),
(3, 'comedie'),
(10, 'crime'),
(2, 'drame'),
(5, 'fantasie'),
(9, 'historique'),
(8, 'horreur'),
(17, 'musical'),
(12, 'mystere'),
(13, 'philosophique'),
(11, 'realisme'),
(7, 'romantique'),
(6, 'science fiction'),
(14, 'western');

-- --------------------------------------------------------

--
-- Structure de la table `t_genres_films`
--

CREATE TABLE `t_genres_films` (
  `id_genre_film` int(11) NOT NULL,
  `fk_genre` int(11) DEFAULT NULL,
  `fk_film` int(11) DEFAULT NULL,
  `date_insert_genre` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Contenu de la table `t_genres_films`
--

INSERT INTO `t_genres_films` (`id_genre_film`, `fk_genre`, `fk_film`, `date_insert_genre`) VALUES
(141, 14, 3, '2020-02-12 21:30:33'),
(142, 1, 4, '2020-02-12 21:31:31'),
(143, 4, 4, '2020-02-12 21:31:31'),
(144, 4, 5, '2020-02-12 21:35:59'),
(145, 1, 14, '2020-02-12 21:36:57'),
(146, 16, 3, '2020-02-12 21:38:01'),
(147, 1, 12, '2020-02-12 21:39:32'),
(148, 1, 17, '2020-02-12 21:40:44'),
(149, 4, 17, '2020-02-12 21:41:00'),
(150, 2, 17, '2020-02-12 21:44:15'),
(151, 12, 15, '2020-02-12 21:46:21'),
(152, 1, 15, '2020-02-12 21:46:21'),
(153, 1, 13, '2020-02-12 21:54:31'),
(154, 4, 13, '2020-02-12 21:54:31'),
(155, 9, 12, '2020-02-12 21:55:36'),
(156, 13, 19, '2020-02-12 21:57:03'),
(157, 6, 19, '2020-02-12 21:58:03');

--
-- Index pour les tables exportées
--

--
-- Index pour la table `t_films`
--
ALTER TABLE `t_films`
  ADD PRIMARY KEY (`id_film`);

--
-- Index pour la table `t_genres`
--
ALTER TABLE `t_genres`
  ADD PRIMARY KEY (`id_genre`),
  ADD UNIQUE KEY `intitule_genre` (`intitule_genre`);

--
-- Index pour la table `t_genres_films`
--
ALTER TABLE `t_genres_films`
  ADD PRIMARY KEY (`id_genre_film`),
  ADD KEY `fk_genre` (`fk_genre`),
  ADD KEY `fk_film` (`fk_film`);

--
-- AUTO_INCREMENT pour les tables exportées
--

--
-- AUTO_INCREMENT pour la table `t_films`
--
ALTER TABLE `t_films`
  MODIFY `id_film` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=20;
--
-- AUTO_INCREMENT pour la table `t_genres`
--
ALTER TABLE `t_genres`
  MODIFY `id_genre` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=159;
--
-- AUTO_INCREMENT pour la table `t_genres_films`
--
ALTER TABLE `t_genres_films`
  MODIFY `id_genre_film` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=158;
--
-- Contraintes pour les tables exportées
--

--
-- Contraintes pour la table `t_genres_films`
--
ALTER TABLE `t_genres_films`
  ADD CONSTRAINT `t_genres_films_ibfk_1` FOREIGN KEY (`fk_genre`) REFERENCES `t_genres` (`id_genre`),
  ADD CONSTRAINT `t_genres_films_ibfk_2` FOREIGN KEY (`fk_film`) REFERENCES `t_films` (`id_film`);
