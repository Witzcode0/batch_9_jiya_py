from . import dbConnection 

def create_table(table_name, col_config):
    sql = f"create table {table_name} ({col_config});"
    dbConnection.cursor.execute(sql)