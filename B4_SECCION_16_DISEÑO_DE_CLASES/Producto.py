class Producto:

    contador_productos = 0

    def __init__(self, nombre, precio) -> None:
        Producto.contador_productos += 1
        self._id_producto = Producto.contador_productos
        self._nombre = nombre
        self._precio = precio

    def __str__(self):
        return f'Id producto: {self._id_producto}, nombre: {self._nombre}, precio: {self._precio}'
    
    @property
    def id_producto(self):
        return self._id_producto 
    
    @property
    def nombre(self):
        return self._nombre
    
    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre

    @property
    def precio(self):
        return self._precio 

    @precio.setter
    def precio(self, precio):
        self._precio = precio

if __name__ == '__main__':
    producto1 = Producto('Camisa', 100.00)
    print(producto1)
    producto2 = Producto('Pantalon', 200.00)
    print(producto2)

