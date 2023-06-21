from DispositivoDeEntrada import DispositivoDeEntrada

class Raton(DispositivoDeEntrada):

    contadorRatones = 0

    def __init__(self, tipoEntrada, marca, tipo) -> None:
        Raton.contadorRatones += 1
        self.__idRaton = Raton.contadorRatones
        super().__init__(marca, tipoEntrada)
        self.__tipo = tipo
        
    
    def __str__(self) -> str:
        return f'Ratón: [Id: {self.__idRaton}]  {super().__str__()}  [tipo: {self.__tipo}]'
    

    @property
    def idRaton(self):
        return self.__idRaton
    
    @property
    def tipo(self):
        return self.__tipo
    
    @tipo.setter
    def tipo(self, tipo):
        self.__tipo = tipo

if __name__ == '__main__':

    raton1 = Raton('usb', 'msi', 'vertical')
    print(raton1)

