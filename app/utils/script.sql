CREATE DATABASE IF NOT EXISTS `LibraryApp`;
USE `LibraryApp`;
CREATE TABLE IF NOT EXISTS `LibraryApp`.`users` ( 
    `id` INT(11) NOT NULL AUTO_INCREMENT , 
    `name` VARCHAR(255) NOT NULL ,
    `LastName` VARCHAR(255) NOT NULL ,
    `UserName` VARCHAR(255) NOT NULL ,
    `Password` VARCHAR(255) NOT NULL ,
    `PhoneNumber` int NOT NULL ,
    `Address` VARCHAR(255) NOT NULL ,
        
    PRIMARY KEY (`id`)) ENGINE = InnoDB;

CREATE TABLE IF NOT EXISTS `LibraryApp`.`books` ( 
    `id` INT(11) NOT NULL AUTO_INCREMENT , 
    `title` VARCHAR(255) NOT NULL ,
    `NumPages` int NOT NULL ,
    `Author` VARCHAR(255) NOT NULL ,
        
    PRIMARY KEY (`id`)) ENGINE = InnoDB;