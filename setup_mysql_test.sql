-- prepar MySQL server for the project
-- create database with new user and give it all priviledges

-- create database
CREATE DATABASE IF NOT EXISTS `hbnb_test_db`;
-- create a new user in database
CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost' IDENTIFIED BY 'hbnb_test_pwd';

-- grant all privilege to user in database
GRANT ALL PRIVILEGES ON `hbnb_test_db`.* TO 'hbnb_test'@'localhost';
-- grant select privilege to user from database
GRANT SELECT ON `performance_shema`.* TO 'hbnb_test'@'localhost';
