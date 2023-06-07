class Cubo:

    def __init__(self, base, altura, profundidad):
        self.base = base
        self.altura = altura
        self.profundidad = profundidad
    
    def areaCubo(self):
        areaCubo = self.base * self.altura * self.profundidad
        return areaCubo


base = int(input('Ingresa la base del cubo: '))
altura = int(input('Ingresa la altura del cubo: '))
profundidad = int(input('Ingresa la profundidad del cubo: '))

calculo1 = Cubo(base, altura, profundidad)

print(f'El area del cubo es: {calculo1.areaCubo()}')



