#284
#generador : es una funcion especial que retorna una secuencia de valores. suspende la ejecucion de la funcion yield que signigica producir. no se usa el return.

def generador():
    yield 1
    print('se reanuda la ejecucion')
    yield 2
    print('se reanuda la ejecucion')
    yield 3

#consumimos el generador, pero a demanda
gen = generador()

#con cada llamada consumimos un valor

print(next(gen))        #1


print(next(gen))        #2


print(next(gen))        #3


#si se piden mas valores de los q genera el generador, va a dar un error de stop iteration
#print(next(gen))        #4


#------------------------------------


#generador con bucle for

for valor in generador():
    print(f'Numero generado: {valor}')
