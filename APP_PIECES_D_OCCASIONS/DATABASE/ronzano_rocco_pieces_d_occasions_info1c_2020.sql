-- phpMyAdmin SQL Dump
-- version 4.5.4.1
-- http://www.phpmyadmin.net
--
-- Client :  localhost
-- Généré le :  Jeu 02 Juillet 2020 à 05:35
-- Version du serveur :  5.7.11
-- Version de PHP :  5.6.18

-- Détection si une autre base de donnée du même nom existe

DROP DATABASE IF EXISTS ronzano_rocco_pieces_d_occasions_info1c_2020;

-- Création d'un nouvelle base de donnée

CREATE DATABASE IF NOT EXISTS ronzano_rocco_pieces_d_occasions_info1c_2020;

-- Utilisation de cette base de donnée

USE ronzano_rocco_pieces_d_occasions_info1c_2020;
-- --------------------------------------------------------

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de données :  `ronzano_rocco_pieces_d_occasions_info1c_2020`
--

-- --------------------------------------------------------

--
-- Structure de la table `t_gender`
--

CREATE TABLE `t_gender` (
  `id_gender` int(11) NOT NULL,
  `gender` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Contenu de la table `t_gender`
--

INSERT INTO `t_gender` (`id_gender`, `gender`) VALUES
(1, '-'),
(2, 'Homme'),
(3, 'Femme'),
(4, 'Non Binaire'),
(5, 'Autre'),
(6, 'Hardcore'),
(7, 'Divinité'),
(8, 'Je ne vous aime pas tous'),
(9, 'Je vous aime tous'),
(10, 'Maccaud'),
(11, 'Sale Merde'),
(13, 'Loli'),
(16, 'FBI'),
(20, 'Licorne'),
(21, 'Stitch');

-- --------------------------------------------------------

--
-- Structure de la table `t_state_stuff`
--

CREATE TABLE `t_state_stuff` (
  `id_state_stuff` int(11) NOT NULL,
  `state_stuff` varchar(32) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Contenu de la table `t_state_stuff`
--

INSERT INTO `t_state_stuff` (`id_state_stuff`, `state_stuff`) VALUES
(1, '-'),
(2, 'Vendu'),
(3, 'à vendre'),
(4, 'à vérifier'),
(5, 'Inconnu'),
(7, 'Pas à vendre');

-- --------------------------------------------------------

--
-- Structure de la table `t_stuff`
--

CREATE TABLE `t_stuff` (
  `id_stuff` int(11) NOT NULL,
  `name_stuff` varchar(64) DEFAULT NULL,
  `description_stuff` longtext,
  `price_stuff` int(5) DEFAULT NULL,
  `type_stuff` varchar(32) DEFAULT NULL,
  `quantity_stuff` int(5) DEFAULT NULL,
  `fk_user` int(11) DEFAULT NULL,
  `fk_state_stuff` int(11) DEFAULT NULL,
  `fk_type_payment` int(11) DEFAULT NULL,
  `date_add_stuff` date DEFAULT NULL,
  `date_bought_stuff` date DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Contenu de la table `t_stuff`
--

INSERT INTO `t_stuff` (`id_stuff`, `name_stuff`, `description_stuff`, `price_stuff`, `type_stuff`, `quantity_stuff`, `fk_user`, `fk_state_stuff`, `fk_type_payment`, `date_add_stuff`, `date_bought_stuff`) VALUES
(9, 'Acer Nitro', 'Ordi Portable', 1200, 'Laptop', 1, 4, 7, 3, '2020-06-29', '2020-07-06'),
(10, 'iMac 27\'\'', 'Imac 27\'\' de 2015', 2399, 'Ordinateur AiO', 56, 4, 7, 3, '2020-05-12', '2020-07-07'),
(11, 'Souris Logitech M523', 'Souris silencieuse wireless', 50, 'Souris', 140, 7, 5, 4, '2012-04-12', '2009-12-23'),
(12, 'Clavier DEll', 'Clavier business', 46, 'Clavier', 140, 7, 5, 4, '2019-07-14', '2008-03-01'),
(13, 'Ecrans Dell 27\'\'', 'Ecrans Dell business', 399, 'Ecran', 140, 7, 5, 4, '2007-03-23', '2010-07-16'),
(14, 'adfadf', 'asdfsdf', 123, 'asdfadf', 123, 12, 3, 5, '2020-06-30', '2020-06-29');

-- --------------------------------------------------------

--
-- Structure de la table `t_type_payment`
--

CREATE TABLE `t_type_payment` (
  `id_type_payment` int(11) NOT NULL,
  `type_payment` varchar(32) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Contenu de la table `t_type_payment`
--

INSERT INTO `t_type_payment` (`id_type_payment`, `type_payment`) VALUES
(1, '-'),
(2, 'Cash'),
(3, 'Carte Banquaire'),
(4, 'Twint'),
(5, 'Chèque'),
(6, 'Nature'),
(7, 'Carte cadeau');

-- --------------------------------------------------------

--
-- Structure de la table `t_user`
--

CREATE TABLE `t_user` (
  `id_user` int(11) NOT NULL,
  `firstname_user` varchar(64) DEFAULT NULL,
  `lastname_user` varchar(64) DEFAULT NULL,
  `mail_user` varchar(125) DEFAULT NULL,
  `phone_user` int(14) DEFAULT NULL,
  `address_user` varchar(128) DEFAULT NULL,
  `city_user` varchar(64) DEFAULT NULL,
  `npa_user` int(6) DEFAULT NULL,
  `fk_gender` int(11) DEFAULT NULL,
  `date_add_user` date DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Contenu de la table `t_user`
--

INSERT INTO `t_user` (`id_user`, `firstname_user`, `lastname_user`, `mail_user`, `phone_user`, `address_user`, `city_user`, `npa_user`, `fk_gender`, `date_add_user`) VALUES
(1, '-', '', 'johan.crocoll@infomaniak.ch', 761234567, 'rue des praliné', 'Nyon', 1234, 1, '2020-05-16'),
(2, 'Johan', 'Crocoll', 'johan.crocoll@infomaniak.ch', 761234567, 'rue des praliné', 'Nyon', 1234, 1, '2020-05-16'),
(3, 'Raphtalia', 'Iwatani', 'rising@shieldhero.jp', 413676875, 'boulevard des lolis', 'lolicity', 69, 2, '2020-05-16'),
(4, 'Rocco', 'Ronzano', 'roccoronzano@hotmail.com', 216914091, 'Route de Romainmôtier 8', 'Moiry VD', 1148, 6, '2020-05-16'),
(7, 'Alex', 'le pd', 'alex@lepd.us', 696969696, 'rue des penis', 'clitoland', 420, 1, '2020-06-01'),
(9, 'Olivier', 'Maccaud', 'bdepsic@yahoo.fr', 764946692, 'OM de la 707', 'Om de Bex', 1880, 10, '1962-06-17'),
(10, 'Jérôme', 'Cosandey', 'jerome.cosandey@epfl.ch', 12345678, 'rue des bâteaux', 'Cosandey-Land', 1234, 1, '2020-06-29'),
(11, 'Netscape-chan', 'Meme Girl', 'netscape@netscape.com', 12345678, 'netscape road', 'Netscape City', 1980, 1, '1980-01-01'),
(12, 'test', 'test', 'test@test.ch', 5465465, 'khgjkh', 'uzgkjg', 654, 6, '2020-03-12');

--
-- Index pour les tables exportées
--

--
-- Index pour la table `t_gender`
--
ALTER TABLE `t_gender`
  ADD PRIMARY KEY (`id_gender`);

--
-- Index pour la table `t_state_stuff`
--
ALTER TABLE `t_state_stuff`
  ADD PRIMARY KEY (`id_state_stuff`);

--
-- Index pour la table `t_stuff`
--
ALTER TABLE `t_stuff`
  ADD PRIMARY KEY (`id_stuff`),
  ADD KEY `fk_user` (`fk_user`),
  ADD KEY `fk_state_stuff` (`fk_state_stuff`),
  ADD KEY `fk_type_payment` (`fk_type_payment`);

--
-- Index pour la table `t_type_payment`
--
ALTER TABLE `t_type_payment`
  ADD PRIMARY KEY (`id_type_payment`);

--
-- Index pour la table `t_user`
--
ALTER TABLE `t_user`
  ADD PRIMARY KEY (`id_user`),
  ADD KEY `fk_gender` (`fk_gender`);

--
-- AUTO_INCREMENT pour les tables exportées
--

--
-- AUTO_INCREMENT pour la table `t_gender`
--
ALTER TABLE `t_gender`
  MODIFY `id_gender` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=22;
--
-- AUTO_INCREMENT pour la table `t_state_stuff`
--
ALTER TABLE `t_state_stuff`
  MODIFY `id_state_stuff` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;
--
-- AUTO_INCREMENT pour la table `t_stuff`
--
ALTER TABLE `t_stuff`
  MODIFY `id_stuff` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=15;
--
-- AUTO_INCREMENT pour la table `t_type_payment`
--
ALTER TABLE `t_type_payment`
  MODIFY `id_type_payment` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;
--
-- AUTO_INCREMENT pour la table `t_user`
--
ALTER TABLE `t_user`
  MODIFY `id_user` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=13;
--
-- Contraintes pour les tables exportées
--

--
-- Contraintes pour la table `t_stuff`
--
ALTER TABLE `t_stuff`
  ADD CONSTRAINT `t_stuff_ibfk_1` FOREIGN KEY (`fk_state_stuff`) REFERENCES `t_state_stuff` (`id_state_stuff`),
  ADD CONSTRAINT `t_stuff_ibfk_2` FOREIGN KEY (`fk_type_payment`) REFERENCES `t_type_payment` (`id_type_payment`),
  ADD CONSTRAINT `t_stuff_ibfk_3` FOREIGN KEY (`fk_user`) REFERENCES `t_user` (`id_user`);

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
