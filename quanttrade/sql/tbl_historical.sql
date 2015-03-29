/*
Navicat MySQL Data Transfer

Source Server         : quanttrade
Source Server Version : 50623
Source Host           : localhost:3306
Source Database       : quanttrade

Target Server Type    : MYSQL
Target Server Version : 50623
File Encoding         : 65001

Date: 2015-03-29 22:53:47
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for tbl_historical
-- ----------------------------
DROP TABLE IF EXISTS `tbl_historical`;
CREATE TABLE `tbl_historical` (
  `id` int(20) unsigned NOT NULL AUTO_INCREMENT,
  `symbol` varchar(10) NOT NULL,
  `open` float NOT NULL,
  `high` float NOT NULL,
  `low` float NOT NULL,
  `close` float NOT NULL,
  `volume` bigint(20) NOT NULL,
  `date` date NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `uniq` (`symbol`,`date`) USING BTREE
) ENGINE=InnoDB AUTO_INCREMENT=4171468 DEFAULT CHARSET=utf8;
