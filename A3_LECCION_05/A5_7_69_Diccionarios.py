diccionario = {
    'IDE':'integrated development environment',
    'OOP':'object oriented programing',
    'DBMS':'database management system',
}
print(diccionario)

#LARGO 
print(len(diccionario))
#ACCEDER A UN ELEMENTO
print(diccionario['IDE'])
#OTRA FORMA DE RECUPERAR UN ELEMENTO
print(diccionario.get('OOP'))
#MODIFICAR ELEMENTOS
diccionario['IDE'] = 'IntegrateD DevelopmenT EnvironmenT'
print(diccionario['IDE'])

print('---------------------------- CLASE 70 -----------------------------')
#RECORRER LOS ELEMENTOS DEL DICCIONARIO
for termino in diccionario:
    print(termino)

#RECORRER LOS ELEMENTOS DEL DICCIONARIO..ACCEDE A LOS VALORES
for termino, valor in diccionario.items()   :
    print(termino, valor)

#RECORRER Y SOLO OBTENER LAS LLAVES
for termino in diccionario.keys():
    print(termino)

#RECORRER Y SOLO OBTENER LOS VALORES
for termino in diccionario.values():
    print(termino)

#COMPROBAR SI EXISTE UN ELEMENTO EN EL DICCIONARIO
print('IDE' in diccionario) 

#AGREGAR UN ELEMENTO
diccionario['PK '] = 'primary key'
print(diccionario)

#ELIMINAR ELEMENTO
diccionario.pop('DBMS')
print(diccionario)

#LIMPIAR EL DICCIONARIO
diccionario.clear()
print(diccionario)

#ELIMINAR EL DICCIONARIO
del diccionario

#DARÁ UN ERROR X X X
print(diccionario)