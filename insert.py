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

# 데이터 삽입 쿼리
sql = "INSERT INTO users (name, email) values (%s, %s)"
values = ("Encore","encore@example.com")

cursor.execute(sql, values) # 쿼리 실행
connection.commit()         # 변경사항 커밋

print(f"{cursor.rowcount}개의 행이 변경 되었습니다.")

cursor.close()
connection.close()

