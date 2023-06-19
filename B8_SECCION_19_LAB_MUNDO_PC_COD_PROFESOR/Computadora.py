from Teclado import Teclado
from Raton import Raton
from Monitor import Monitor

class Computadora:

    contador_computadoras = 0

    def __init__(self, nombre, monitor, teclado, raton):
        Computadora.contador_computadoras += 1
        self._id_computadora = Computadora.contador_computadoras
        self._nombre = nombre
        self._monitor = monitor
        self._teclado = teclado
        self._raton = raton

    def __str__(self):
        return f'''
        {self._nombre}: {self._id_computadora}
        Monitor: {self._monitor}
        Teclado: {self._teclado}
        Raton: {self._raton}
        '''
    

if __name__ == '__main__':
    teclado1 = Teclado('Hp', 'usb')
    raton1 = Raton('Hp', 'usb')
    monitor1 = Monitor('Hp', 'usb')

    computadora1 = Computadora('HP', monitor1, teclado1, raton1)
    print(computadora1)

    print('')

    teclado2 = Teclado('ACER', 'bluetooth')
    raton2 = Raton('ACER', 'bluetooth')
    monitor2 = Monitor('ACER', 'bluetooth')
    computadora2 = Computadora('ACER', monitor2, teclado2, raton2)
    print(computadora2)

    