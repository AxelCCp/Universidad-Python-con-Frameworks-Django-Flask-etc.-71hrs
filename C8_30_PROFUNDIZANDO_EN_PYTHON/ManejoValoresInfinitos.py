#212  MANEJANDO INFINITOS

import math
from decimal import Decimal

print('-----------212-------------')

infinito_positivo = float("inf")                                                                        #INF REPRESENTA EL VALOR DE INFINITO.
print(f'infinito_positivo : {infinito_positivo}')
print(f'es positivo?: {math.isinf(infinito_positivo)}')                                                 #SE PREGUNTA SI UN VALOR ES INFINITO

infinito_negativo = float("-inf")
print(f'infinito_negativo : {infinito_negativo}')
print(f'es negativo?: {math.isinf(infinito_negativo)}')  


print('-----------213-------------')

#213    CREA INFINITOS CON MATH
infinito_positivo = math.inf
print(f'infinito_positivo : {infinito_positivo}')
print(f'es positivo?: {math.isinf(infinito_positivo)}') 

infinito_negativo = -math.inf
print(f'infinito_negativo : {infinito_negativo}')
print(f'es negativo?: {math.isinf(infinito_negativo)}')  


#CREA INFINITOS CON DECIMAL
print("----------")
infinito_positivo = Decimal('Infinity')
print(f'infinito_positivo : {infinito_positivo}')
print(f'es positivo?: {math.isinf(infinito_positivo)}') 

infinito_negativo = Decimal('-Infinity')
print(f'infinito_negativo : {infinito_negativo}')
print(f'es negativo?: {math.isinf(infinito_negativo)}')  







