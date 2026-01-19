from . import dbConnection

def insert_data():
    sql = "insert into students (name, age)values('brijesh gondaliya', 30)"
    dbConnection.cursor.execute(sql)
    dbConnection.conn.commit()
    