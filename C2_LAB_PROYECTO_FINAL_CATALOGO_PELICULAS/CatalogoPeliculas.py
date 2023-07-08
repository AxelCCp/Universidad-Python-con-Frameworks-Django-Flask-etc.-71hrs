class CatalogoPeliculas:

    def __init__(self, rutaArchivo):
        self.__rutaArchivo = rutaArchivo
    
    @property
    def lista(self):
        return self.__lista
    
    def agregarPelicula(self, pelicula):
        self.__lista.append(pelicula) 


    def eliminarPelicula(self, pelicula):
        self.__lista.remove(pelicula)

    
    
    

    
    
