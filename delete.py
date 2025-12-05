import connector

# #MySQL 연결 설정
# connection = mysql.connector.connect(
#     host = "localhost",
#     user = 'root',
#     password = '1234',
#     database = "python_test"
# )
connection = connector.get_connection()

cursor = connection.cursor() #데이터베이스 작업을 위한 커서 객체 생성

sql = "delete from users where name = %s"
values = ("Encore",)

cursor.execute(sql,values)
connection.commit()
print(f"{cursor.rowcount}개의 행이 삭제 되었습니다.")

cursor.close()
connection.close()