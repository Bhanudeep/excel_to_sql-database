import xlrd
import MySQLdb
import mysql.connector
from datetime import datetime,date
# now = datetime.now()
# mydb = mysql.connector.connect(
#   host="localhost",
#   user="root",
#   password="*********",
#   database="test",
#   auth_plugin='mysql_native_password'
# )

# mycursor = mydb.cursor()
# today = str(12345)
# day = now.strftime("%d")
# query="CREATE TABLE "+ "buss"+" (Reg VARCHAR(255), Faculty VARCHAR(255));"
# print(query)
# q=str(query)
# mycursor.execute(q)
# Open the workbook and define the worksheet
book = xlrd.open_workbook("template.xlsx")
sheet = book.sheet_by_name("Sheet1")

# Establish a MySQL connection
database = MySQLdb.connect (host="localhost", user = "root", passwd = "bhanudeep", db = "test")

# Get the cursor, which is used to traverse the database, line by line
cursor = database.cursor()

# Create the INSERT INTO sql query
query = """INSERT INTO NEW_TABLE (Reg,Name) VALUES (%s, %s)"""

# Create a For loop to iterate through each row in the XLS file, starting at row 2 to skip the headers
for r in range(1, sheet.nrows):
		Reg		= sheet.cell(r,0).value
		Name 	= sheet.cell(r,1).value		

		# Assign values from each row
		values = (Reg, Name)

		# Execute sql Query
		cursor.execute(query, values)

# Close the cursor
cursor.close()

# Commit the transaction
database.commit()

# Close the database connection
database.close()

# Print results
print ("")
print ("All Done! Bye, for now.")
print ("")
columns = str(sheet.ncols)
rows = str(sheet.nrows)
print ("I just imported " + "columns" +  " columns and " +  "rows" + " rows to MySQL!")
