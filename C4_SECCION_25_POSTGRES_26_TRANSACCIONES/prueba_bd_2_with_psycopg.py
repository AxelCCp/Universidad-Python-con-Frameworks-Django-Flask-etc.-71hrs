
import psycopg2

conexion = psycopg2.connect(user='postgres', password='sasa', host='127.0.0.1', port='5432', database='test_db')

try:
    with conexion:
        with conexion.cursor() as cursor:
            sentencia = 'select * from persona'
            cursor.execute(sentencia)
            registros = cursor.fetchall()
            print(registros)
except Exception as e:
    print(f'Ocurrió un error: {e}')
finally:
    conexion.close()
