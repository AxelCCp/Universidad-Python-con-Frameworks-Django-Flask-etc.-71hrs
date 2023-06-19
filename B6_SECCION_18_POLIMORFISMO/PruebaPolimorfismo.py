from Empleado import Empleado
from Gerente import Gerente

def imprimirDetalles(objeto):
    #print(objeto)
    print(type(objeto))
    print(objeto.monstrarDetalles())
    if isinstance(objeto, Gerente):
        print(objeto.departamento)

empleado = Empleado('Juan', 5000)
imprimirDetalles(empleado)

gerente = Gerente('Karla', 6000, 'Sistemas')
imprimirDetalles(gerente)
