class Vehiculo:

    def __init__(self, color, ruedas):
        self.color = color
        self.ruedas = ruedas
    
    def __str__(self):
        return f'''
                    Vehiculo
                        Color: {self.color}
                        Ruedas: {self.ruedas}
                '''
    
class Coche(Vehiculo):

    def __init__(self, color, ruedas, velocidad):
        super().__init__(color, ruedas)
        self.velocidad = velocidad
    
    def __str__(self):
        return f'''
                {super().__str__()}
                        Velocidad: {self.velocidad}
                '''
    
class Bicicleta(Vehiculo):

    def __init__(self, color, ruedas, tipo):
        super().__init__(color, ruedas)
        self.tipo = tipo

    def __str__(self):
        return f'''
         {super().__str__()}
                    Tipo: {self.tipo}
        '''


vehiculo1 = Vehiculo('Plateado', 4)
print(vehiculo1)


coche1 = Coche('azul', 4 ,'10 km/hr')
print(coche1)


bici1 = Bicicleta('Rojo', 2, 'Montaña')
print(bici1)