
import psycopg2 

conexion = psycopg2.connect(user='postgres', password='sasa', host='127.0.0.1', port='5432', database='test_db')

try:  

    conexion.autocommit = False                                                                                                #quiere decir q si no se hace commit al final del código, no se van a guardar los cambios.
    cursor = conexion.cursor()
    
    sentencia = 'insert into persona (nombre, apellido, email) values(%s, %s, %s)'
    valores = ('Androide', '16', '16@16.jp')
    cursor.execute(sentencia, valores)

    sentencia = 'update persona set nombre=%s, apellido=%s, email=%s where id_persona=%s'
    valores = ('Majin', 'Boo', 'boo@boo.jp', 8)
    cursor.execute(sentencia, valores)

    conexion.commit()
    print('Termina la transaccion, se hizo commit.')

except Exception as e:
    conexion.rollback();
    print(f'Ocurrió un error, se hizo rollback: {e} ')
finally:
    conexion.close()
