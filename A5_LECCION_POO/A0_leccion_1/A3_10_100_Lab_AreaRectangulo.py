
class Calculos:

    def __init__ (self, num1, num2):
        self.num1 = num1
        self.num2 = num2
    
    def areatriangulo(self):
        return self.num1 * self.num2

    
base = int(input('Ingresa la base del rectangulo: '))
altura = int(input('Ingresa la altura del rectangulo: '))

calculo1 = Calculos(base, altura)

print(f'El area del rectangulo es: {calculo1.areatriangulo()}')
