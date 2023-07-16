
import psycopg2

conexion = psycopg2.connect(user='postgres', password='sasa', host='127.0.0.1', port='5432', database='test_db')

try:
    with conexion:
        with conexion.cursor() as cursor:
            sentencia = 'update persona set nombre=%s, apellido=%s, email=%s where id_persona=%s'
            valores = ('Juan Carlos', 'Juarez', 'jcjuarez@mail.com', 1)
            cursor.execute(sentencia, valores)
            registros_actualizados = cursor.rowcount                                                                              
            print(f'Registros actualizados: {registros_actualizados}')
except Exception as e:
    print(f'Ocurrió un error: {e}')
finally:
    conexion.close()
