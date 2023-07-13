class CatalogoPeliculas:

    rutaArchivo = ""
    listaPeliculas = []

    def __init__(self, rutaArchivo):
        CatalogoPeliculas.rutaArchivo = rutaArchivo
        #self.__pelicula = pelicula

    @staticmethod
    def listarPeliculas():
        peliculas_str = ''
        for p in CatalogoPeliculas.listaPeliculas:
            peliculas_str += ' ' + p.__str__()
        return f'''
        Lista de películas: {peliculas_str}
        '''
    
    @staticmethod
    def agregarPelicula(pelicula):
        CatalogoPeliculas.listaPeliculas.append(pelicula) 

    @staticmethod
    def eliminarPelicula(pelicula):
        for p in CatalogoPeliculas.listaPeliculas:
            if p.nombre == pelicula:
                CatalogoPeliculas.listaPeliculas.remove(p)

    
    
    

    
    
