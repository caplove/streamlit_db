
import sqlite3

# SQLite3 데이터베이스 연결 설정
conn = sqlite3.connect("database.db") # database.db 파일이 없으면 생성됨
# conn = sqlite3.connect(":memory:") # 메모리에 생성됨



# 테이블 생성
conn.execute('''CREATE TABLE IF NOT EXISTS car_owners
                (ID INT PRIMARY KEY NOT NULL,
                Name TEXT NOT NULL,
                Car TEXT NOT NULL);''')


# 데이터 삽입
data = [(1, "John", "Avante"),
        (2, "Jane", "Morning"),
        (3, "Mike", "Sonata")]

# # 데이터 삽입
# data = [(4, "Sarah", "Tucson"),
#     (5, "Michael", "Elantra"),
#     (6, "Emily", "Santa Fe")]

conn.executemany("INSERT INTO car_owners (ID, Name, Car) VALUES (?, ?, ?)", data)

# 변경사항 저장
conn.commit()

# 변경내용 출력
cursor = conn.cursor() # 커서 객체 생성
cursor.execute("SELECT * FROM car_owners") # SQL 쿼리 실행
results = cursor.fetchall() # 결과 가져오기
print(results)




# 결과를 DataFrame으로 표시
import pandas as pd
df = pd.DataFrame(results, columns=["ID", "Name", "Car"])
print(df)




# 연결 종료
conn.close()
