#!/usr/bin/env python
## Connecting to the database

## importing 'mysql.connector' as mysql for convenient
import mysql.connector as mysql
print('MySQL Database Connection')
## connecting to the database using 'connect()' method
## it takes 3 required parameters 'host', 'user', 'passwd'
db = mysql.connect(
    host = "localhost",
    user = "root",
    passwd = "Msar1982))*",
    database = "devices"
)
print('Mysql Connect Return:',db) # it will print a connection object if everything is fine
dbname='devices'
cursor = db.cursor()
cursor.execute("SHOW TABLES")
tables=cursor.fetchall()

print('List of table in database',dbname)
for table in tables:
    print(table)


cursor.execute("DESC farm_sensor")
print(cursor.fetchall())

query = "INSERT INTO farm_sensor (number,name, location,type) VALUES (%s,%s,%s,%s)"
values = (2, "infrared","10 10","infrared")

#cursor.execute(query, values)
#db.commit()

#print(cursor.rowcount, "record inserted")


read_query="SELECT * FROM farm_sensor"
cursor.execute(read_query)
records = cursor.fetchall()
for record in records:
    print(record)

