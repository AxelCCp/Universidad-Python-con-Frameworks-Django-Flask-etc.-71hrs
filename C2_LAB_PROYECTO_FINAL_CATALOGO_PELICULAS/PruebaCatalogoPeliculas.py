from Pelicula import Pelicula
from CatalogoPeliculas import CatalogoPeliculas

listaPeliculas = []

num = int(input('''Elije una de las siguientes opciones: 
                    1) Agregar película.
                    2) Listar películas.
                    3) Eliminar película.
                    4) Salir
                : '''))

contador = 0

while num != 4:

    if contador > 0:
        num = int(input('''Elije una de las siguientes opciones: 
                            1) Agregar película.
                            2) Listar películas.
                            3) Eliminar película.
                            4) Salir
                        : '''))
    
    contador += 1 

    if num==1:
        nombre  = input('''Agregar película:
            Nombre:
            ''')
        pelicula1 = Pelicula(nombre)
        CatalogoPeliculas.agregarPelicula(pelicula1)
        listaPeliculas = CatalogoPeliculas.listarPeliculas()
        print(listaPeliculas)

    elif num==2:

        listaPeliculas = CatalogoPeliculas.listarPeliculas()
        print(listaPeliculas)

    elif num==3:

        nombre = input('Eliminar película: \nIngresa el nombre de la película: ')
        CatalogoPeliculas.eliminarPelicula(nombre)
        print(CatalogoPeliculas.listarPeliculas())
        
    elif num==4:
        
        break

    else:
        print('Elige una opción válida!')

   