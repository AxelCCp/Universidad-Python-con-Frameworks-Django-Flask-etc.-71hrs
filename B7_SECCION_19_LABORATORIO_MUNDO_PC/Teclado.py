from DispositivoDeEntrada import DispositivoDeEntrada

class Teclado(DispositivoDeEntrada):

    contadorTeclados = 0

    def __init__(self, tipoEntrada, marca, tipo) -> None:
        Teclado.contadorTeclados += 1
        self.__idTeclado = Teclado.contadorTeclados
        super().__init__(marca, tipoEntrada)
        self.__tipo = tipo

    def __str__(self) -> str:
        return f'Teclado: [id: {self.__idTeclado}] {super().__str__()} [tipo: {self.__tipo}] '
    
    @property
    def idTeclado(self):
        return self.__idTeclado
    
    @property
    def tipo(self):
        return self.__tipo
    
    @tipo.setter
    def tipo(self, tipo):
        self.__tipo = tipo

if __name__ == '__main__':

    teclado1 = Teclado('msi', 'cable', 'gamer')
    print(teclado1)


    
    
