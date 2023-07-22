from Conexion import Conexion
from Persona import Persona
from Logger_base import log
from Cursor_del_pool import CursorDelPool

class PersonaDao:
    
    _SELECCIONAR = 'select * from persona order by id_persona'
    _INSERTAR = 'insert into persona(nombre, apellido, email) values(%s, %s, %s)'
    _ACTUALIZAR = 'update persona set nombre=%s, apellido=%s, email=%s where id_persona=%s'
    _ELIMINAR = 'delete from persona where id_persona=%s'

    @classmethod
    def seleccionar(cls):
        with CursorDelPool() as cursor:
            cursor.execute(cls._SELECCIONAR)
            registros = cursor.fetchall()
            personas = []
            for r in registros:                                                                 #registros no es una lista del tipo persona, por esto se crea la lista personas.
                persona = Persona(r[0], r[1], r[2], r[3])        
                personas.append(persona)
            return personas
        

    @classmethod
    def insertar(cls, persona):
        with CursorDelPool() as cursor:
            log.debug(f'Persona a insertar: {persona}')
            valores = (persona.nombre, persona.apellido, persona.email)
            cursor.execute(cls._INSERTAR, valores)
            log.debug(f'Persona insertada: {persona}')
            return cursor.rowcount
            

    @classmethod
    def actualizar(cls, persona):
        with CursorDelPool() as cursor:
            valores = (persona.nombre, persona.apellido, persona.email, persona.id_persona)
            cursor.execute(cls._ACTUALIZAR, valores)
            log.debug(f'Persona actualizada: {persona}')
            return cursor.rowcount
            
    @classmethod
    def eliminar(cls, persona):
        with CursorDelPool() as cursor:      
            valores = (persona.id_persona,)                                                    #SE PASA UNA TUPLA CON UN SOLO VALOR
            cursor.execute(cls._ELIMINAR, valores)
            log.debug(f'Objeto eliminado: {persona}')
            return cursor.rowcount
            
        
if __name__ == '__main__':

    
    ''' # INSERT
    persona1 = Persona(nombre='puar', apellido='...', email='puar@mail.com')
    personas_insertadas = PersonaDao.insertar(persona1)
    log.debug(f'Personas insertadas: {personas_insertadas}')
    '''

    ''' # UPDATE 
    persona1 = Persona(12, 'Maron...', 'xxxxxx', 'maron@mail.jp')
    personas_actualizadas = PersonaDao.actualizar(persona1)
    log.debug(f'Personas actualizadas: {personas_actualizadas}')
    '''

    ''' # DELETE
    persona1 = Persona(id_persona=10)
    personas_eliminadas = PersonaDao.eliminar(persona1)
    log.debug(f'Personas eliminadas: {personas_eliminadas}')
    '''
            
    #READ
    personas = PersonaDao.seleccionar()
    for p in personas:
        log.debug(p)


