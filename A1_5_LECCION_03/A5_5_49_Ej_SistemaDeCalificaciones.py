calificacion : int = None

calificacion = int(input('Proporciona un valor entre 0 y 10: '))
letra = None

if   9 <= calificacion <= 10:
    letra = 'A'
elif 8 <= calificacion < 9:
    letra = 'B'
elif 7 <= calificacion < 8:
    letra = 'C'
elif 6 <= calificacion < 7:
    letra = 'D'
elif 0 <= calificacion < 6:
    letra = 'F'
else:
    letra = 'Valor incorrecto. Proporciona un valor entre 0 y 10'

print(f'La letra para las calificacion {calificacion} es: {letra}')

