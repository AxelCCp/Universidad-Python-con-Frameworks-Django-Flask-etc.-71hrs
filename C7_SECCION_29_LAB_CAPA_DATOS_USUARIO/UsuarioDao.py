from CursorPool import CursorPool
from Usuario import Usuario
from MyLogger import log

class UsuarioDao:

    _SELECCIONAR = 'select * from usuarios order by id_usuario'
    _INSERTAR = 'insert into usuarios(username, password) values(%s, %s)'
    _ACTUALIZAR = 'update usuarios set username=%s, password=%s where id_usuario=%s'
    _ELIMINAR = 'delete from usuarios where id_usuario=%s'

    @classmethod
    def seleccionar(cls):
        with CursorPool() as cursor:
            cursor.execute(cls._SELECCIONAR)
            registros = cursor.fetchall()
            usuarios = []
            for r in registros:                                                                 #registros no es una lista del tipo persona, por esto se crea la lista personas.
                usuario = Usuario(r[0], r[1], r[2])        
                usuarios.append(usuario)
            return usuarios
         
    @classmethod
    def insertar(cls, usuario):
        with CursorPool() as cursor:
            log.debug(f'Usuario a insertar: {usuario}')
            valores = (usuario.username, usuario.password)
            cursor.execute(cls._INSERTAR, valores)
            log.debug(f'Usuario insertado: {usuario}')
            return cursor.rowcount
    
    @classmethod
    def actualizar(cls, usuario):
        with CursorPool() as cursor:
            valores = (usuario.username, usuario.password, usuario.id_usuario)
            cursor.execute(cls._ACTUALIZAR, valores)
            log.debug(f'Usuario actualizado: {usuario}')
            return cursor.rowcount
    
    @classmethod
    def eliminar(cls, usuario):
        with CursorPool() as cursor:      
            valores = (usuario.id_usuario,)                                                    #SE PASA UNA TUPLA CON UN SOLO VALOR
            cursor.execute(cls._ELIMINAR, valores)
            log.debug(f'Usuario eliminado: {usuario}')
            return cursor.rowcount
        
if __name__ == '__main__':

    '''
    usuario = Usuario(username='Mr.Satan', password='njibhuvgy')
    UsuarioDao.insertar(usuario)
    '''

    '''
    usuario = Usuario(id_usuario=5, username='Bulma', password='capCorp')
    UsuarioDao.actualizar(usuario)
    '''

    usuario = Usuario(id_usuario=2)
    UsuarioDao.eliminar(usuario)

    usuarios = UsuarioDao.seleccionar()
    for u in usuarios:
        log.debug(u)