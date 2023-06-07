lista = [1,2,3,4,5,6,7,8,9,10]
for num in lista:
    print(num)

print('-----')

print(lista[:])

print('-----')

for num in lista:
    if num % 3 ==0:
        print(num)

print('-----')

print(lista[2:6])

print('-----')

c = 0
while c < len(lista):
    if c >= 2:
        print(lista[c])   
    c += 1


print('-----')

c = 0
while c < len(lista):
    if c >= 2:
        print(lista[c])   
    c += 2

print('-----')




print('--------------CODIGO PROFESOR--------------------')

print('Rango de 0 a 10 con numeros divisibles entre 3')
for i in range(11):
    if i % 3 == 0:
        print(i)

print('Crear un rango de 2 a 6 e imprimir')
rango = range(2, 7)
for i in rango:
    print(i)

print('Rango con valores de inicio = 3, fin = 10, incremento de 2 en 2')
for i in range(3, 11, 2):
    print(i)