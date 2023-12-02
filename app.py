import sqlite3
import pandas as pd
import streamlit as st

print("Hello, world!")

def main():
    # SQLite3 데이터베이스 연결 설정
    conn = sqlite3.connect("database.db") # database.db 파일이 없으면 생성됨

    # 데이터베이스에 존재하는 테이블 이름으로 부터 UI 생성하여, 테이블 선택하고, 결과를 출력하는 코드

    # 테이블 이름을 가져옴
    cursor = conn.cursor() # 커서 객체 생성
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';") # SQL 쿼리 실행
    results = cursor.fetchall() # 결과 가져오기
    table_names = [result[0] for result in results] # 테이블 이름만 가져옴
    print(table_names)

    # 테이블 선택 UI 생성
    table_name = st.sidebar.selectbox("테이블 선택", table_names)

    # 테이블 선택
    cursor.execute(f"SELECT * FROM {table_name}") # SQL 쿼리 실행
    results = cursor.fetchall() # 결과 가져오기

    # 결과를 DataFrame으로 표시
    df = pd.DataFrame(results, columns=[description[0] for description in cursor.description])
    st.dataframe(df)

    # 연결 종료
    conn.close()


if __name__ == '__main__':
    main()

