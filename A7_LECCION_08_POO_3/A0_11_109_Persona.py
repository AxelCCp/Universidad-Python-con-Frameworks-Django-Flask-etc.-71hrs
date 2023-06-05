
print('--------------------105. Encapsulamiento en Python--------------------')

class Persona:
    
    def __init__(self, nombre, apellido, edad):                  
        self._nombre = nombre
        self._apellido = apellido
        self._edad = edad

    def mostrarDetalle(self):
        print(f'''Persona: 
                  nombre: {self._nombre} 
                  apellido: {self._apellido} 
                  edad : {self._edad}''')

    
    #get
    @property                                                #CON PROPERTY SOLO SE PUEDE ACCEDER A LA VARIABLE CON EL METODO GET
    def nombre(self):
        return self._nombre

    #set
    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre

    @property
    def apellido(self):
        return self._apellido
    
    @apellido.setter
    def apellido(self, apellido):
        self._apellido = apellido

    @property
    def edad(self):
        return self._edad
    
    @edad.setter
    def edad(self, edad):
        self._edad = edad


#110 - ESTO ES PARA Q ESTE CÓDIGO SOLO SE EJECUTE SI ES QUE LE DAMOS RUN A ESTE ARCHIVO.
if __name__ == '__main__':
    persona1 = Persona('Juan', 'Perez', 37)
    persona1.mostrarDetalle()
    print('')

    #LLAMANDO AL METODO GET NOMBRE
    print(persona1.nombre)

    #LLAMANDO AL MÉTODO SET NOMBRE
    persona1.nombre = 'Juan Carlos'
    print(persona1.nombre)

    persona1.apellido = 'Lara'
    print(persona1.apellido)

    persona1.edad = 30
    print(persona1.edad)

    persona1.mostrarDetalle()

    print(__name__)
