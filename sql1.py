import pyodbc
#connecting to northwind database
server = 'localhost, 1433'
database = 'Northwind'
username = 'SA'
password = 'Passw0rd2018'
docker_Northwind = pyodbc.connect('DRIVER={SQL Server};SERVER='+server+';DATABASE='+database+';'
                                  'UID='+username+';PWD='+ password)

#a cursor itself is a control structure
#allows us to control and manage rows of data from a response

cursor = docker_Northwind.cursor()

cursor.execute("SELECT @@version;")
row = cursor.fetchone()
# print("The row is", row)

cust_rows = cursor.execute("SELECT * FROM Customers;").fetchone()
# print("Customer rows are", cust_rows)

rows = cursor.execute("SELECT * FROM Products;").fetchall()
# for record in rows:
#     print(record.UnitPrice)

ln = cursor.execute("SELECT LastName FROM Employees").fetchall()
# print(ln)
# for record in ln:
#     print(record.LastName)

los = cursor.execute("SELECT * FROM Employees WHERE City IN ('Seattle', 'London')").fetchall()
# for record in los:
#     print(record.FirstName, record.LastName)




