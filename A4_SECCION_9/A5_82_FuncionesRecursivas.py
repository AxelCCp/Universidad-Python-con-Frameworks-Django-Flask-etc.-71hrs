def factorial(numero):
    if numero == 1:
        return 1
    else:
        return numero * factorial(numero - 1)

numero = 5   
resultado = factorial(numero)

print(f'El resultado del factorial de {numero} es: {resultado}')