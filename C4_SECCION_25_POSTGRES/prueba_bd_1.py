
import psycopg2

conexion = psycopg2.connect(user='postgres', password='sasa', host='127.0.0.1', port='5432', database='test_db')

print(conexion)

cursor = conexion.cursor()
sentencia = 'select * from persona'
cursor.execute(sentencia)
registros = cursor.fetchall()

print(registros)

cursor.close()
conexion.close()
