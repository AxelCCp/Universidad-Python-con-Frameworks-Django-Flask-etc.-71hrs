#simulacion de sobrecarga de constructores 

class Persona:

    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido

    @classmethod
    def crearPersonaVacia(cls):
        return cls(None, None)
    
    @classmethod
    def crearPersonaConValores(cls, nombre, apellido):
        return cls(nombre, apellido)
    
    def __str__(self) -> str:
        return f'Nombre: {self.nombre}, apellido: {self.apellido}'

#forma 1 para crear obj
persona1  = Persona('juan', 'perez')
print(persona1)

#forma 2 para crear obj
persona_vacio = Persona.crearPersonaVacia()
print(persona_vacio)


#forma 3 para crear obj con valores
persona_con_valores = Persona.crearPersonaConValores('kasjhd','aioa')
print(persona_con_valores)






