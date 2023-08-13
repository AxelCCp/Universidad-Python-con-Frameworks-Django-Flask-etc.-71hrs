#276
#las funciones son ciudadanas de primera clase


#definimos funcion

def sumar(a,b):
    return a+b

#1 - asignar funcion a una variable
mi_funcion = sumar

# - verificar el tipo de la variable
print(type(mi_funcion))                                                     #es un obj de la clase function

# - llamamos la funcion a traves de la variable
resultado = mi_funcion(5,8)

print(f'Resultado: {resultado}')


#277 ---------------------------------

#2 - funcion como argumento
def operacion(a, b, sumar_arg):
    print(f'Resultado sumar: {sumar_arg(a,b)}')

operacion(4,5, sumar)



#3 - podemos retornar una funcion desde otras funciones
def retornar_funcion():
    #retornamos una funcion
    return sumar

mi_funcion_retornada = retornar_funcion() 
print(f'Resultado de la funcion retornada: {mi_funcion_retornada(5,7)}')