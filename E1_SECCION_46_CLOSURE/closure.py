#280
#funcion closure, una funcion q encapsula a otra funcion.
#la funcion anidada puede acceder a las variables locales definidas en la funcion principal o externa.

#funcion principal
def operacion(a,b):
    #funcion interna
    def sumar():
        return  a + b
    
    #retornar la funcion
    return sumar

mi_funcion_closure = operacion(5,2)
print(f'Resultado de la funcion closure: {mi_funcion_closure()}')



#llamar la funcion regresada al vuelo
print(f'resultado funcion closure al vuelo: {operacion(2,3)()}')                       #se llama a  operacion(a,b) y luego a sumar con "()"