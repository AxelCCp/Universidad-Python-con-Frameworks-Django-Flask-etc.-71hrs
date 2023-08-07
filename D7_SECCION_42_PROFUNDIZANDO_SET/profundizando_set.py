#264
#set : coleccion de elementos unicos  y es mutable.
#los elementos de un set deben ser inmutables.

#conjunto  = {[1,2], [3,4]}
conjunto1 = {'-juan', True, 18.00}
print(conjunto1)


#como declarar un set vacio
conjunto = set()
print(conjunto)
print(type(conjunto))


#mutable
conjunto.add('juan')
print(conjunto)


#contiene valores unicos
conjunto.add('juan')
print(conjunto)


#crear set a partir de un iterable
conjunto = set([4,5,6,7,8,4])
print(conjunto)


#CLASE 265

#podemos agregar más elementos o incluso otro set

conjunto2 = {100,200, 300, 400, 500}
conjunto.update(conjunto2)
print(conjunto)


#copiar un set (copia poco profunda, solo copia referencias)

conjunto_copia =conjunto.copy()
print(conjunto_copia)


#verificar igualdad
print(f'es igual en contenido: {conjunto == conjunto_copia}')
print(f'es la misma referencia: {conjunto is conjunto_copia}')

