import pymysql
from config import host, user, password, db_name

try:
    connection = pymysql.connect(
    host = host,
    port = 3306,
    user = user,
    password = password,
    database = db_name,
    cursorclass = pymysql.cursors.DictCursor
    )
    print("Sucsesfully connected")
except Exception as ex:
    print("Connection refused")
    print(ex) 

try:
    with connection.cursor() as cursor:
        create_table_query = """CREATE TABLE 'toys'
                            (id int,
                            toy_id int,
                            name VARCHAR(32),
                            status ENUM('ok', 'broken', 'repair'),
                            status_updated TIMESTAMP(8), PRIMARY KEY (ID));
                            """
        cursor.execute(create_table_query)
        print("toys was created")

finally:
    connection.close

