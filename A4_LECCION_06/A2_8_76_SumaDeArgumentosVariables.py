#SUMA TODOOS LOS NUMEROS Q SE RECIBAN POR PARAMETRO
def sumaNumeros(*args):
    suma = 0
    for num in args:
        suma += num
    return suma

print(sumaNumeros(5,5,6,10,20,20,100))

print(f'La suma de todos los números es: {sumaNumeros(5,20,50,10)}')

print('-------------------------CLASE 78---------------------------')

#MULTIPLICA TODOS LOS NUMEROS Q SE RECIBAN POR PARAMETRO
def multNumeros(*args):
    resultado = 1
    for num in args:
        resultado *= num
    return resultado

print(multNumeros(5,5,6,10))

print(f'La multiplicacion de todos los números es: {multNumeros(5,24,2)}')