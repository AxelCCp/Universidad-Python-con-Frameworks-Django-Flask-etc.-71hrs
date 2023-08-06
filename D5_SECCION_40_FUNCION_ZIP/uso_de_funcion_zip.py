#uso de funcion zip
#print(dir(__builtins__))

numeros = [1,2,3]
letras = ['a','b','c']
mezcla = zip(numeros, letras)  
print(mezcla)
print(list(mezcla))


print(tuple(zip(numeros, letras)))


#258
numeros = [1,2,3]
letras = ['a','b','c']
identificadores = [321,432,543,645,765]
mezcla = zip(numeros, letras, identificadores)
print(list(mezcla))


numeros = [1,2,3]
letras = ['a','b','c']
identificadores = [321,432,543,645,765]
conjunto = {1,2,3,4,5,6,7,8}                                                               # es un set {}
mezcla = zip(numeros, letras, identificadores, conjunto)
print(list(mezcla))


#259 iterar en paralelo

for numero, letra, id, aleatorio in zip(numeros, letras, identificadores, conjunto):
    print(f'numero: {numero}, letra: {letra}, id: {id}, aleatorio: {aleatorio}')


nueva_lista = []
for numero, letra, id, aleatorio in zip(numeros, letras, identificadores, conjunto):
    nueva_lista.append(f'{id}-{numero}-{letra}-{aleatorio}')
print(nueva_lista)


#260 unzip
mezcla = [(1, 'a'), (2,'b'), (3,'c')]
numeros, letras = zip(*mezcla)
print(f'numeros: {numeros} letras: {letras}')



#261 ordenar un zip
letras = ['c','a','d','e','b']
numeros = [3,1,2,4,0]
mezcla = zip(letras,numeros)
print(tuple(mezcla))
#ordenar por letra
print(sorted(zip(letras, numeros)))
#ordenar por num
print(sorted(zip(numeros, letras)))


#262 crear diccionario con zip
llaves  = ['nombre', 'apellido', 'edad']
valores = ['juan', 'perez', 18]
diccionario  = dict(zip(llaves, valores))
print(diccionario)

#actualizar elemento de diccionario
llave = ['edad']
nueva_edad = [28]
diccionario.update(zip(llave, nueva_edad))
print(diccionario)

#agregar elemento de diccionario
llave = ['phone']
phone = [28234243]
diccionario.update(zip(llave, phone))
print(diccionario)



