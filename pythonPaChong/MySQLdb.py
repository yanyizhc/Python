#coding:utf-8
import MySQLdb

conn = MySQLdb.connect(host="localhost",user="root",passwd="admin123",db="python_mysql",charset="utf8")    

cur = conn.cursor()
sql = "select * from python_user"

aadata = cur.execute(sql)

info = cur.fetchmany(aadata)

for i in info:
	print i
	
cur.close()
conn.commit()
conn.close()