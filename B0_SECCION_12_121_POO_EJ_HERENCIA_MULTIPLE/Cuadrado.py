from FiguraGeometrica import FiguraGeometrica
from Color import Color

class Cuadrado(FiguraGeometrica, Color):

    def __init__(self, lado, color) -> None:
        FiguraGeometrica.__init__(self, lado, lado)
        Color.__init__(self, color)
    
    def __str__(self):
        return f'''
                {super().__str__()}
                Color: {self.color}
                '''

    def calcularArea(self):
        return self.alto * self.ancho
    



