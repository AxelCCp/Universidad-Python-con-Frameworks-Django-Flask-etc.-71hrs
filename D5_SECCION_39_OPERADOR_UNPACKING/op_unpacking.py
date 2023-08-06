#253

numeros = [1,2,3]
print(numeros)
print(*numeros)
print(*numeros, sep=' - ')


#254 Unpacking como argumento
def sumar(a,b,c):
    print(f'resultado suma: {a + b + c}')

sumar(*numeros)


#255 extraer algunos elementos de una lista 
mi_lista = [1,2,3,4,5,6]
a,*b,c,d = mi_lista
print(a,b,c,d)


#256 crear listas con operador unpacking
lista1 = [1,2,3]
lista2 = [4,5,6]
lista3 = [lista1 , lista2]
print(f'lista de listas: {lista3}')

lista3 = [*lista1, *lista2]
print(f'lista 3 unida: {lista3}')

# unir diccionarios

dic1 = {'A':1, 'B':2, 'C':3}
dic2 = {'D':4, 'E':5}
dic3 = {**dic1, **dic2}
print(f'unir diccionarios: {dic3}')


#construir lista a partir de string
lista = [*'holaMundo']
print(lista)
print(*lista, sep='')
