from . import dbConnection

def show_data():
    sql = "select * from students"
    dbConnection.cursor.execute(sql)

    data = dbConnection.cursor.fetchall()
    return data