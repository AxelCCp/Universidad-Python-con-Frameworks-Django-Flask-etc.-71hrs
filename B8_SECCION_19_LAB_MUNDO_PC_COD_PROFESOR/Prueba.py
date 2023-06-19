from Teclado import Teclado
from Raton import Raton
from Monitor import Monitor
from Computadora import Computadora
from Orden import Orden


teclado1 = Teclado('Hp', 'usb')
raton1 = Raton('Hp', 'usb')
monitor1 = Monitor('Hp', 'usb')
computadora1 = Computadora('HP', monitor1, teclado1, raton1)


print('')

teclado2 = Teclado('ACER', 'bluetooth')
raton2 = Raton('ACER', 'bluetooth')
monitor2 = Monitor('ACER', 'bluetooth')
computadora2 = Computadora('ACER', monitor2, teclado2, raton2)


teclado3 = Teclado('Gamer', 'bluetooth')
raton3 = Raton('Gamer', 'bluetooth')
monitor3 = Monitor('Gamer', '34')
computadora3 = Computadora('GAMER', monitor3, teclado3, raton3)


computadoras1 = [computadora1, computadora2]
orden1 = Orden(computadoras1)
print(orden1)

print('')

orden1.agregar_computadora(computadora3)
print(orden1)