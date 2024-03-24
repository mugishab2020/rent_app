import mysql.connector
mybd = mysql.connector(
    host="localhost",
    user="root",
    passwd= "mugishab2020"
)
my_cursor = mybd.cursor()
my_cursor.execute("CREATE DATABASE mydatabase")
my_cursor.execute("SHOW DATABASES")
for db in my_cursor:
    print(db)