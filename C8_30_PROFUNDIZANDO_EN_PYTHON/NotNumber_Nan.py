#214

import math
from decimal import Decimal

a = float('NaN')
print(f'a : {a}')
print(f'a - Es NaN (not a number)? : {math.isnan(a)}')

b = float('2.0')
print(f'b: {b}')
print(f'b - Es NaN (not a number)? : {math.isnan(b)}')

print('----------')

a = Decimal('NaN')
print(f'a : {a}')
print(f'Es Nan (not a number)?: {math.isnan(a)}')

