import mysql.connector

dataBase=mysql.connector.connect(
	host='localhost',
	user='root',
	passwd='root'
	)

# cursor object
cursorObj = dataBase.cursor()

# create a database
cursorObj.execute("CREATE DATABASE mydb")
print("All Done!!")