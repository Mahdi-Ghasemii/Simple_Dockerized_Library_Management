CREATE DATABASE IF NOT EXISTS `LibraryApp`;
USE `LibraryApp`;
CREATE TABLE IF NOT EXISTS `LibraryApp`.`users` ( 
    `Id` INT(11) NOT NULL UNIQUE PRIMARY KEY AUTO_INCREMENT, 
    `Name` VARCHAR(255) NOT NULL,
    `LastName` VARCHAR(255) NOT NULL,
    `UserName` VARCHAR(255) NOT NULL,
    `Password` VARCHAR(255) NOT NULL,
    `PhoneNumber` VARCHAR(255) NOT NULL,
    `Address` VARCHAR(255) NOT NULL,
        
    CHECK(LENGTH(Name) > 2),
    CHECK(LENGTH(LastName) > 2),
    CHECK(LENGTH(UserName) > 2),
    CHECK(LENGTH(Password) > 7),
    CHECK(LENGTH(PhoneNumber) = 10),
    CHECK(LENGTH(Address) > 5)
);

CREATE TABLE IF NOT EXISTS `LibraryApp`.`books` ( 
    `Id` INT(11) NOT NULL UNIQUE PRIMARY KEY AUTO_INCREMENT , 
    `Title` VARCHAR(255) NOT NULL,
    `NumPages` INT NOT NULL,
    `Author` VARCHAR(255) NOT NULL,

    CHECK(LENGTH(Title) > 2),
    CHECK(NumPages > 1),
    CHECK(LENGTH(Author) > 2)
       
);