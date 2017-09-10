CREATE DATABASE `COMPANY` CHARACTER SET utf8 COLLATE utf8_general_ci;

USE company;

CREATE TABLE `EMPLOYEE` (
	`fname` varchar(20),
	`lname` varchar(20),
	`id` int(6),
	`bdate` date,
	`sex` enum('F', 'M'),
	`salary` int(50)
);

INSERT INTO `EMPLOYEE` VALUES ('Scarlett', 'Johansson', '100001', '1984-11-22', 'F', '100000');
INSERT INTO `EMPLOYEE` VALUES ('Natalie', 'Portman', '100002', '1981-06-09', 'F', '250000');
INSERT INTO `EMPLOYEE` VALUES ('Emma', 'Stone', '100003', '1988-11-06', 'F', '350000');
INSERT INTO `EMPLOYEE` VALUES ('Ryan', 'Gosling', '100004', '1980-11-12', 'M', '340000');
INSERT INTO `EMPLOYEE` VALUES ('Tom', 'Hardy', '100005', '1977-09-15', 'M', '750000');