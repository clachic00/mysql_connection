import connector

# #MySQL 연결 설정
# connection = mysql.connector.connect(
#     host = "localhost",
#     user = 'root',
#     password = '1234',
#     database = "python_test"
# )
connection = connector.get_connection()


#cursor = connection.cursor() #데이터베이스 작업을 위한 커서 객체 생성
cursor = connection.cursor(dictionary=True) #딕셔너리로 가져오기
cursor.execute("SELECT * FROM users")

rows = cursor.fetchall() # 조회 결과를 가져온다

for row in rows:
    print(row) # 조회결과 출력
    
cursor.close()
connection.close()