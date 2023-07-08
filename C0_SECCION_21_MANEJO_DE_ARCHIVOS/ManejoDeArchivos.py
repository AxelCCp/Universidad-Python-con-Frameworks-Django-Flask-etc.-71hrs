
print('-----------------------156. y 157.-------------------------')
try:
    #C:\\Users\\Fanta\\Downloads\\prueba.txt
    archivo = open('prueba.txt', 'w', encoding='utf8')                       #CREA EL ARCHIVO. / LA W ES DE WRITE. / EL ENCODIG PARA Q SOPORTE LOS ACENTOS.
    archivo.write('Agregamos información al archivo')       #ESCRIBIENDO EN EL ARCHIVO.
    archivo.write('\nadios!')
except Exception as e:
    print(e)
finally:
    archivo.close()                                         #UAN VEZ CERRADO EL ARCHIVO, YA NO SE PUEDE SEGUIR TRABAJANDO CON EL ARCHIVO.        
    print('fin del archivo')
