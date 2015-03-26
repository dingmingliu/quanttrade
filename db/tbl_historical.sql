/*
Navicat MySQL Data Transfer

Source Server         : localhost
Source Server Version : 50168
Source Host           : localhost:3306
Source Database       : quanttrade

Target Server Type    : MYSQL
Target Server Version : 50168
File Encoding         : 65001

Date: 2015-03-26 16:29:22
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for `tbl_historical`
-- ----------------------------
DROP TABLE IF EXISTS `tbl_historical`;
CREATE TABLE `tbl_historical` (
  `symbol` varchar(10) NOT NULL,
  `open` float NOT NULL,
  `high` float NOT NULL,
  `low` float NOT NULL,
  `close` float NOT NULL,
  `volume` int(20) NOT NULL,
  `date` date NOT NULL,
  PRIMARY KEY (`symbol`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of tbl_historical
-- ----------------------------
