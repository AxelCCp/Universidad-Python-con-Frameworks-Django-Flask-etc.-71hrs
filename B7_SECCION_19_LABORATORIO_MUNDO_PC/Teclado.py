from DispositivoDeEntrada import DispositivoDeEntrada

class Teclado(DispositivoDeEntrada):

    def __init(self) -> None:
        Teclado.contadorTeclados += 1
        self._idTeclado = Teclado.contadorTeclados

    def __str__(self) -> str:
        return f'Teclado: [id: {self._idTeclado}]'
    
