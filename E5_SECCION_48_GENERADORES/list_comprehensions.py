#288 -------------------------------------------------------------------------------------------------------------------------------------------

numeros = range(10)
lista_pares = []

#creamos nueva lista con valores pares--------------------------------------------------

for numero in numeros:

    #revisa si el numero es par
    if numero % 2 == 0:
        lista_pares.append(numero * numero)

print(f'lista pares: {lista_pares}')


#ahora lo mismo, pero con list comprehension
# [expresion for var in coleccion if  condicion]
# la condicion del if es opcional

lista_todos = []
lista_pares = []

lista_todos = [numero * numero for numero in numeros]
lista_pares = [numero * numero for numero in numeros if numero % 2 == 0]

print(f'lista de todos con list comprehensions: {lista_todos}')

print(f'lista de pares con list comprehensions: {lista_pares}')


#ejemplo con dos condiciones ------------------------------------------------------------

pares = [numero for numero in range(50) if numero%2 == 0 if numero%6 == 0]

print(f'lista divisible entre 2 y entre 6: {pares}')


#ejemplo de pares e impares -------------------------------------------------------------

lista_pares = []
lista_impares = []

for numero in range (10):
    if numero % 2 == 0:
        lista_pares.append(numero)
    else:
        lista_impares.append(numero)

print(f'pares: {lista_pares}') 
print(f'impares: {lista_impares}') 



#ahora lo mismo, pero con list comprehension
lista_pares = []
lista_impares = []

[lista_pares.append(numero) if numero%2 == 0 else lista_impares.append(numero) for numero in range(10)]

print(f'pares: {lista_pares}') 
print(f'impares: {lista_impares}') 


#290 ---------------------------------------------------------------------------------------------------------------------------
#lista de listas
lista_de_listas = [[1,2,3], [4,5,6], [7,8,9,10]]

#convertimos la lista de listas en una sola lista

lista_simple = [valor for sublista in lista_de_listas for valor in sublista]
print(f'lista simple: {lista_simple}')


#ahora creamos una lista de numeros pares a partir de la lista de listas--------------------

#sin list comprehensions 
lista_pares = []
for sublista in lista_de_listas:
    for valor in sublista:
        if valor%2 == 0:
            lista_pares.append(valor)

print(f'pares: {lista_pares}')

#con list comprehensions
lista_pares = []
lista_pares = [valor for sublista in lista_de_listas for valor in sublista if valor%2==0]
print(f'pares: {lista_pares}')