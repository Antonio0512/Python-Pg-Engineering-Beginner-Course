import os
import dotenv
import psycopg2

dotenv.load_dotenv()

connection = None
cur = None

try:
    connection = psycopg2.connect(
        host=os.environ.get('host'),
        port=os.environ.get('port'),
        database=os.environ.get('database'),
        user=os.environ.get('user'),
        password=os.environ.get('password')
    )
except psycopg2.Error as e:
    print("Error: Could not make connection to the postgres Database")
    print(e)

try:
    cur = connection.cursor()
except psycopg2.Error as e:
    print("Error: Could not get cursor to the Database")
    print(e)

connection.set_session(autocommit=True)

try:
    cur.execute("CREATE TABLE IF NOT EXISTS students (student_id int, name varchar,\
                age int, gender varchar, subject varchar, marks int);")
except psycopg2.Error as e:
    print("Error: Issue creating table")
    print(e)

try:
    cur.execute("INSERT INTO students (student_id, name, age, gender, subject, marks) \
                    VALUES (%s, %s, %s, %s, %s, %s)",
                (1, "Toni", 22, "Male", "Python", 99))
except psycopg2.Error as e:
    print("Error: Inserting Rows")
    print(e)

try:
    cur.execute("INSERT INTO students (student_id, name, age, gender, subject, marks) \
                    VALUES (%s, %s, %s, %s, %s, %s)",
                (1, "Irina", 23, "Female", "Python", 98))
except psycopg2.Error as e:
    print("Error: Inserting Rows")
    print(e)

try:
    cur.execute("SELECT * FROM students;")
except psycopg2.Error as e:
    print("Error: select *")
    print(e)

row = cur.fetchone()
while row:
    print(row)
    row = cur.fetchone()

cur.close()
connection.close()
