help(str.join)


tupla_str = ('Hola', 'Mundo', 'Universidad', 'Python')

mensaje = ' '.join(tupla_str)

print(f'mensaje: {mensaje}')

print('--------------------------------------------------------')

lista_cursos = ['java', 'python', 'angular', 'spring']

mensaje = ', '.join(lista_cursos)

print(f'mensaje: {mensaje}')

print('--------------------------------------------------------')

cadena = 'HolaMundo'
mensaje = '.'.join(cadena)
print(f'mensaje: {mensaje}')

print('--------------------------------------------------------')

dic = {'nombre' : 'juan', 'apellido' : 'perez', 'edad' : '18'}
llaves = '-'.join(dic.keys())
valores = '-'.join(dic.values())
print(f'llaves: {llaves}, type: {type(llaves)}')
print(f'valores: {valores}, type: {type(valores)}')

