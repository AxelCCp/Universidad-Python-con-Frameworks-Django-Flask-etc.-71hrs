#281

#funcion principal

def operacion(a,b):
    #1.se define lambda interna o anidada y la retornamos
    return lambda : a + b


mi_funcion_closure = operacion(5,2)
print(f'Resultado de la funcion closure: {mi_funcion_closure()}')


print(f'resultado funcion closure al vuelo: {operacion(2,3)()}')   