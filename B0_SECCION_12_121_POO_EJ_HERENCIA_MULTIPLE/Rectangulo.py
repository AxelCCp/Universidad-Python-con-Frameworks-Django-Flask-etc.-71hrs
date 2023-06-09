from FiguraGeometrica import FiguraGeometrica
from Color import Color

class Rectangulo(FiguraGeometrica, Color):

    def __init__(self, alto, ancho, color) -> None:
        FiguraGeometrica.__init__(self, alto, ancho)
        Color.__init__(self, color)
    
    def __str__(self):
        return f'''
                {super().__str__()}
                Color: {self.color}
                '''
    def calculaArea(self):
        return f'''
                Area: {self.alto * self.ancho}
                '''


