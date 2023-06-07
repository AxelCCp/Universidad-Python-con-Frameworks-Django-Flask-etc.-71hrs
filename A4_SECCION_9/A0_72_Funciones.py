print('-------------------------CLASE 71---------------------------')

def miFuncion():
    print('Saludos desde la funcion!') 

miFuncion()

print('-------------------------CLASE 72---------------------------')

def miFuncion2(nombre, apellido):
    print(f'Saludos {nombre} {apellido} desde la funcion!') 

miFuncion2('juan', 'perez')


print('-------------------------CLASE 73---------------------------')

def sumar(a,b):
    return a + b

resultado = sumar(34,56) 
print(resultado)

print(f'Resultado de sumar: {sumar(23,45)}')

print('-------------------------CLASE 74---------------------------')

#VALORES POR DEFAULT EN LOS PARAMETROS DEL METODO

def sumar2(a = 0, b = 0):
    return a + b

print(f'Resultado de sumar: {sumar2()}')
print(f'Resultado de sumar: {sumar2(23,45)}')

#SE AGREGA UNA PISTA ACERCA DEL TIPO DE DATO Q VA A REGRESAR LA FUNCION

def sumar3(a = 0, b = 0) -> int:
    return a + b

print(f'Resultado de sumar: {sumar3()}')
print(f'Resultado de sumar: {sumar3(34,12)}')
