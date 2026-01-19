import mysql.connector

conn = mysql.connector.connect(
    user='root', 
    password='root',
    host='127.0.0.1',
    database="school"
    )

cursor = conn.cursor()

cursor.execute("SELECT CURDATE()")

row = cursor.fetchone()
print("Current date is: {0}".format(row[0]))