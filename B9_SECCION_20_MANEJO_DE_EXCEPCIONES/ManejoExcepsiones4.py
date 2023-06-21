resultado = None
a = '10'
b = 0

try:
    resultado = a/b
except ZeroDivisionError as zde:
    print(f'ZeroDivisionError - Ocurrió un error: {zde}, ------> {type(zde)}')
except TypeError as te:
    print(f'TypeError - Ocurrió un errror: {te} ------> {type(te)}')
except Exception as e:
    print(f'Exception - Ocurrió un errror: {e} ------> {type(e)}')


print(f'Resultado: {resultado}')
print('continuamos ... ')