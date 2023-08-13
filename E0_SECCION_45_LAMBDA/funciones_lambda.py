#278
#funciones lambda : son funciones anonimas y pequeñas. una linea de código

def sumar(a,b):
    return a+b

# no es posible asignar una funcion a una variable
# mi_funcion = def sumar2(a,b) : return a + b


# con una lambda, la funcion es anonima y una sola línea de código. no se necesita parentesis para los parámetros. la palabra return no se necesita usar,  pero se debe usar una expresion válida.
mi_funcion_lambda = lambda a, b : a + b                             #los parametros son opcionales   "lambda (a, b) : a + b"    //  la expresion a regresar es obligatioria ": a + b"   


resultado = mi_funcion_lambda(4,6)


print(f'resultado de sumar con funcion lambda: {resultado}')


#279
#funcion lambda que no recibe argumentos , pero si se debe regresar una expresión valida

mi_funcion_lambda = lambda : 'funcion sin argumentos'
print(f'llamar funcion lambda sin argumntos: {mi_funcion_lambda()}')


#función lambda con parámetros por default
mi_funcion_lambda = lambda a=2, b=3 : a + b
print(f'llamar a función lambda con parámetros por default: {mi_funcion_lambda()}')

print(f'llamar a función lambda con parámetros por default: {mi_funcion_lambda(7,9)}')

#lambda y valores variables y argumentos variables en una tupla de valores
#argumentos variables con *args y *kwargs
# *args --> tupla
# *kwargs --> diccionario

mi_funcion_lambda = lambda *args, **kwargs : len(args) +  len(kwargs)
print(f'resultado argumentos variables: {mi_funcion_lambda(1,2,3, a=4, b=5)}')

#lambda con argumentos, argumentos variables y valores por default
mi_funcion_lambda = lambda a, b, c=3, *args, **kwargs : a + b + c + len(args) + len(kwargs)
print(f'resultado función lambda: {mi_funcion_lambda(1,2,4, 5,6,7, e=5, f=7)}')
