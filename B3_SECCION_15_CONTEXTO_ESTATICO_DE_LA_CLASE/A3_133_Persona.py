class Persona:

    contador_personas = 0

    def __init__(self, nombre, edad):
        #Persona.contador_personas += 1
        #self.id_persona = Persona.contador_personas
        self.id_persona = Persona.generar_siguiente_valor()                        #134 - ESTA ES UNA MEJORA A LAS 2 LINEAS COMENTADAS
        self.nombre = nombre
        self.edad = edad

    @classmethod
    def generar_siguiente_valor(cls):
        cls.contador_personas += 1
        return cls.contador_personas

    def __str__(self):
        return f'Persona[{self.id_persona} {self.nombre} {self.edad}]'
    
persona1 = Persona('Juan', 28)
print(persona1)

persona2 = Persona('Karla', 25)
print(persona2)

print(f'Valor contador personas: {Persona.contador_personas}')

persona3 = Persona('Erika', 37)
print(persona3)

print(f'Valor contador personas: {Persona.contador_personas}')
