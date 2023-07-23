#211
#PROFUNDIZANDO EN EL TIPO FLOAT

a = 3.0
print(f'a = {a}')
print(f'a = {a:.2f}')

a = float(10)
print(f'a = {a:.2f}')

a = float('10')
print(f'a = {a:.2f}')


#NOTACION EXPONENCIAL, VALORES POSITIVOS O NEGATIVOS
a = 3e5
print(f'a = {a}')

a = 3e-5
print(f'a = {a}')
print(f'a = {a:.5f}')

#CUALQUIER CALCULO Q TENGA UN FLOAT, SE PROMUEVE A FLOAT
a = 4.0 + 5
print(a)
print(type(a))
