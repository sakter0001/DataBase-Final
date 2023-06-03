import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="YU_oppdivide!20"
)
mycursor = mydb.cursor()
mycursor.execute("DROP DATABASE IF EXISTS menagerie")
for i in mycursor:
  print(i)