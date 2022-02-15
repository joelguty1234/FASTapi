from os import getenv
import pymssql

server = "joel-sql.database.windows.net"
user = "joel"
password = "Valtx22fory"

conn = pymssql.connect(server, user, password, "JOEL-SQL-COURSERA")
cursor = conn.cursor()
cursor.execute(""" SELECT TOP (1000) [B_ID] FROM [dbo].[BOARD]""")


rows = cursor.fetchall()
print(rows)

for row in rows:
    print (row)
    
conn.close()



  