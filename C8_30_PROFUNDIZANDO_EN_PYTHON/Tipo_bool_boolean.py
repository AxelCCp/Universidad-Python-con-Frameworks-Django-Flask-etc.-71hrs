#215
#PASAR UN NUMERO A BO0LEAN

print('-----------numeros-----------')

valor = 0
resultado = bool(valor)                             
print(f'Valor {valor}, resultado: {resultado}')


valor = 5
resultado = bool(valor)                             
print(f'Valor {valor}, resultado: {resultado}')


valor = 0.0
resultado = bool(valor)                             
print(f'Valor {valor}, resultado: {resultado}')


valor = 15.0
resultado = bool(valor)                             
print(f'Valor {valor}, resultado: {resultado}')


# PASAR STRING A BOOLEAN
print('-----------string-----------')

valor = ''
resultado = bool(valor)                             
print(f'Valor {valor}, resultado: {resultado}')

valor = 'jkahsdjhaksdjhasjkdahd'
resultado = bool(valor)                             
print(f'Valor {valor}, resultado: {resultado}')


# PASAR COLECCIONES A BOOLEAN
print('----------colecciones------------')

valor = []
resultado = bool(valor)                             
print(f'Valor {valor}, resultado: {resultado}')

valor = ['AHSJ', 'AKSJHD', 78]
resultado = bool(valor)                             
print(f'Valor {valor}, resultado: {resultado}')


# PASAR TUPLAS A BOOLEAN
print('-----------tuplas-----------')

valor = ()
resultado = bool(valor)                             
print(f'Valor {valor}, resultado: {resultado}')

valor = ('AHSJ', 'AKSJHD', 78)
resultado = bool(valor)                             
print(f'Valor {valor}, resultado: {resultado}')


# PASAR DICIONARIO A BOOLEAN
print('-----------tuplas-----------')

valor = {}
resultado = bool(valor)                             
print(f'Valor {valor}, resultado: {resultado}')

valor = {'1':'AHSJ', '2':'AKSJHD', '3':78}
resultado = bool(valor)                             
print(f'Valor {valor}, resultado: {resultado}')

print('-----bool-----')

if bool(17):
    print('regreso verdadero')
else:
    print('regreso false')

if bool(0):
    print('regreso verdadero')
else:
    print('regreso false')

if bool(''):
    print('regreso verdadero')
else:
    print('regreso false')

if '':
    print('regreso verdadero')
else:
    print('regreso false')

if bool(['234sdf','qweqqwe',4242]):
    print('regreso verdadero')
else:
    print('regreso false')

if bool([]):
    print('regreso verdadero')
else:
    print('regreso false')







