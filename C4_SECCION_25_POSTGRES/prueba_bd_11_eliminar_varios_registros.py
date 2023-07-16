
import psycopg2

conexion = psycopg2.connect(user='postgres', password='sasa', host='127.0.0.1', port='5432', database='test_db')

try:
    with conexion:
        with conexion.cursor() as cursor:
            sentencia = 'delete from persona where id_persona IN %s'
            entrada = input('Ingresa los id para eliminar, (separados por coma): ')
            valores = (tuple(entrada.split(',')),)                                                                  #SE PASA UNA TUPLA DE TUPLAS...
            cursor.execute(sentencia, valores)
            registros_eliminados = cursor.rowcount                                                                              
            print(f'Registros eliminados: {registros_eliminados}')
except Exception as e:
    print(f'Ocurrió un error: {e}')
finally:
    conexion.close()
