
print('-----------------------------CLASE 64-------------------------------')
frutas = ('naranja', 'platano', 'guayaba') 
#LARGO DE UNA TUPLA
print(len(frutas))
#ACCEDER A UN ELEMENTO
print(frutas[0])
#NAVEGACION INVERSA .. ULTIMO ELEMENTO DE LA LISTA
print(frutas[-1])
#RANGO DE VALORES
print(frutas[0:2])  #SIN INCUIR EL uLTIMO INDICE.

print('-----------------------------CLASE 65-------------------------------')

#RECORRE LA TUPLA
for fruta in frutas:
    print(fruta)

#SIN SALTO DE LINEA
for fruta in frutas:
    print(fruta, end=' ')

#CAMBIAR UN VALOR DE UNA TUPLA .... NO SE PUEDEN MODIFICAR LOS ELEMENTOS DE UNA TUPLA
#frutas[0] = 'pera'
#print(frutas)

#PARA MODIFICAR UNA TUPLA INDIRECTAMENTE, MODIFICANDO LA TUPLA A UNA LISTA Y LUEGO LA LISTA A UNA TUPLA
frutasLista = list(frutas)
frutasLista[0] = 'pera'
frutas = tuple(frutasLista)
print(frutas)

print("...")

print('\n', frutas)


#ELIMINAR TUPLA
del frutas