-- phpMyAdmin SQL Dump
-- version 4.5.4.1
-- http://www.phpmyadmin.net
--
-- Client :  localhost
-- Généré le :  Dim 28 Juin 2020 à 17:34
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
(1, 'Homme'),
(2, 'Femme'),
(3, 'Non Binaire'),
(4, 'Autre'),
(5, 'Hardcore'),
(6, 'Divinité'),
(7, 'Je ne vous aime pas tous'),
(8, 'Je vous aime tous'),
(10, 'Maccaud'),
(11, 'Sale Merde'),
(13, 'Loli'),
(16, 'FBI');

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
(1, 'Vendu'),
(2, 'à vendre'),
(3, 'à vérifier'),
(4, 'Inconnu');

-- --------------------------------------------------------

--
-- Structure de la table `t_stuff`
--

CREATE TABLE `t_stuff` (
  `id_stuff` int(11) NOT NULL,
  `name_stuff` varchar(64) NOT NULL,
  `description_stuff` longtext NOT NULL,
  `price_stuff` int(5) NOT NULL,
  `type_stuff` varchar(32) NOT NULL,
  `quantity_stuff` int(5) NOT NULL,
  `fk_user` int(11) DEFAULT NULL,
  `fk_state_stuff` int(11) NOT NULL,
  `fk_type_payment` int(11) NOT NULL,
  `date_add_stuff` date NOT NULL,
  `date_bought_stuff` date DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Contenu de la table `t_stuff`
--

INSERT INTO `t_stuff` (`id_stuff`, `name_stuff`, `description_stuff`, `price_stuff`, `type_stuff`, `quantity_stuff`, `fk_user`, `fk_state_stuff`, `fk_type_payment`, `date_add_stuff`, `date_bought_stuff`) VALUES
(1, 'Phare de Bentley', 'Phare de bentley, en très bon état', 99, 'Phare', 1, NULL, 2, 1, '2020-05-16', NULL),
(2, 'Vessie de Maccaud', 'Vessie usagée', 42, 'Pièce de corps humain', 1, NULL, 3, 5, '2020-01-07', NULL);

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
(1, 'Cash'),
(2, 'Carte Banquaire'),
(3, 'Twint'),
(4, 'Chèque'),
(5, 'Nature'),
(6, 'Carte cadeau');

-- --------------------------------------------------------

--
-- Structure de la table `t_user`
--

CREATE TABLE `t_user` (
  `id_user` int(11) NOT NULL,
  `firstname_user` varchar(64) NOT NULL,
  `lastname_user` varchar(64) NOT NULL,
  `mail` varchar(125) NOT NULL,
  `phone` int(14) NOT NULL,
  `address` varchar(128) NOT NULL,
  `city` varchar(64) NOT NULL,
  `npa` int(6) NOT NULL,
  `fk_gender` int(11) DEFAULT NULL,
  `date_user` date NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Contenu de la table `t_user`
--

INSERT INTO `t_user` (`id_user`, `firstname_user`, `lastname_user`, `mail`, `phone`, `address`, `city`, `npa`, `fk_gender`, `date_user`) VALUES
(1, 'Johan', 'Crocoll', 'johan.crocoll@infomaniak.ch', 761234567, 'rue des praliné', 'Nyon', 1234, 1, '2020-05-16'),
(2, 'Raphtalia', 'Iwatani', 'rising@shieldhero.jp', 413676875, 'boulevard des lolis', 'lolicity', 69, 2, '2020-05-16'),
(3, 'Rocco', 'Ronzano', 'roccoronzano@hotmail.com', 216914091, 'Route de Romainmôtier 8', 'Moiry VD', 1148, 6, '2020-05-16'),
(4, 'Atom', 'Le Furry', 'apple-chan@icloud.com', 216914091, 'rue des pommiers 69', 'sdgfsdfsdf', 6666, 16, '2020-06-16');

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
  MODIFY `id_gender` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=17;
--
-- AUTO_INCREMENT pour la table `t_state_stuff`
--
ALTER TABLE `t_state_stuff`
  MODIFY `id_state_stuff` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;
--
-- AUTO_INCREMENT pour la table `t_stuff`
--
ALTER TABLE `t_stuff`
  MODIFY `id_stuff` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;
--
-- AUTO_INCREMENT pour la table `t_type_payment`
--
ALTER TABLE `t_type_payment`
  MODIFY `id_type_payment` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;
--
-- AUTO_INCREMENT pour la table `t_user`
--
ALTER TABLE `t_user`
  MODIFY `id_user` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;
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

--
-- Contraintes pour la table `t_user`
--
ALTER TABLE `t_user`
  ADD CONSTRAINT `t_user_ibfk_1` FOREIGN KEY (`fk_gender`) REFERENCES `t_gender` (`id_gender`);

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
