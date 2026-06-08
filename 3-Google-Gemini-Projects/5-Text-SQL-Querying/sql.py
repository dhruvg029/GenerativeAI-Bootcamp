import sqlite3
import pandas as pd

## create connection
connection = sqlite3.connect('students.db')

## Create a cursor table to insert, record, create tables, retrieve
cursor = connection.cursor()

## create table
cursor.execute('''
CREATE TABLE students (
    name VARCHAR(50),
    class VARCHAR(50),
    section VARCHAR(50),
    marks INT
)
''')

## insert records
cursor.execute('''
INSERT INTO students (name, class, section, marks) VALUES
('John', 'Data Science', 'A', 90),
('Jane', 'Data Science', 'B', 85),
('Bob', 'DevOps', 'C', 80),
('Alice', 'DevOps', 'A', 88),
('Charlie', 'Fullstack', 'B', 92)
''')

print('The inserted records into the table is as follows:')

data = cursor.execute('''
SELECT * FROM students
''')

## Displaying the data
for row in data:
    print(row)

connection.commit()
connection.close()