#CREATE DATABASE sybbery;
USE sybbery;
CREATE TABLE IF NOT EXISTS toys(
    id INT PRIMARY KEY ,
    toy_id INT NOT NULL,
    toy_name varchar(32) NOT NULL,
    fix_status ENUM('ok', 'broken', 'repair'),
    status_updated timestamp
    
)ENGINE = InnoDB;

CREATE TABLE IF NOT EXISTS games(
    id INT PRIMARY KEY ,
    game_id INT NOT NULL,
    game_name varchar(32) NOT NULL,
    date_updated date
    
)ENGINE = InnoDB;

CREATE TABLE IF NOT EXISTS toys_games(
    id INT PRIMARY KEY ,
    game_id INT NOT NULL,
    toy_id INT NOT NULL,
    date_updated date
)ENGINE = InnoDB;



#CREATE DATABASE sybbery;
USE sybbery;
CREATE TABLE IF NOT EXISTS toys(
    id INT PRIMARY KEY ,
    toy_id INT NOT NULL auto_increment,
    toy_name varchar(32) NOT NULL,
    fix_status ENUM('ok', 'broken', 'repair'),
    status_updated date
    
)ENGINE = InnoDB;

INSERT INTO toys( toy_id, toy_name, fix_status, status_updated)
VALUES (1, 'boat', 'broken', 2018-03-19),
(7, 'Teddy Bear', 'ok',2018-03-30),
(43, 'octopus','ok', 2018-03-19)
;
CREATE TABLE IF NOT EXISTS games(
    id INT PRIMARY KEY ,
    game_id INT NOT NULL auto_increment,
    game_name varchar(32) NOT NULL,
    date_updated date,
    FOREIGN KEY (Id)  REFERENCES toys (Id) ON UPDATE CASCADE
)ENGINE = InnoDB;

INSERT INTO games (id, game_id, date_updated, game_name)
VALUES(1,1, 2018-03-19, 'car'),
(1,14, 2018-03-19, 'boat'),
(7,5, 2018-03-30, 'bear'),
(43,5,2018-03-19, 'octopus5'),
(43,14,2018-03-19, 'octopus14')
;
CREATE TABLE IF NOT EXISTS toys_games(
    id INT PRIMARY KEY,
    game_id INT NOT NULL,
    toy_id INT NOT NULL,
    note varchar(100),
    FOREIGN KEY (Id)  REFERENCES toys (Id) ON UPDATE CASCADE,
    FOREIGN KEY (game_id)  REFERENCES games (game_id) ON UPDATE CASCADE,
    FOREIGN KEY (toy_id)  REFERENCES toys (toy_id) ON UPDATE CASCADE
    
)ENGINE = InnoDB;


INSERT INTO toys_games (toy_id, game_id, note)
VALUES(1, 1, 'need repair'),
(1, 14, 'boat is broken'),
(7, 5, 'bear feels well'),
(43, 5, 'felt rather good though had no water to swim'),
(43, 14, 'two tentacles are lost')
;



