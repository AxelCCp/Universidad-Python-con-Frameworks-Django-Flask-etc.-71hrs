class Monitor:

    def __init__(self, marca, tamano) -> None:
        Monitor.contadorMonitores += 1
        self.__idMonitor = Monitor.contadorMonitores
        self.__marca = marca
        self.__tamano = tamano

    def __str__(self) -> str:
        return f'Monitor: [id: {self._idMonitor}, marca: {self._marca}, tamaño: {self._tamano}]'
    
    @property
    def marca(self):
        return self.__marca
    
    @marca.setter
    def marca(self, marca):
        self.__marca = marca

    @property
    def tamano(self):
        return self.__tamano
    
    @tamano.setter
    def tamano(self, tamano):
        self.__tamano = tamano

    