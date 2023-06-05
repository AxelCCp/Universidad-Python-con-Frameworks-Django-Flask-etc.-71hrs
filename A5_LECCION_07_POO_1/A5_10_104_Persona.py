
print('--------------------104. Robusteciendo el Método Init--------------------')

class Persona:
    
    def __init__(self, nombre, apellido, edad, *args, **kwargs):                     # *args : PASA UNA TUPLA DE VALORES / **kwargs : PASA UN DICCIONARIO DE DATOS
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.args = args
        self.kwargs = kwargs

    def mostrarDetalle(self):
        print(f'''Persona: 
                  nombre: {self.nombre} 
                  apellido: {self.apellido} 
                  edad : {self.edad} 
                  tupla: {self.args} 
                  diccionario: {self.kwargs}''')


persona1 = Persona('otra persona', 'nnn', 30)

persona2 = Persona('Erika', 'Argentina', 37, '2738468232', 2,3,5, m='manzana', p='pera')

persona1.mostrarDetalle()

persona2.mostrarDetalle()
