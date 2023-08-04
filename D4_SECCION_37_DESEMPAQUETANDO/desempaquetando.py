
#244

print('----------244-----------')

#desempaquetando
valores = 1,2,3
print(valores) 
print(type(valores))


valor1, valor2, valor3 = 1,2,3
print(valor1, valor2, valor3)


#el "_" se usa para definir q no se va a usar esa variable dentro del programa.
valor1, _, valor3 = 1,2,3

print(valor1, valor3)
print(_)


valor1, valor2, *valor3= 1,2,3,4,5,6,7,8,9
print(valor1, valor2, valor3)

valor1, valor2, *valor3, valor4, valor5= 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16
print(valor1, valor2, valor3, valor4, valor5)

print('----------245-----------')

valor1, valor2, *valor3, valor4, valor5= [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]
print(valor1, valor2, valor3, valor4, valor5)

def regresaVariosDatos():
    return 1,2,3

valor1, valor2, valor3 = regresaVariosDatos()
print(valor1, valor2, valor3)


valor1, *valores_restantes = regresaVariosDatos()
print(valor1, valores_restantes)

print('----------246-----------')

variable = '17:20'.partition(':')
print(type(variable))

hora, separador, minutos = '17:20'.partition(':')
print(hora, separador, minutos)

