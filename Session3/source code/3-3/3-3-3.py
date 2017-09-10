import pymysql

conn = pymysql.connect(host = 'localhost', user = 'buomsoo', password = '12345', 
	db = 'company', charset= 'utf8')

curs = conn.cursor()

sql_query = 'select fname, lname from employee'
curs.execute(sql_query)

rows = curs.fetchall()
for row in rows:
	print(row)

# sql_query = 'select * from employee'
# curs.execute(sql_query)

# rows = curs.fetchall()
# for row in rows:
# 	print('Name of the employee is: ', row[0] + ' ' + row[1])

conn.close()