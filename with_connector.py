import mysql.connector

with mysql.connector.connect(
    host="localhost",
    user="root",
    password="1234",
    database="python_test"
) as connection:
    with connection.cursor() as cursor:
        cursor.execute("select * from users")
        for row in cursor.fetchall():
            print(row)

# close를 안해도 자동 종료 됨