print('Proporcione los siguientes datos del libro: ')
nombreLibro = input('Proporciona el nombre: ')
idLibro = int(input('Proporciona el id del libro: '))
precioLibro =  float(input('Proporciona el precio (formato 000.00): '))
envio = input('Indica si el envio es gratuito (True/False): ')                      #NO SE PUEDE USAR BOOL() PARA EL PARSE, YA Q BOOL() EVALÚA SI LA CADENA VIENE VACIA O NO

if envio == 'True':
    envio = True
elif envio == 'False':
    envio = False
else:
    envio = 'Valor incorrecto, debe escribir (True/False)'

print(f'''
    Nombre: {nombreLibro}
    Id: {idLibro}
    Precio: {precioLibro}
    Envio: {envio}
''')


"""
print(f'Nombre: {nombreLibro}')
print(f'Id: {idLibro}')
print(f'Precio: {precioLibro}')
print(f'Envio: {envio}')
"""
