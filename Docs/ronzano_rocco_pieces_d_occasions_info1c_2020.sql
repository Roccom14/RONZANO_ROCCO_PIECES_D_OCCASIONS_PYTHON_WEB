-- phpMyAdmin SQL Dump
-- version 4.5.4.1
-- http://www.phpmyadmin.net
--
-- Client :  localhost
-- Généré le :  Ven 01 Mai 2020 à 09:00
-- Version du serveur :  5.7.11
-- Version de PHP :  5.6.18

-- Détection si une autre base de donnée du même nom existe

DROP DATABASE IF EXISTS ronzano_rocco_pieces_d_occasions_info1c_2020;

-- Création d'un nouvelle base de donnée

CREATE DATABASE IF NOT EXISTS ronzano_rocco_pieces_d_occasions_info1c_2020;

-- Utilisation de cette base de donnée

USE ronzano_rocco_pieces_d_occasions_info1c_2020;


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
-- Structure de la table `t_address`
--

CREATE TABLE `t_address` (
  `id_address` int(11) NOT NULL,
  `address` varchar(64) NOT NULL,
  `npa` int(8) NOT NULL,
  `city` varchar(32) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Structure de la table `t_gender`
--

CREATE TABLE `t_gender` (
  `id_gender` int(11) NOT NULL,
  `gender` varchar(32) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Structure de la table `t_mail`
--

CREATE TABLE `t_mail` (
  `id_mail` int(11) NOT NULL,
  `mail` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Structure de la table `t_payment`
--

CREATE TABLE `t_payment` (
  `id_payment` int(11) NOT NULL,
  `type_payment` varchar(64) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Structure de la table `t_phone`
--

CREATE TABLE `t_phone` (
  `id_phone` int(11) NOT NULL,
  `mobile_phone` int(16) NOT NULL,
  `phone` int(16) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Structure de la table `t_state_stuff`
--

CREATE TABLE `t_state_stuff` (
  `id_state_stuff` int(11) NOT NULL,
  `state_stuff` varchar(32) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Structure de la table `t_stuff`
--

CREATE TABLE `t_stuff` (
  `id_stuff` int(11) NOT NULL,
  `name_stuff` varchar(64) NOT NULL,
  `description_stuff` varchar(1000) NOT NULL,
  `price_stuff` int(11) NOT NULL,
  `type_stuff` varchar(64) NOT NULL,
  `fk_state_stuff` int(11) NOT NULL,
  `fk_payment` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Structure de la table `t_user`
--

CREATE TABLE `t_user` (
  `id_user` int(11) NOT NULL,
  `fistname_user` text NOT NULL,
  `lastname_user` text NOT NULL,
  `fk_stuff` int(11) NOT NULL,
  `fk_gender` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Structure de la table `t_user_address`
--

CREATE TABLE `t_user_address` (
  `id_user_address` int(11) NOT NULL,
  `fk_user` int(11) NOT NULL,
  `fk_address` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Structure de la table `t_user_mail`
--

CREATE TABLE `t_user_mail` (
  `id_user_mail` int(11) NOT NULL,
  `fk_user` int(11) NOT NULL,
  `fk_mail` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Structure de la table `t_user_phone`
--

CREATE TABLE `t_user_phone` (
  `id_user_phone` int(11) NOT NULL,
  `fk_user` int(11) NOT NULL,
  `fk_phone` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Index pour les tables exportées
--

--
-- Index pour la table `t_address`
--
ALTER TABLE `t_address`
  ADD PRIMARY KEY (`id_address`);

--
-- Index pour la table `t_gender`
--
ALTER TABLE `t_gender`
  ADD PRIMARY KEY (`id_gender`);

--
-- Index pour la table `t_mail`
--
ALTER TABLE `t_mail`
  ADD PRIMARY KEY (`id_mail`);

--
-- Index pour la table `t_payment`
--
ALTER TABLE `t_payment`
  ADD PRIMARY KEY (`id_payment`);

--
-- Index pour la table `t_phone`
--
ALTER TABLE `t_phone`
  ADD PRIMARY KEY (`id_phone`);

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
  ADD KEY `fk_state_stuff` (`fk_state_stuff`),
  ADD KEY `fk_payment` (`fk_payment`);

--
-- Index pour la table `t_user`
--
ALTER TABLE `t_user`
  ADD PRIMARY KEY (`id_user`),
  ADD KEY `fk_stuff` (`fk_stuff`),
  ADD KEY `fk_gender` (`fk_gender`);

--
-- Index pour la table `t_user_address`
--
ALTER TABLE `t_user_address`
  ADD KEY `fk_user` (`fk_user`),
  ADD KEY `fk_address` (`fk_address`);

--
-- Index pour la table `t_user_mail`
--
ALTER TABLE `t_user_mail`
  ADD KEY `fk_user` (`fk_user`),
  ADD KEY `fk_mail` (`fk_mail`);

--
-- Index pour la table `t_user_phone`
--
ALTER TABLE `t_user_phone`
  ADD PRIMARY KEY (`id_user_phone`),
  ADD UNIQUE KEY `fk_phone` (`fk_phone`),
  ADD KEY `fk_user` (`fk_user`);

--
-- AUTO_INCREMENT pour les tables exportées
--

--
-- AUTO_INCREMENT pour la table `t_address`
--
ALTER TABLE `t_address`
  MODIFY `id_address` int(11) NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT pour la table `t_gender`
--
ALTER TABLE `t_gender`
  MODIFY `id_gender` int(11) NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT pour la table `t_mail`
--
ALTER TABLE `t_mail`
  MODIFY `id_mail` int(11) NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT pour la table `t_payment`
--
ALTER TABLE `t_payment`
  MODIFY `id_payment` int(11) NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT pour la table `t_phone`
--
ALTER TABLE `t_phone`
  MODIFY `id_phone` int(11) NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT pour la table `t_state_stuff`
--
ALTER TABLE `t_state_stuff`
  MODIFY `id_state_stuff` int(11) NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT pour la table `t_stuff`
--
ALTER TABLE `t_stuff`
  MODIFY `id_stuff` int(11) NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT pour la table `t_user`
--
ALTER TABLE `t_user`
  MODIFY `id_user` int(11) NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT pour la table `t_user_phone`
--
ALTER TABLE `t_user_phone`
  MODIFY `id_user_phone` int(11) NOT NULL AUTO_INCREMENT;
--
-- Contraintes pour les tables exportées
--

--
-- Contraintes pour la table `t_stuff`
--
ALTER TABLE `t_stuff`
  ADD CONSTRAINT `t_stuff_ibfk_1` FOREIGN KEY (`fk_state_stuff`) REFERENCES `t_state_stuff` (`id_state_stuff`),
  ADD CONSTRAINT `t_stuff_ibfk_2` FOREIGN KEY (`fk_payment`) REFERENCES `t_payment` (`id_payment`);

--
-- Contraintes pour la table `t_user`
--
ALTER TABLE `t_user`
  ADD CONSTRAINT `t_user_ibfk_1` FOREIGN KEY (`fk_stuff`) REFERENCES `t_stuff` (`id_stuff`),
  ADD CONSTRAINT `t_user_ibfk_2` FOREIGN KEY (`fk_gender`) REFERENCES `t_gender` (`id_gender`);

--
-- Contraintes pour la table `t_user_address`
--
ALTER TABLE `t_user_address`
  ADD CONSTRAINT `t_user_address_ibfk_1` FOREIGN KEY (`fk_user`) REFERENCES `t_user` (`id_user`),
  ADD CONSTRAINT `t_user_address_ibfk_2` FOREIGN KEY (`fk_address`) REFERENCES `t_address` (`id_address`);

--
-- Contraintes pour la table `t_user_mail`
--
ALTER TABLE `t_user_mail`
  ADD CONSTRAINT `t_user_mail_ibfk_1` FOREIGN KEY (`fk_user`) REFERENCES `t_user` (`id_user`),
  ADD CONSTRAINT `t_user_mail_ibfk_2` FOREIGN KEY (`fk_mail`) REFERENCES `t_mail` (`id_mail`);

--
-- Contraintes pour la table `t_user_phone`
--
ALTER TABLE `t_user_phone`
  ADD CONSTRAINT `t_user_phone_ibfk_1` FOREIGN KEY (`fk_user`) REFERENCES `t_user` (`id_user`),
  ADD CONSTRAINT `t_user_phone_ibfk_2` FOREIGN KEY (`fk_phone`) REFERENCES `t_phone` (`id_phone`);

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
