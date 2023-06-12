from FiguraGeometrica import FiguraGeoetrica
from Color import Color

class Cuadrado(FiguraGeoetrica, Color):

    def __init__(self, lado, color):
        FiguraGeoetrica.__init__(self, lado, lado)
        Color.__init__(self, color)

    def __str__(self) -> str:
        return f'{FiguraGeoetrica.__str__(self)}  {Color.__str__(self)}'

    def calcularArea(self):
        return self.alto * self.ancho

