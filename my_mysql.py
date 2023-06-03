import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="YU_oppdivide!20"
)
mycursor = mydb.cursor()
mycursor.execute("SHOW DATABASES")
for database in mycursor:
    print(database[0])
