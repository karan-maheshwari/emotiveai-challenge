import psycopg2

conn = psycopg2.connect("dbname=postgres host=localhost user=emotiveai password=emotiveai")

print(conn)
cursor = conn.cursor()
#cursor.execute("""DROP TABLE customers;""")
cursor.execute("""SELECT * from data""")
conn.commit() # <--- makes sure the change is shown in the database
rows = cursor.fetchall()
print(rows)
cursor.execute("""SELECT * from customers""")
conn.commit() # <--- makes sure the change is shown in the database
rows = cursor.fetchall()
print(rows)

conn.close()
cursor.close()
