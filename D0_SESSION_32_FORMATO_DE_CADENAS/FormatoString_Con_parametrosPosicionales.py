#223

nombre = 'juan'
edad = 28
mensaje_con_formato = 'mi nombre es %s y tengo %d años'%(nombre, edad) 
print(mensaje_con_formato)  

print('..............')

persona = ('Karla', 'gomez', 5000.0)
mensaje_con_formato = 'Hola %s %s. Tu sueldo es %.2f'%persona
print(mensaje_con_formato)

print('..............')

mensaje_con_formato = 'Hola %s %s. Tu sueldo es %.2f'
print(mensaje_con_formato%persona)