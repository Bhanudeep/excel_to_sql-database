# Python code for creating Table in the Database
# Host: It is the server name. It will be "localhost"
# if you are using localhost database
today=str(123)
import mysql.connector as SQLC
def CreateTable():
	
	# Connecting To the Database in Localhost
	DataBase = SQLC.connect(
				host ="localhost",
				user ="root",
				password ="bhanudeep",
				database ="test"
			)

	# Cursor to the database
	Cursor = DataBase.cursor()

	# Query for Creating the table
	# The student table contains two columns Name and
	# Name of data type varchar i.e to store string
	# and Roll number of the integer data type.
    
	TableName ="CREATE TABLE students (Reg VARCHAR(255),Name VARCHAR(255) );"

	Cursor.execute(TableName)
	print("Student Table is Created in the Database")
	return

# Calling CreateTable function 
CreateTable()
