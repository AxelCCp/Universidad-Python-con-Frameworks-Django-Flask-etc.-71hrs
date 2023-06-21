from Monitor import Monitor
from Teclado import Teclado
from Raton import Raton


class Computadora:

    contadorComputadoras = 0

    def __init__(self, nombre, monitor, teclado, raton) -> None:
        Computadora.contadorComputadoras += 1
        self.__idComputadora = Computadora.contadorComputadoras
        self.__nombre = nombre
        self.__monitor = monitor
        self.__teclado = teclado
        self.__raton = raton

    def __str__(self) -> str:
        return f'''
        COMPUTADORA: 
            Id: {self.__idComputadora}
            Nombre: {self.__nombre}
            Monitor: {self.__monitor}
            Teclado: {self.__teclado}
            Ratón: {self.__raton}
        '''
    
    @property
    def idComputadora(self):
        return self.__idComputadora
    
    @property
    def nombre(self):
        return self.__nombre
    
    @nombre.setter
    def nombre(self, nombre):
        self.__nombre = nombre


if __name__ == '__main__':

    monitor1 = Monitor('msi', 'usb', 17)
    #print(monitor1)

    teclado1 = Teclado('msi', 'cable', 'gamer')
    #print(teclado1)

    raton1 = Raton('usb', 'msi', 'vertical')
    #print(raton1)

    pc1 = Computadora('msi katana', monitor1, teclado1, raton1)
    print(pc1)


    