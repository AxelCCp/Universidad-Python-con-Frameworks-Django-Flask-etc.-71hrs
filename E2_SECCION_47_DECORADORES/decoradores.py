#282
#decorador : es una funcion q recibe una funcion y regresa otra. y se usa para extender funcionalidad.

#1. funcion decorador (a)
#2. funcion a decorar (b)
#3. funcion decorada (c)


def funcion_decorador_a(funcion_a_decorar_b):
    
    def funcion_decorada_c():
        print('antes de ejecutar la funcion')
        funcion_a_decorar_b()
        print('despues de ejecutar la funcion')
    return funcion_decorada_c


@funcion_decorador_a
def mostrar_mensaje():                                          # b
    print('hola desde funcion mostrar mensaje')

mostrar_mensaje()


def imprimir():
    print('hola desde funcion imprimir')


imprimir()