numero = int(input('Proporciona un valor entre uno y tres: '))

numeroTexto = ''

if numero == 1:
    numeroTexto = 'Numero 1'
elif numero == 2:
    numeroTexto = 'Numero 2'
elif numero == 3:
    numeroTexto = 'Numero 3'
else:
    numeroTexto = 'Fuera de rango'

print(f'Numero proporcionado: {numero} : {numeroTexto}')
