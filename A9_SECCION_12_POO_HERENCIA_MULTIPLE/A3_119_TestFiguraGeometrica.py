from A2_118_Cuadrado import Cuadrado

cuadrado1 = Cuadrado(5, 'Rojo')
print(cuadrado1.ancho)
print(cuadrado1.alto)
print(cuadrado1.color)
print(cuadrado1.calcularArea())


# 120
# MRO - METHOD RESOLUTION ORDER -DEVUELVE EL ORDEN DE JERARQUIA DE LAS CLASES EN HERENCIA MULTIPLE.
print(Cuadrado.mro())