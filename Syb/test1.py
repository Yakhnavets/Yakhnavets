import mysql.connector
from mysql.connector import Error
from config import host, user, password, db_name


def create_connection_db(host, user, password, db_name = None):
    connectiondb = None
    try:
        connectiondb = mysql.connector.connect(
            host = host,
            port = 3306,
            user = user,
            password = password,
            database = db_name,
        )
        print("Sucsesfully connected")
    except Error as ex:
        print("Connection refused", ex)
    return connectiondb 

conn = create_connection_db(host, user, password)

try:
    with conn.cursor()as curssor:
        create_db_sql_query = 'CREATE DATABASE{}'.format('db_test')
        curssor.execute =(create_db_sql_query)
        print("db was created")
finally:
    curssor.close
    conn.close

conn = create_connection_db(host, user, password, 'db_test')

try:
    with conn.cursor()as curssor:
        create_table_query = """
        CREATE TABLE IF NOT EXIST toys(
        id INT AUTO_INCREMENT,
        toy_id INT AUTOINCREMENT,
        name VARCHAR(32),
        status ENUM('ok', 'broken', 'repair'),
        status_updated TIMESTAMP(8),
        PRIMARY KEY (ID)
        ) ENGINE = InnoDB"""
        curssor.execute(create_table_query)
        conn.commit

except Error as psd:
    print(psd)



