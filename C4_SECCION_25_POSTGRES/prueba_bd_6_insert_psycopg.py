
import psycopg2

conexion = psycopg2.connect(user='postgres', password='sasa', host='127.0.0.1', port='5432', database='test_db')

try:
    with conexion:
        with conexion.cursor() as cursor:
            sentencia = 'insert into persona(nombre, apellido, email) values(%s, %s, %s)'
            valores = ('Carlos', 'Lara', 'clara@gmail.com')
            cursor.execute(sentencia, valores)
            #conexion.commit()                                                                                                  #NO ES NECESARIO PQ SE ESTA USANDO EL BLOQUE WITH.
            registros_insertados = cursor.rowcount                                                                              #TE DICE CUANTOS REGISTROS SE HAN INSERTADO.
            print(f'Registros insertados: {registros_insertados}')
except Exception as e:
    print(f'Ocurrió un error: {e}')
finally:
    conexion.close()
