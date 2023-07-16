
import psycopg2

conexion = psycopg2.connect(user='postgres', password='sasa', host='127.0.0.1', port='5432', database='test_db')

try:
    with conexion:
        with conexion.cursor() as cursor:
            
            #sentencia = 'select * from persona where id_persona IN (1, 3)'
            #cursor.execute(sentencia)   

            sentencia = 'select * from persona where id_persona IN %s'
            llavesPrimarias = ((1,2,3),)                                                    #SON LO ARGUMENTOS Q SE LE PASAN A LA QUERY

            cursor.execute(sentencia, llavesPrimarias)             
            registros = cursor.fetchall()   
            for r in registros:
                print(r)

except Exception as e:
    print(f'Ocurrió un error: {e}')
finally:
    conexion.close()
