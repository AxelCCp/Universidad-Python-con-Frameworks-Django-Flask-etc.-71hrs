from A0_117_FiguraGeometrica import *
from A1_117_Color import *

class Cuadrado(FiguraGeometrica, Color):
    
    def __init__(self, lado, color):
        FiguraGeometrica.__init__(self, lado, lado)
        Color.__init__(self, color)

    def calcularArea(self):
        return self._alto * self._ancho
    
    
    