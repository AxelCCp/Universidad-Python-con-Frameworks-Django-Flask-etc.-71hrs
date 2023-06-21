from DispositivoDeEntrada import DispositivoDeEntrada

class Monitor(DispositivoDeEntrada):

    contadorMonitores = 0

    def __init__(self, tipoEntrada, marca, tamano) -> None:
        Monitor.contadorMonitores += 1
        self.__idMonitor = Monitor.contadorMonitores
        super().__init__(marca, tipoEntrada)
        self.__tamano = tamano

    def __str__(self) -> str:
        return f'Monitor: [id: {self.__idMonitor}  {super().__str__()}  tamaño: {self.__tamano}]'
    
    @property
    def IdMonitor(self):
        return self.__idMonitor 
    
    @property
    def marca(self):
        return self.__marca
    
    @marca.setter
    def marca(self, marca):
        self.__marca = marca

    @property
    def tipoEntrada(self):
        return self.__tipoEntrada
    
    @tipoEntrada.setter
    def tipoEntrada(self, tipoEntrada):
        self.__tipoEntrada = tipoEntrada

    @property
    def tamano(self):
        return self.__tamano
    
    @tamano.setter
    def tamano(self, tamano):
        self.__tamano = tamano

    
if __name__ == '__main__':

    monitor1 = Monitor('msi', 'usb', 17)
    print(monitor1)


    