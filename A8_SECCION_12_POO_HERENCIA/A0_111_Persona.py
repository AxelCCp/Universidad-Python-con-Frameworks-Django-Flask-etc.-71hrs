class Persona:

    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def __str__(self):
        return f'''
                Empleado
                    Nombre: {self.nombre}
                    Edad: {self.edad}
                '''


class Empleado(Persona):

    def __init__(self, nombre, edad, sueldo):
        super().__init__(nombre, edad)  
        self.sueldo = sueldo
    
    #SOBREESCRIBE EL TO STRING
    def __str__(self):
        return f'''
                {super().__str__()}
                    Sueldo: {self.sueldo}
                '''


"""
empleado1 = Empleado('Juan', 28, 5000)

print(f'''
Empleado
    Nombre: {empleado1.nombre}
    Edad: {empleado1.edad}
    Sueldo: {empleado1.sueldo}
''')

"""