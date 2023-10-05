class Persona:

    contador_personas = 0
    
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido


#mostrar los atributos del obj
persona1 = Persona('juan', 'perez')
print(persona1.__dict__)                                                            #despliega un diccionario con los atributos de este obj.


#crear un atributo al vuelo
print(persona1.contador_personas)                                                   # accediendo al atributo de clase


# no es posible modificarlo con el obj, sino con la clase
persona1.contador_personas = 10                                                     # se asocia un nuevo atributo al obj persona1 con el mismo nombre del contador de la clase
print(persona1.__dict__)  


#ahora se accede atributo de clase
print(Persona.contador_personas)


# al crear un nuevo obj,  se consideran solo los atributos de la clase,  no se considera el atributo que se creo al vuelo
persona2 = Persona('kjhasd', 'askdhj')
print(persona2.__dict__)   


#se crea una variable de clase al vuelo
Persona.contador2 = 20
print(Persona.contador2)



