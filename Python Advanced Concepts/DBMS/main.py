import pyodbc

driver = 'ODBC Driver 17 for SQL Server'
server = 'SERVER=localhost: 1433'
port = 'PORT=1433'
db = 'DATABASE=main'
user = 'UID=root'
pw = 'PWD= Educative@123'

conn_str = ([driver, server, port, db, user, pw])
c = ['DRIVER={ODBC Driver 17 for SQL Server}', 'SERVER=localhost: 1433', 'DATABASE=main', 'UID=root', 'PWD= Educative@123']
conn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=localhost;DATABASE=master;UID=sa;PWD=Educative@123')

cursor = conn.cursor()
cursor.execute('select * from table_name')
row = cursor.fetchone()
rest_of_rows = cursor.fetchall()
print(rest_of_rows)