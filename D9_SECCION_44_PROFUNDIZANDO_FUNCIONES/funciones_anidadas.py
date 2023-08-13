#271
#anida una funcion dentro de otra

def calculadora1(a,b):
    #funcion anidada
    def sumar(a,b):
        return a + b
    
    def restar(a,b):
        return a - b
    
    #llama a la funcion
    print(f'Suma: {sumar(a,b)}')

    print(f'Resta: {restar(a,b)}')

calculadora1(10, 50)


print('---------------------------------')


def calculadora2(a, b, operacion = 'sumar'):
    
    
    def sumar(a,b):
        return a + b
    
    def restar(a,b):
        return a - b
    
    if operacion == 'sumar':
        print(f'Suma: {sumar(a,b)}')
    elif operacion == 'restar':
        print(f'Resta: {restar(a,b)}')
    else:
        print('ingresa una opracion valida')


calculadora2(10, 50, 'sumar')

calculadora2(10, 50, 'restar')

calculadora2(10, 50, 'xxx')
