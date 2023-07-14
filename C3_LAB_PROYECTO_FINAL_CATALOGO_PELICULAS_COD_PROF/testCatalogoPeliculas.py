from dominio.Pelicula import Pelicula
from servicio.catalogoPeliculas import CatalogoPeliculas as cp

opcion = None

while opcion != 4:
    try:
        print('Opciones:')
        print('1. agregar pelicula.')
        print('2. listar peliculas.')
        print('3. eliminar catalogo peliculas.')
        print('4. salir.')
        opcion = int(input('escribe tu opcion (1-4): '))

        if opcion==1:
            nombrePelicula = input('Proporciona el nombre de la pelicula: ')
            pelicula = Pelicula(nombrePelicula)
            cp.agregarPelicula(pelicula)
        elif opcion==2:
            cp.listarPeliculas()
        elif opcion==3:
            cp.eliminarPeliculas()
    except Exception as e:
        print(f'ocurrió un error {e}')
        option = None
else:

    print('salimos del programa.')