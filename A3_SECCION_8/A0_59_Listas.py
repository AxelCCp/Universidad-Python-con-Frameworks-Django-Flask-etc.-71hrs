print('-------------------------CLASE 59-----------------------------')

nombres = ['Juan', 'Erika', 'Ricardo', 'Karla']
#IMPRIME LA LISTA
print(nombres)
#PRIMER ELEMENTO DE LA LISTA
print(nombres[0])
#ULTIMO ELEMENTO DE LA LISTA
print(nombres[-1])
#PENULTIMO ELEMENTO DE LA LISTA
print(nombres[-2])

print('-------------------------CLASE 60-----------------------------')

#IMPRIMIR UN RANGO del 0 al 1, EL DOS NO LO INCLUYE
print(nombres[0:2])
#RECORRER LA LISTA HASTA UN INDICE INDICADO, SIN INCLUIR EL ÚLTIMO
print(nombres[:3])
#RECORER LA LISTA DESDE EL INDICE INDICADO HASTA EL FINAL
print(nombres[1:])
#CAMBIAR UN VALOR DE LA LISTA
nombres[3] = 'Ivone'
print(nombres)
#ITERAR LA LISTA
for nombre in nombres:
    print(nombre)
else:
    print('No existen más nombres en la lista')

print('-------------------------CLASE 60-----------------------------')

#LARGO DE LA LISTA
print(len(nombres))
#AGREGAR UN ELEMENTO
nombres.append('Lorenzo')
print(nombres)
#AGREGAR NOMBRE EN UN INDICE ESPECIFICO
nombres.insert(1,'Octavio')
print(nombres)
#QUITAR ELEMENTO
nombres.remove('Octavio')
print(nombres)
#ELIMINA EL ÚLTIMO ELEMENTO AGREGADO A LA LISTA
nombres.pop()
print(nombres)
#ELIMINAR ELEMENTO EN UN INDICE INDICADO
del nombres[2]
print(nombres)
#ELIMINA TODOS LOS ELEMENTOS DE LA LISTA
nombres.clear()
print(nombres)
#ELIMINA POR COMPLETO LA LISTA DE LA MEMORIA
del nombres
print(nombres) #ESTO DARÁ UN ERROR YA Q LA LISTA NO EXISTE.
