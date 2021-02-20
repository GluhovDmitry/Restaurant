import psycopg2

conn = psycopg2.connect(dbname='django_db', user='dima', password='1', host='127.0.0.1')

cursor = conn.cursor()

#cursor.execute('INSERT INTO ')




