from Producto import Producto
from Orden import Orden

producto1 = Producto('Camisa', 100.00)
producto2 = Producto('Pantalon', 200.00)
producto3 = Producto('Calcetines', 50.00)
producto4 = Producto('Blusa', 70)

productos1 = [producto1, producto2]
productos2 = [producto3, producto4]

orden1 = Orden(productos1)
print(orden1)
print(f'Total de la orden1 {orden1.calcular_total()}')

print('')

orden2 = Orden(productos2)
print(orden2)
print(f'Total de la orden2 {orden2.calcular_total()}')

print('')

orden1.agregar_producto(producto3)
orden1.agregar_producto(producto4)
print(orden1)
print(f'Total de la orden1 {orden1.calcular_total()}')
