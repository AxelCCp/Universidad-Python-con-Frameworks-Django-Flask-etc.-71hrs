#CREAR UNA LISTA Q SOLO INCLUYA LOS NUMEROS MENORES A 5 DE LA TUPLA

tupla = (13, 1, 8, 3, 2, 5, 8)

nums = []

for num in tupla:   
    if(num < 5):
        nums.append(num)
print(nums)

tuplaJr = tuple(nums)

print(tuplaJr)
