print('---------------------CLASE 56-----------------------')
cadena = 'Hola'
for letra in cadena:
    print(letra)
else:
    print('Fin ciclo for')


print('---------------------CLASE 57---------BREAK--------------')
for letra  in 'Holanda':
    if letra == 'a':
        print(f'Letra encontrada: {letra}')
else:
    print('Fin ciclo for')

print('-------')

for letra  in 'Holanda':
    if letra == 'a':
        print(f'Letra encontrada: {letra}')
        break
else:
    print('Fin ciclo for')


print('---------------------CLASE 58-----------RANGE------------')

for i in range(6):
    print(f'Valor: {i}')

print('----valores pares---')

for i in range(6):
    if i%2 == 0:
        print(f'Valor: {i}')

print('----valores pares---continue----')

for i in range(6):
    if i%2 != 0:
        continue
    print(f'Valor: {i}')
