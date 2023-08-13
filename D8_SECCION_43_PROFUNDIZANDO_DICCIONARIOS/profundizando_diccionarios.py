#269
#los dic guardan un orden a diferencia de un set

diccionario = {'Nombre' : 'Juan', 'Apellido':'Perez', 'Edad':28}
print(diccionario)

#los diccionarios son mutables, pero las llaves deben ser inmutables.

#no se puede usar una lista como llave ya que las listas son mutables
#diccionario = {[1,2] : 'valor1'}

#si se puede usar una tupla como llave ya que la tupla es inmutable
#diccionario = {(1,2) : 'valor1'}

#se agrega una llave si es que no se encuentra el elemento dentro del diccionario
diccionario['departamento'] = 'sistemas'
print(diccionario)

#no hay valores duplicados en las llaves de un diccionario. si la llave ya existe, se reemplaza
diccionario['Nombre'] = 'juan carlos'
print(diccionario)

#recuperar un valor indicandouna llave
print(diccionario['Nombre'])


#si no encuentra la llave, lanza una excepcion
#print(diccionario['nombre'])

#el metodo get recupera el valor de la llave, y si no la encuentra,  no lanza un error
#además podemos regresar un valor en caso de que no exista la llave
print(diccionario.get('Nombre', 'No se encontró la llave')) 
print(diccionario.get('nombre', 'No se encontró la llave')) 

#setDefault sí modifica el diccionario en caso de que no encuentre la llave. además agrega un valor por default
nombre  = diccionario.setdefault('Nombre', 'valor por default')
print(nombre)
print(diccionario)

nombre  = diccionario.setdefault('nombres', 'valor por default')
print(nombre)
print(diccionario)

#imprimir con pprint

from pprint import pprint as pp
help(pp)

pp(diccionario)

#ordena con pprint segun se fueron agregando los elementos
pp(diccionario, sort_dicts=False)