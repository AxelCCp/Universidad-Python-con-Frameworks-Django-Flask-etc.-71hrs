#ENTRE LOS 30'S Y 40'S AÑOS

edad = int(input('ingresa tu edad: '))

veintes = edad >= 20 and edad < 30
treintas = edad >= 30 and edad < 40

if veintes or treintas:
    print(f'tu edad {edad} esta entre los 20\'s y 39\'s')
else:
    print(f"tu edad {edad} esta fuera de los 20's y 39's")

#CLASE 37

if 20 <= edad < 30 or 30 <= edad < 40:
    print(f'tu edad {edad} esta entre los 20\'s y 39\'s')
else:
    print(f"tu edad {edad} esta fuera de los 20's y 39's")