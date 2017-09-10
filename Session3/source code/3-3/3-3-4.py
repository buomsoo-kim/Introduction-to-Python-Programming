import pymysql

conn = pymysql.connect(host = 'localhost', user = 'buomsoo', password = '12345', 
	db = 'company', charset= 'utf8')

curs = conn.cursor()

sql_query = "INSERT INTO employee VALUES ('Daniel', 'Craig', '100006', '1968-03-02', 'M', '800000')"
curs.execute(sql_query)
conn.commit()

conn.close()