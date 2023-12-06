
import sqlite3

# SQLite3 데이터베이스 연결 설정
conn = sqlite3.connect("database.db") # database.db 파일이 없으면 생성됨
# conn = sqlite3.connect(":memory:") # 메모리에 생성됨



# 테이블 생성
conn.execute('''CREATE TABLE IF NOT EXISTS pet_owners
                (ID INT PRIMARY KEY NOT NULL,
                Name TEXT NOT NULL,
                Pet TEXT NOT NULL);''')

# """
# 선택된 코드는 Python에서 SQLite 연결 객체의 execute 메서드를 사용하여 SQL 명령을 실행하는 부분입니다. 
# 이 명령은 SQLite 데이터베이스에 새 테이블을 생성합니다(이미 존재하지 않는 경우).

# 코드의 각 부분이 하는 일은 다음과 같습니다:
# CREATE TABLE IF NOT EXISTS pet_owners: 이 부분의 명령은 데이터베이스에 pet_owners라는 새 테이블을 생성합니다. 
# 단, 같은 이름의 테이블이 이미 존재하지 않는 경우에만 생성합니다. 
# IF NOT EXISTS 절은 테이블이 이미 존재하는 경우 오류가 발생하는 것을 방지합니다.
# (ID INT PRIMARY KEY NOT NULL, Name TEXT NOT NULL, Pet TEXT NOT NULL): 이 부분의 명령은 테이블의 열을 정의합니다. 
# 세 개의 열이 있습니다: ID, Name, Pet. 
# ID 열의 유형은 INT이며, 이는 테이블의 기본 키로, 고유한 값을 가져야 합니다. 
# Name과 Pet 열의 유형은 TEXT입니다. 각 열에 대한 NOT NULL 제약 조건은 열이 항상 값을 가져야 함을 의미합니다. 
# 이는 열을 비워 둘 수 없으며 NULL로 설정할 수 없습니다.
# conn.execute(...): 이 코드 줄은 SQL 명령을 실행합니다. 
# SQLite 연결 객체의 execute 메서드는 SQL 명령을 실행하는 데 사용됩니다.

# 요약하면, 이 코드는 SQLite 데이터베이스에 pet_owners라는 새 테이블을 생성하며, 
# 이 테이블에는 세 개의 열(ID, Name, Pet)이 있습니다. 
# 단, 테이블이 이미 존재하지 않는 경우에만 생성합니다.
# """


# 데이터 삽입
data = [(1, "John", "Dog"),
        (2, "Jane", "Cat"),
        (3, "Mike", "Bird")]


# data = [(4, "John2", "Dog2")]

conn.executemany("INSERT INTO pet_owners (ID, Name, Pet) VALUES (?, ?, ?)", data)
"""
이 코드는 pet_owners 테이블에 데이터를 삽입합니다.
conn.executemany(...): 이 코드 줄은 SQL 명령을 실행합니다.
이 경우 SQL 명령은 pet_owners 테이블에 데이터를 삽입하는 것입니다.
INSERT INTO pet_owners (ID, Name, Pet) VALUES (?, ?, ?): 이 부분의 명령은 pet_owners 테이블에 데이터를 삽입합니다.
(ID, Name, Pet) VALUES (?, ?, ?): 이 부분은 삽입할 데이터의 열을 지정합니다.
?는 데이터를 삽입할 때 사용할 값의 위치를 나타냅니다.
data: 이 코드 줄의 마지막 부분은 데이터를 나타냅니다.
data는 튜플의 리스트입니다.
각 튜플은 pet_owners 테이블의 열에 대한 데이터를 포함합니다.
"""

# 변경사항 저장
conn.commit()


# 변경내용 출력
cursor = conn.cursor() # 커서 객체 생성
cursor.execute("SELECT * FROM pet_owners") # SQL 쿼리 실행
results = cursor.fetchall() # 결과 가져오기
print(results)
"""
이 코드는 pet_owners 테이블의 모든 데이터를 가져옵니다.
cursor.execute(...): 이 코드 줄은 SQL 명령을 실행합니다.
이 경우 SQL 명령은 pet_owners 테이블의 모든 데이터를 가져오는 것입니다.
SELECT * FROM pet_owners: 이 부분의 명령은 pet_owners 테이블의 모든 데이터를 가져옵니다.
cursor.fetchall(): 이 코드 줄은 SQL 명령의 결과를 가져옵니다.
이 경우 SQL 명령의 결과는 pet_owners 테이블의 모든 데이터입니다.
"""




# 결과를 DataFrame으로 표시
import pandas as pd
df = pd.DataFrame(results, columns=["ID", "Name", "Pet"])
print(df)




# 연결 종료
conn.close()
