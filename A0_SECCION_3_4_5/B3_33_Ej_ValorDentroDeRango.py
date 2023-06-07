#MI SOLUCION

valor = int(input('Ingresa un valor para ver si está dentro del rango: '))

if valor >= 0 and valor <= 5:
    print(f'El valor {valor} está dentro del rango entre 0 y 5')
else:
    print(f'El valor ingresado {valor}, no está dentro del rango entre 0 y 5')

#SOLUCION PROFESOR

valor2 = int(input('Ingresa un valor para ver si está dentro del rango: '))
rangoInf = 0
rangoSup = 5

dentroDeRango = (valor2 >= rangoInf) and (valor2 <= rangoSup)

if(dentroDeRango):
    print(f'El valor {valor2} está dentro del rango entre {rangoInf} y {rangoSup}')
else:
    print(f'El valor ingresado {valor2}, no está dentro del rango entre {rangoInf} y {rangoSup}')