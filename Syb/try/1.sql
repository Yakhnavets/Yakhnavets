
#CREATE DATABASE sybbery;
USE sybbery;
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
    toy_id INT ,
    game_id INT NOT NULL,
    game_name varchar(32) NOT NULL,
    date_updated date
)ENGINE = InnoDB;

INSERT INTO games (toy_id, game_id, date_updated, game_name)
VALUES(1,1, '2018-03-19', 'car'),
(1,14, '2018-03-19', 'boat'),
(7,5, '2018-03-30', 'bear'),
(43,5,'2018-03-19', 'octopus5'),
(43,14,'2018-03-19', 'octopus14')
;

