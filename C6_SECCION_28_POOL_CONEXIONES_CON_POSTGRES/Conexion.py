from Logger_base import log
from psycopg2 import pool 
import sys

class Conexion:
    _DATABASE = 'test_db'
    _USERNAME = 'postgres'
    _PASSWORD = 'sasa'
    _DB_PORT = '5432'
    _HOST = '127.0.0.1'
    _MIN_CON = 1
    _MAX_CON = 5
    _pool = None


    @classmethod
    def obtenerPool(cls):
        if cls._pool is None:
            try:
                cls._pool = pool.SimpleConnectionPool(cls._MIN_CON, 
                                                      cls._MAX_CON, 
                                                      host = cls._HOST, 
                                                      user = cls._USERNAME, 
                                                      password = cls._PASSWORD,
                                                      port = cls._DB_PORT,
                                                      database = cls._DATABASE)
                log.debug(f'Creacion del pool exitosa: {cls._pool}')
                return cls._pool
            except Exception as e:
                log.error(f'Ocurrió un error al obtener el pool {e}')
                sys.exit()
        else:
            return cls._pool


    @classmethod
    def obtenerConexion(cls):
        conexion = cls.obtenerPool().getconn()                                                           #CON ESTO SE OBTIENE EL POOL Y SE PIDE UNA DE LAS 5 CONEXIONES DEL POOL DE CONEXIONES.
        log.debug(f'Conexion obtenida del pool: {conexion}')
        return conexion
    
    @classmethod
    def liberarConexion(cls, conexion):
        cls.obtenerPool().putconn(conexion)
        log.debug(f'Regresamos la conexión al pool: {conexion}')

    @classmethod
    def cerrarConexiones(cls):
        cls.obtenerPool().closeall()
        
    

if __name__ == '__main__':
    #PROBANDO LA OBTENCION DE CONEXIONES.
    conexion1 = Conexion.obtenerConexion()
    Conexion.liberarConexion(conexion1)
    conexion2 = Conexion.obtenerConexion()
