
import psycopg2

conexion = psycopg2.connect(user='postgres', password='sasa', host='127.0.0.1', port='5432', database='test_db')

try:
    with conexion:
        with conexion.cursor() as cursor:
            
            sentencia = 'select * from persona where id_persona IN %s'

            entrada = input('Proporciona los id\'s a buscar, (separado por comas): ')    
            llavesPrimarias = (tuple(entrada.split(',')),)                                     #ESTA TIENE Q SER UNA TUPLA DE TUPLAS, POR LO TANTO SE PONE TODO ENTRE PARENTESIS Y SE AGERGA UNA COMA.
            
            cursor.execute(sentencia, llavesPrimarias)             
            registros = cursor.fetchall()   
            for r in registros:
                print(r)

except Exception as e:
    print(f'Ocurrió un error: {e}')
finally:
    conexion.close()
