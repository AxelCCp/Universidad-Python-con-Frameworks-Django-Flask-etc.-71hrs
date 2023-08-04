#251

matriz = [[10, 20],[30, 40, 50],[60, 70, 80, 90]]
print(f'matriz original: {matriz}')
print(f'reglon 0 ,  columna 1 : {matriz[0][1]}')


#252  - ORDENAMIENTO

lista_listas  = [[10, 20,45, 67, 89],[30, 40, 50, 23, 56, 78],[60, 70, 80, 90, 45, 89, 31, 52, 56]]
lista_listas.sort(key=len)                                                                                      #ordena por el largo de la lista
print(f'orden por cantidad de elementos: {lista_listas}')

#ORDENAMIENTO BUILT IN

nombres1 = ['juan carlos','karla','pedro','esperanza']
nombres1 = sorted(nombres1)
print(nombres1)

nombres1 = ['juan carlos','karla','pedro','esperanza']
nombres1 = sorted(nombres1, reverse=True)
print(nombres1)

nombres1 = ['juan carlos','karla','pedro','esperanza']
nombres1 = sorted(nombres1, key=len)
print(nombres1)

#built in reversed
nombres1 = reversed(nombres1)
print(list(nombres1))