class Persona:
    
    def __init__(self, nombre, apellido, edad):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad

    #96
    def mostrarDetalle(self):
        print(f'Persona: {self.nombre} {self.apellido} {self.edad}')


print(type(Persona))

persona1 = Persona('Juan', 'Diaz', 35)

print(persona1.nombre)
print(persona1.apellido)
print(persona1.edad)
        
persona2 = Persona('Erika', 'Argentina', 37)
print(f'''
    nombre:    {persona2.nombre}
    apellido:  {persona2.apellido}
    edad:      {persona2.edad}
''')    

print('-------------------CLASE 95------MODIFICAR ATRIBUTOS--------------')

persona2.nombre = 'Katherine'
persona2.apellido = 'nnn'
persona2.edad = 45

print(f'''
    nombre:    {persona2.nombre}
    apellido:  {persona2.apellido}
    edad:      {persona2.edad}
''')   

print('-------------------CLASE 96------METODOS DE INSTANCIA--------------')

persona2.mostrarDetalle()

print('-----------97. Más de Self y Atributos de Instancia en Python-----------')

#OTRA SINTAXIS PARA LLAMAR AL METODO
Persona.mostrarDetalle(persona1)

#CREAR UN ATRIBUTO ADICIONAL AL OBJ
persona2.telefono = '8723634243'
persona2.mostrarDetalle()
print(persona2.telefono)
