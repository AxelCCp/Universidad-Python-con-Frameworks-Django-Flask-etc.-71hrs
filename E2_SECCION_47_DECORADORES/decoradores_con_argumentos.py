#282
#decorador : es una funcion q recibe una funcion y regresa otra. y se usa para extender funcionalidad.

#1. funcion decorador (a)
#2. funcion a decorar (b)
#3. funcion decorada (c)


def funcion_decorador_a(funcion_a_decorar_b):
    
    def funcion_decorada_c(*args, **kwargs):

        print('antes de ejecutar la funcion')
        
        resultado = funcion_a_decorar_b(*args, **kwargs)

        print('despues de ejecutar la funcion')
        
        return resultado
    
    return funcion_decorada_c


@funcion_decorador_a
def sumar(a,b):
    return a+b

resultado = sumar(5,6)
print(f'resultado de la suma: {resultado}')


