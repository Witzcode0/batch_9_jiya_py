# from mySqlPck.createDatabase import create_db
from mySqlPck.createTable import create_table
from mySqlPck.insertData import insert_data
from mySqlPck.showData import show_data

# create_db("school")

# create_table("students", "id int primary key auto_increment, name varchar(155),age int")
# insert_data()

# print(show_data())

for student in show_data():
    print(student[1])