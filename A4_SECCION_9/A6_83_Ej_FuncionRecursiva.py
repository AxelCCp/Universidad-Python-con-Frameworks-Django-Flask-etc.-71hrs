def imprimeNumero(numero):
    if numero == 1:
        print(1)
    else:
        print(numero)
        return imprimeNumero(numero-1)
    
imprimeNumero(5)

print('')

def imprimirNumeroRecursivo(numero):
    if numero >= 1:
        print(numero)
        imprimirNumeroRecursivo(numero-1)
    elif numero <= 0:
        print('valor incorrecto...')


imprimirNumeroRecursivo(8)