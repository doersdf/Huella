# ************************************************************
# Generación bbdd inicial HUELLA
# 
# Author: Antonio Jiménez (antonio@doersfd.com)
# http://www.doersdf.com/
# Database Name: fichaje
# ************************************************************


# Volcado de tabla employees
# ------------------------------------------------------------

DROP TABLE IF EXISTS `employees`;

CREATE TABLE `employees` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(60) COLLATE utf8_spanish_ci NOT NULL,
  `email` varchar(60) COLLATE utf8_spanish_ci NOT NULL,
  `code` int(6) NOT NULL,
  `fingerprint` varchar(200) COLLATE utf8_spanish_ci NOT NULL,
  `week_hours` int(11) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_spanish_ci;



# Volcado de tabla sessions
# ------------------------------------------------------------

DROP TABLE IF EXISTS `sessions`;

CREATE TABLE `sessions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `day` date NOT NULL,
  `start` time NOT NULL,
  `end` time DEFAULT NULL,
  `employee` int(11) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_spanish_ci;

LOCK TABLES `sessions` WRITE;
/*!40000 ALTER TABLE `sessions` DISABLE KEYS */;

# Volcado de tabla users
# ------------------------------------------------------------

DROP TABLE IF EXISTS `users`;

CREATE TABLE `users` (
  `username` varchar(60) COLLATE utf8_spanish_ci NOT NULL,
  `password` varchar(200) COLLATE utf8_spanish_ci NOT NULL,
  `email` varchar(60) COLLATE utf8_spanish_ci NOT NULL,
  `token` varchar(200) COLLATE utf8_spanish_ci DEFAULT NULL,
  `expire` datetime NOT NULL,
  PRIMARY KEY (`username`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_spanish_ci;



# Volcado de tabla vwSesiones
# ------------------------------------------------------------

DROP VIEW IF EXISTS `vwSesiones`;

CREATE TABLE `vwSesiones` (
   `idSesion` INT(11) NULL DEFAULT NULL,
   `day` DATE NOT NULL,
   `fichajes` BIGINT(21) NOT NULL DEFAULT '0',
   `horas` DECIMAL(39) NULL DEFAULT NULL,
   `employee` INT(11) NOT NULL,
   `email` VARCHAR(60) NULL DEFAULT NULL,
   `idSesions` TEXT NULL DEFAULT NULL,
   `Intervalos` TEXT NULL DEFAULT NULL,
   `week_hours` INT(11) NULL DEFAULT NULL
) ENGINE=MyISAM;





# Replace placeholder table for vwSesiones with correct view syntax
# ------------------------------------------------------------

DROP TABLE `vwSesiones`;

CREATE ALGORITHM=UNDEFINED DEFINER=`root`@`192.168.0.%` SQL SECURITY DEFINER VIEW `vwSesiones`
AS SELECT
   max(`sessions`.`id`) AS `idSesion`,
   `sessions`.`day` AS `day`,count(`sessions`.`day`) AS `fichajes`,sum(((time_to_sec(timediff(`sessions`.`end`,
   `sessions`.`start`)) / 60) / 60)) AS `horas`,
   `sessions`.`employee` AS `employee`,
   `employees`.`email` AS `email`,group_concat(`sessions`.`id` order by `sessions`.`id` ASC separator ',') AS `idSesions`,group_concat(concat(`sessions`.`start`,' a ',`sessions`.`end`) order by `sessions`.`start` ASC separator ', ') AS `Intervalos`,
   `employees`.`week_hours` AS `week_hours`
FROM (`sessions` left join `employees` on((`sessions`.`employee` = `employees`.`id`))) group by `sessions`.`day`,`sessions`.`employee`,`employees`.`email`,`employees`.`week_hours`;
