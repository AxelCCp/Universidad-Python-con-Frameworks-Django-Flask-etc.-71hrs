#285
#generador de numeros 1 al 5

def generador_numeros():
    for numero in range(1,6):
        yield numero
        print('se reanuda la ejecucion de la funcion')


#usamos el generador
generador = generador_numeros()

print(f'obj generador : {generador}')
print(f'tipo generador : {type(generador)}')


#consumimos el generador
for valor in generador:
    print(f'numero producido: {valor}')


#consumir a demanda
generador = generador_numeros()

try:
    print(next(generador))
    print(next(generador))
    print(next(generador))
    print(next(generador))
    print(next(generador))
    print(next(generador))
except StopIteration as e:
    print(f'Error al consumir el generador --> {e}')



#-----------------------------------------------


#consumir generador con while

generador = generador_numeros()

while True:
    try:
        valor = next(generador)
        print(f'Impresion valor generado {valor}')
    except StopIteration as e:
        print('Se termino de iterar el generador')
        break


