import pymysql

#1. 연결
conn = pymysql.connect(host='localhost', user='leehyosang', password='q1w2e3', db='shopping_db_1')
#2. 커서
cur = conn.cursor()
#3. 쿼리 작성
cur.execute('select avg(age) from CUSTOMER where address = "gyeonggi"')
#4. 결과값 조회
result = cur.fetchone()
print(int(result[0]))
#5. 종료(연결 해제)
cur.close()
conn.close()
