
CREATE SCHEMA `syberry` ;
USE syberry;
CREATE TABLE IF NOT EXISTS toys(
    id INT PRIMARY KEY auto_increment,
    toy_id INT NOT NULL,
    toy_name varchar(32) NOT NULL,
    fix_status ENUM('ok', 'broken', 'repair'),
    status_updated date
    
)ENGINE = InnoDB;

INSERT INTO toys(toy_id, toy_name, fix_status, status_updated)
VALUES (1, 'boat', 'broken', '2018-03-19'),
(7, 'Teddy Bear', 'ok', '2018-03-30'),
(43, 'octopus','ok', '2018-03-19')
;

CREATE TABLE IF NOT EXISTS games(
    id INT PRIMARY KEY auto_increment ,
    game_id INT NOT NULL,
    game_name varchar(32) NOT NULL,
    date_updated date
    
)ENGINE = InnoDB;

INSERT INTO games (game_id, date_updated, game_name)
VALUES(1, '2018-02-12', 'Ships in the ocean '),
(5,'2018-03-30', 'ZOO Railroad'),
(14,'2018-03-18', 'Octopus-destroyer')

;

CREATE TABLE IF NOT EXISTS toys_games(
    id INT PRIMARY KEY auto_increment,
    game_id INT NOT NULL,
    toy_id INT NOT NULL,
    note varchar(100)
    
)ENGINE = InnoDB;
INSERT INTO toys_games (toy_id, game_id, note)
VALUES(1, 1, 'need repair'),
(1, 14, 'boat is broken'),
(7, 5, 'bear feels well'),
(43, 5, 'felt rather good though had no water to swim'),
(43, 14, 'two tentacles are lost')
;
SELECT * 
FROM toys_games
INNER JOIN games WHERE games.game_id = toys_games.game_id;

SELECT * 
FROM toys_games
INNER JOIN toys WHERE toys.toy_id = toys_games.toy_id;


#------------------------------------------------------------Task1

CREATE TABLE IF NOT EXISTS toys_repair(
    id INT PRIMARY KEY auto_increment,
    toy_id INT NOT NULL,
    issue_description varchar(100)
    )
;
INSERT INTO toys_repair(toy_id, issue_description) SELECT toy_id, note FROM toys_games 
;

SELECT *
FROM toys_repair
INNER JOIN toys ON toys.toy_id = toys_repair.toy_id WHERE fix_status = 'repair'
;


#--------------------------------------------------------------------Task2
SELECT *
FROM toys_games 
JOIN games  ON games.game_id = toys_games.game_id
INNER JOIN toys ON toys.toy_id = toys_games.toy_id WHERE status_updated < 2022-01-31   #DATEADD(year,-1,GETDATE())
;

#----------------------------------------------------------------Task4

SELECT *
FROM toys INNER JOIN toys_repair ON toys_repair.toy_id = toys.toy_id WHERE fix_status = 'ok'
;

#-----------------------------------------------------------------Task5