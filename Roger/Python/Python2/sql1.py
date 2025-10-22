import mysql.connector 

mydb = mysql.connector.connect(
  host="localhost",
  user="roger",
  password="yourpassword"
)

print(mydb) 