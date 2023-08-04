#247

nombres1 = ['juan', 'karla', 'pedro']
nombres2 = 'laura maria, claudia, ernesto'.split()

print('------------#sumar listas--------------')
print(nombres1 + nombres2)  
print('')


print('----------#extender una lista con otroa lista----------')
nombres1.extend(nombres2)
print(nombres1)
print('')


#248
print('-------obtener el indice del 1er elemento encontrado en una lista--------')
numeros1 = [12,34,65,67,78,98,25,65]
print(f'indice 4 : {numeros1.index(65)}')
print('')   

print('------------Lista invertida------------')
numeros1.reverse()
print(f'Lista invertida: {numeros1}')
print('')

print('---------ordenar elementos de una lista-----------')
numeros1.sort()
print(numeros1)
print('')

print('---------ordenar elementos de una lista desc-----------')
numeros1.sort(reverse=True)
print(numeros1)
print('')

print('-------obtener el valor mínimo-------')
print(min(numeros1))
print('')

print('--------obtener el valor máximo-------')
print(max(numeros1))
print('')

print('---------copiar los elementos de una lista--------')                 #ESTO SOLO COPIA LAS REFERENCIAS 
numeros2 = numeros1.copy()
print(numeros2)

print(f'es misma referencia? : {numeros1 is numeros2}')                     #quiere decir que son obj's diferentes
print(f'es mismo contenido? : {numeros1 == numeros2}')
print('')  

print('---------copiar los elementos de una lista con slicing--------')
numeros2 = numeros1[:]
print(f'es misma referencia? : {numeros1 is numeros2}')                     
print(f'es mismo contenido? : {numeros1 == numeros2}')
print('')   


print('------------multiplicacion listas----------')
lista_mult = 5 * [[2,5]]
print(lista_mult)
print(f'es misma referencia? : {lista_mult[0] is lista_mult[1]}')                     
print(f'es mismo contenido? : {lista_mult[0] == lista_mult[1]}')

print('--------agregar elemento a lista multiplicada--------')
lista_mult[2].append(10)
print(lista_mult)