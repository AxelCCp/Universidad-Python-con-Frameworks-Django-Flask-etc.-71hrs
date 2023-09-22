#286

#EXPRESION GENERADORA : ES UN GENERADOR ANONIMO

multiplicacion = (valor * valor for valor in range(4))
print(type(multiplicacion)) 
print(next(multiplicacion)) 
print(next(multiplicacion)) 
print(next(multiplicacion)) 
print(next(multiplicacion)) 

#tambn se puede pasar una expresion generadora a una funcion (sin parentesis)

suma = sum(valor * valor for valor in range(4))
print(f'Suma: {suma}')


#287
#tmbn se puede usar una lista o cualquier otro iterador

lista = ['juan', 'pérez']
generador = (valor for valor in lista)
print(next(generador))
print(next(generador))

#crear un string a partir de un generador creado a partir de una lista
lista = ['karla', 'gomez']
contador = 0;

def incrementar():
    global contador
    contador += 1
    return contador

#la primera es para el yield y la segunda es para el for, entre parentesis
generador = (f'{incrementar()}. {nombre}' for nombre in lista)
lista = list(generador)
print(lista)

cadena = ', '.join(lista)
print(f'cadena: {cadena}')

