
print('-------------158. Lectura de Archivos en Python---------------')

#C:\\Users\\Fanta\\Downloads\\prueba.txt
archivo = open('prueba.txt', 'r', encoding='utf8')     #r de read.

#print(archivo.read())


# leer algunos caracteres
#print(archivo.read(5))
#print(archivo.read(4))


# leer lineas completas
#print(archivo.readline())
#print(archivo.readline())

#iterar las lineas
#for linea in archivo:
#    print(linea)

#metodo q lee todo el archivo
#print(archivo.readlines())

#acceder solo a una línea del archivo
#print(archivo.readlines()[0])                     #linea 1

print('Vaciar el contenido del archivo existente en un nuevo archivo.')

# a - anexar informacion.

archivo2 = open('copia.txt', 'a', encoding='utf8')          #SI SE USA W, NO VA A ANEXAR, VA A REESCRIBIR INFORMACION. SI EL ARCHIVO YA TIENE CONTENIDO, LO VA A REEMPLAZAR.
archivo2.write(archivo.read())

archivo.close()
archivo2.close()

print('Se ha terminado el proceso de leer y copiar el archivo.')