nombre = 'juan'
edad = 28
sueldo = 3000
mensaje_con_formato = 'mi nombre {} edad {} sueldo {:.2f}'.format(nombre, edad, sueldo)
print(mensaje_con_formato)

print('...........')

mensaje = 'Nombre {0} edad {1} sueldo {2:.2f}'.format(nombre, edad, sueldo)
print(mensaje)


print('...........')

mensaje = 'Nombre {2} edad {0} sueldo {1:.2f}'.format(nombre, edad, sueldo)
print(mensaje)

print('...........')

mensaje = 'Nombre {n} edad {e} sueldo {s:.2f}'.format(n=nombre, e=edad, s=sueldo)
print(mensaje)


print('...........')


diccionario = {'nombre':'ivan', 'edad':35, 'sueldo':8000.00}
mensaje = 'nombre: {dic[nombre]}'.format(dic=diccionario)
print(mensaje)


mensaje = 'nombre: {dic[nombre]} edad: {dic[edad]} sueldo: {dic[sueldo]:.2f}'.format(dic=diccionario)
print(mensaje)