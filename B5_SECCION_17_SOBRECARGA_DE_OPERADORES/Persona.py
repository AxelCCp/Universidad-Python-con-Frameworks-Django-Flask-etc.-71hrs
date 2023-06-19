class Persona:

    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    
    #SE SOBREESCRIBE EL METODO DE SUMA
    def __add__(self, other):
       # return self.nombre + other.nombre
       return f'{self.nombre}  {other.nombre}'
    
    #SE SOBREESCRIBE EL  METODO RESTA
    def __sub__(self, other):
        return self.edad - other.edad

#obj1 + obj2
#obj1.__add__(obj2)

persona1 = Persona('Juan', 28)
persona2 = Persona('Carlos', 50)

print(persona1 + persona2)
print(persona1 - persona2)