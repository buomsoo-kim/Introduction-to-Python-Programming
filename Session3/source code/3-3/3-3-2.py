import pymysql

conn = pymysql.connect(host = 'localhost', user = 'buomsoo', password = '12345', 
	db = 'company', charset= 'utf8')

curs = conn.cursor()

sql_query = 'select * from employee'
curs.execute(sql_query)

rows = curs.fetchall()
print(rows)

conn.close()