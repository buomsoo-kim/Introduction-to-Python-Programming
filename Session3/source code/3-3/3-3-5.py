import pymysql

with open('data.txt', 'r') as f:
	lines = f.readlines()
	f.close()

conn = pymysql.connect(host = 'localhost', user = 'buomsoo', password = '12345', 
	db = 'company', charset= 'utf8')

curs = conn.cursor()

for line in lines:
	line = tuple(line.split())
	print(line)
	sql_query = "INSERT INTO employee VALUES ('{}', '{}', '{}', '{}', '{}', '{}')".format(*line)
	curs.execute(sql_query)
	conn.commit()

conn.close()