from Monitor import Monitor
from Teclado import Teclado
from Raton import Raton
from Computadora import Computadora

class Orden:

    contadorOrden = 0
    def __init__(self, computadora):
        Orden.contadorOrden += 1
        self.__idOrden = Orden.contadorOrden
        self.__computadoras = computadora

    def __str__(self):
        pc_str = ''
        for c in self.__computadoras:
            pc_str += c.__str__()
        return f'''
            ORDEN: {self.__idOrden}
               {pc_str}
        '''
    

if __name__ == '__main__':

    monitor1 = Monitor('msi', 'usb', 17)
    teclado1 = Teclado('msi', 'cable', 'gamer')
    raton1 = Raton('usb', 'msi', 'vertical')
    pc1 = Computadora('msi katana', monitor1, teclado1, raton1)

    monitor2 = Monitor('asus', 'usb', 17)
    teclado2 = Teclado('asus', 'cable', 'gamer')
    raton2 = Raton('usb', 'asus', 'vertical')
    pc2 = Computadora('asus gamer', monitor2, teclado2, raton2)
    
    computadoras = [pc1, pc2]

    orden1 = Orden(computadoras)
    
    print(orden1)


    
