
import psycopg2

conexion = psycopg2.connect(user='postgres', password='sasa', host='127.0.0.1', port='5432', database='test_db')

try:
    with conexion:
        with conexion.cursor() as cursor:
            sentencia = 'select * from persona where id_persona=%s'
            id_persona = input('Proporciona el id_persona: ')
            cursor.execute(sentencia, (id_persona,))                                       #SE PASA UNA TUPLA CON EL ID_PERSONA
            #registros = cursor.fetchall()                                                  #DEVUELVE UNA LISTA DE REGISTROS
            registro = cursor.fetchone()                                                   #DEVUELVE 1 SOLO REGISTRO       
            #print(f'REGISTROS: {registros}')
            print(f'REGISTRO: {registro}')
except Exception as e:
    print(f'Ocurrió un error: {e}')
finally:
    conexion.close()
