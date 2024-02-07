import sqlite3

connection=sqlite3.connect("student.db")
cursor=connection.cursor()

table_info="""
Create table STUDENT(NAME VARCHAR(25),CLASS VARCHAR(25),
SECTION VARCHAR(25),MARKS INT);

"""

cursor.execute(table_info)

cursor.execute('''Insert Into STUDENT values('Krish','Data Science','A',90)''')
cursor.execute('''Insert Into STUDENT values('Manohar','Math','B',85)''')
cursor.execute('''Insert Into STUDENT values('Patil','Physics','C',80)''')
cursor.execute('''Insert Into STUDENT values('Thakur','Python','D',75)''')


print("Inserted records are")

data=cursor.execute(''' Select * from STUDENT''')

for row in data:
    print(row)


connection.commit()
connection.close()