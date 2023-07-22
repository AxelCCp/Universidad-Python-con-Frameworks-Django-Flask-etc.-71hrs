from Logger_base import log
from Conexion import Conexion

#199

class CursorDelPool:

    def __init__(self):
        self._conexion = None
        self._cursor = None

    #ESTE METODO SE ENCARGA DE OBTENER UNA CONEXION.
    def __enter__(self):
        log.debug('Inicio del metodo with __enter__')
        self._conexion = Conexion.obtenerConexion()
        self._cursor = self._conexion.cursor()
        return self._cursor
    
    #SE ENCARGA SE HACER COMMIT O ROLLBACK DE LA TRANSACCION. y TAMBN DE REGRESAR EL OBJ CONEXION AL POOL.
    def __exit__(self, tipo_excepcion, valor_excepcion, detalle_excepcion):
        log.debug('se ejecuta metodo __exit__')
        if valor_excepcion:
            self._conexion.rollback()
            log.error(f'Ocurrio una excepcion, se hace rollback: {valor_excepcion} {tipo_excepcion} {detalle_excepcion}')
        else:
            self._conexion.commit()
            log.debug('Commit de la transaccion')
        
        self._cursor.close()
        Conexion.liberarConexion(self._conexion)


if __name__== '__main__':
    with CursorDelPool() as cursor:
        log.debug('Dentro del bloque with')
        cursor.execute('Select * from persona')
        log.debug(cursor.fetchall())


    