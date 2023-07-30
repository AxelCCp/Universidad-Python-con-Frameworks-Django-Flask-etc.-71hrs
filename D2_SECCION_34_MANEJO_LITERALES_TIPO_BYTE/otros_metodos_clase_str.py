#237

# Leer contenido online
import urllib
from urllib.request import urlopen

# Debido a cambios en la libreria se deben hacer los siguientes cambios:
peticion = urllib.request.Request(
    'http://globalmentoring.com.mx/recursos/GlobalMentoring.txt',
    data=None,
    headers={
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'
    }
)
with urlopen(peticion) as mensaje:
    contenido = mensaje.read().decode('utf-8')

# Contar ocurrencias de una cadena
print('No. veces Universidad: ', contenido.count('Universidad'))

# upper convierte a mayúsculas un str
print(contenido.upper())
print(contenido)

# lower convierte a minúsculas un str
print(contenido.lower())

# buscamos la cadena python en el contenido
print('Existe python?: ','python'.lower() in contenido.lower())
print('Existe Python?: ','Python'.upper() in contenido.upper())

#PREGUNTA SI INICIA O TERMINA CON
print('inicia con: ', contenido.startswith('En GlobalMentoring'))
print('termina con: ', contenido.endswith('GlobalMentoring.com.mx'))

#PREGUNTA SI TIENE MINUSCULAS O MAYUSCULAS
mensaje = 'Hola Mundo'
print(mensaje.lower().islower())
print(mensaje.upper().isupper())

print('--------------239--------------')

#ALINEAR CADENAS
titulo = 'Sitio web de globalmentoring.com.mx'
print(len(titulo))
print(titulo.center(50,'*'))
print(len(titulo.center(50, '*')))
print(titulo.center(len(titulo)+10, '-'))


print('--------------240--------------')
print(titulo.ljust(50, '*'))
print(titulo.ljust(len(titulo)+10, '-'))

print(titulo.rjust(50, '*'))
print(titulo.rjust(len(titulo)+10, '-'))

print('--------------241--------------')
#reemplaza espacios por guiones
print(contenido.replace(' ', '-'))

#eliminar caracteres al inicio y final de la cadena
titulo = ' *** globalmentoring.com.mx *** '
print('cadena original: ', titulo, len(titulo))
titulo = titulo.strip()
print('cadena modificada: ', titulo, len(titulo))

titulo = '***globalmentoring.com.mx***'.strip('*')
print('cadena modificada: ', titulo)

#quita caracteres isq
titulo = '***globalmentoring.com.mx***'.lstrip('*')
print('cadena modificada: ', titulo)


#quita caracteres der
titulo = '***globalmentoring.com.mx***'.rstrip('*')
print('cadena modificada: ', titulo)


titulo = ' *** globalmentoring.com.mx *** '.strip().strip('*').strip()
print('cadena modificada: ', titulo)




