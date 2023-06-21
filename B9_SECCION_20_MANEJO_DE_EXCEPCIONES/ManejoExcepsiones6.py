
from NumerosIdenticosException import NumerosIdenticosException

resultado = None

try:
    a = int(input('primer número: '))
    b = int(input('segundo número: '))

    if a == b:
        #raise SE USA PARA LANZAR CUALQUIE TIPO DE EXCEPTION
        raise NumerosIdenticosException('números idénticos')                                    #AQUI ARROJA UN ERROR Y LUEGO LA CLASE EXCEPTION ES LA QUE LO MANEJA, YA Q NumerosIdenticosException HEREDA DE EXCEPTION. 
        #raise ValueError("error de valor")
        
    resultado = a/b
except ZeroDivisionError as zde:
    print(f'ZeroDivisionError - Ocurrió un error: {zde}, ------> {type(zde)}')
except TypeError as te:
    print(f'TypeError - Ocurrió un error: {te} ------> {type(te)}')
except Exception as e:
    print(f'Exception - Ocurrió un error: {e} ------> {type(e)}')
else:
    print('No se arrojó ninguna excepción')
finally:
    print('Ejecución del bloque finally')

print(f'Resultado: {resultado}')
print('continuamos ... ')