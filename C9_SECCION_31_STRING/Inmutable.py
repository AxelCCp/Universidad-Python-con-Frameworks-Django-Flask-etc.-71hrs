help(str.capitalize)
mensaje1 = 'hola mundo'
mensaje2 = mensaje1.capitalize()                #ESTO DEVUELVE UNA NUEVA CADENA ... AGREGA UNA MAYUSCULA AL INICIO.

print(f'mensaje1 {mensaje1}, id: {id(mensaje1)}, direccion memoria obj: {hex(id(mensaje1))}')           # hex : hexagecimal
print(f'mensaje2 {mensaje2}, id: {id(mensaje2)}, direccion memoria obj: {hex(id(mensaje2))}')