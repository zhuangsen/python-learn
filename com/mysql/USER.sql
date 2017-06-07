/*
Navicat MySQL Data Transfer

Source Server         : mysql
Source Server Version : 50718
Source Host           : localhost:3306
Source Database       : test

Target Server Type    : MYSQL
Target Server Version : 50718
File Encoding         : 65001

Date: 2017-06-04 10:48:18
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for USER
-- ----------------------------
DROP TABLE IF EXISTS `USER`;
CREATE TABLE `USER` (
  `userid` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`userid`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of USER
-- ----------------------------
INSERT INTO `USER` VALUES ('1', 'name1');
INSERT INTO `USER` VALUES ('2', 'name2');
INSERT INTO `USER` VALUES ('3', 'name3');
INSERT INTO `USER` VALUES ('4', 'name4');
INSERT INTO `USER` VALUES ('5', 'name5');
INSERT INTO `USER` VALUES ('6', 'name6');
INSERT INTO `USER` VALUES ('7', 'name7');
INSERT INTO `USER` VALUES ('8', 'name8');
INSERT INTO `USER` VALUES ('9', 'name9');
SET FOREIGN_KEY_CHECKS=1;
