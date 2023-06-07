print('-------------------------CLASE 75---------------------------')

def listarNombres(*nombres):                                                      # *nombres : RECIBE UNA CANTIDAD VARIABLE DE PARAMETROS DENTRO DEL MÉTODO SE GESTIONAN COMO UNA TUPLA.
    for nombre in nombres:
        print(nombre)

listarNombres('Juan', 'Karla', 'Erika', 'Ernesto', 'Etc')
listarNombres('Laura', 'Carlos')