from Cuadrado import Cuadrado
from Rectangulo import Rectangulo
from FiguraGeometrica import FiguraGeoetrica

print('Creacion de obj cuadrado'.center(50, '-'))
cuadrado1 = Cuadrado(7, 'Rojo')
print(f'Calculo  area cuadrado: {cuadrado1.calcularArea()}')
print(cuadrado1)

print('')

print('Creacion de obj rectangulo'.center(50, '-'))
rectangulo1 = Rectangulo(7, 8, 'verde')
print(f'Calculo area rectangulo: {rectangulo1.calcularArea()}')
print(rectangulo1)


print('Con descripcion de argumentos'.center(100, '-'))

print('Creacion de otr obj cuadrado'.center(50, '-'))
cuadrado1 = Cuadrado(lado=40, color='Rojo')
print(f'Calculo  area cuadrado: {cuadrado1.calcularArea()}')
print(cuadrado1)

print('')

print('Creacion de otro obj rectangulo'.center(50, '-'))
rectangulo2 = Rectangulo(ancho=9, alto=8, color='verde')
print(f'Calculo area rectangulo: {rectangulo1.calcularArea()}')
print(rectangulo1)

print('')

print('----------------PROBANDO LAS VALIDACIONES EN LOS SETTER DE FIGURA GEOMETRICA----------------------')

rectangulo3 = Rectangulo(ancho=9, alto=8, color='amarillo')

rectangulo3.alto = -10
rectangulo3.ancho = 200


print('-------------------------126 - Clases abstractas en python----------------------------')

#NO SE PUEDE INICIALIZAR UN OBJ DE UNA CLASE ABSTRACTA
#figura = FiguraGeoetrica()


#NUEVO ORDEN DE JERARQUIA DE CLASES CUANDO SE TIENE HERENCIA MULTIPLE Y CLASES ABSTRACTAS.
print(Cuadrado.mro())




