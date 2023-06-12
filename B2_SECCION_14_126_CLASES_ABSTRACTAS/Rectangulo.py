from FiguraGeometrica import FiguraGeoetrica
from Color import Color

class Rectangulo(FiguraGeoetrica, Color):

    def __init__(self, alto, ancho, color):
        FiguraGeoetrica.__init__(self, ancho, alto)
        Color.__init__(self, color)

    def __str__(self):
        return f'{FiguraGeoetrica.__str__(self)}  {Color.__str__(self)}'
    
    def calcularArea(self):
        return self.alto * self.ancho
        