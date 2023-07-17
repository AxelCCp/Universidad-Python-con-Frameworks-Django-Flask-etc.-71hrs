
import psycopg2 

conexion = psycopg2.connect(user='postgres', password='sasa', host='127.0.0.1', port='5432', database='test_db')

try:  
    with conexion:                                                                                             #quiere decir q si no se hace commit al final del código, no se van a guardar los cambios.
        with conexion.cursor() as cursor:
            
            sentencia = 'insert into persona (nombre, apellido, email) values(%s, %s, %s)'
            valores = ('Androide', '17', '17@17.jp')
            cursor.execute(sentencia, valores)

            sentencia = 'update persona set nombre=%s, apellido=%s, email=%s where id_persona=%s'
            valores = ('Up', '...', 'up@boo.jp', 6)
            cursor.execute(sentencia, valores)

except Exception as e:
    print(f'Ocurrió un error, se hizo rollback: {e} ')
finally:
    conexion.close()

print('Termina la transaccion, se hizo commit.')
