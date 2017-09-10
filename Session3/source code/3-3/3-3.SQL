SHOW DATABASES;

CREATE DATABASE university CHARACTER SET utf8 COLLATE utf8_general_ci;
SHOW DATABASES;

DROP DATABASE university;
SHOW DATABASES;

CREATE DATABASE university CHARACTER SET utf8 COLLATE utf8_general_ci;

CREATE TABLE `student` (
	`name` varchar(20),
	`id` int(5),
	`department` varchar(30),
	`birthday` date) ENGINGE = innodb;
SHOW TABLES;
DESC `student`;

DROP TABLE `student`;
SHOW TABLES;

CREATE TABLE `student` (
	`name` varchar(20),
	`id` int(5),
	`department` varchar(30),
	`birthday` date) ENGINGE = innodb;
SHOW TABLES;

INSERT INTO `student` VALUES ('Brad Pitt', '13001', 'Humanities', '1963-12-18');
INSERT INTO `student` VALUES ('Leonardo Dicaprio', '13002', 'Social sciences', '1974-11-11');
INSERT INTO `student` VALUES ('Tom Cruise', '13003', 'Engineering', '1962-07-03');
INSERT INTO `student` VALUES ('John Travolta', '13004', 'Engineering', '1954-02-18');
INSERT INTO `student` VALUES ('Kevin Costner', '13005', 'Humanities', '1955-01-18');
SELECT * FROM student;

UPDATE `student` SET birthday = '1963-12-24' WHERE id = '13001';
UPDATE `student` SET name = 'Tom Hanks' WHERE id = '13003';
SELECT * FROM student;

DELETE FROM `student` WHERE name = 'Leonardo Dicaprio';
SELECT * FROM student;

SELECT * FROM student;
SELECT name FROM student;
SELECT name, birthday FROM student;
SELECT * FROM student WHERE id = '13004';
SELECT * FROM student WHERE name = 'Tom Hanks';
