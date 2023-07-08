# CON ESTA SINTAXIS, DE MANERA AUTOMATICA ABRE Y CIERRA EL ARCHIVO 

'''
EL WITH MANDA A LLAMAR A 2 METODOS,  EL __enter__ y el __exit__, para abrir y cerrar.
'''

'''
with open('prueba.txt', 'r', encoding='utf8') as archivo:
    print(archivo.read())
'''

#------------------------

#ESTO SE PUEDE PERSONALIZAR CON LA CLASE MAJEJO ARCHIVOS
 
from ManejoArchivos import ManejoArchivos

with ManejoArchivos('prueba.txt') as archivo:
    print(archivo.read())
