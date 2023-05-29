#MI CODIGO

mes = int(input('Ingresa el mes del año actual (valor entre 1 y 12): '))
# marzo - mayo
if 3 <= mes <= 5:
    print('Estamos en otoño')
# julio -agosto
elif 6 <= mes <= 8:
    print('Estamos en invierno')
# septiembre - noviembre
elif 9 <= mes <= 11:
    print('Estamos en primavera')
#diciembre - febrero
elif mes == 12 or mes <= 2:
    print('Estamos en verano')
else:
    print('ingresa un valor valido')

#CODIGO PROFESOR

mes = int(input('Ingresa el mes del año(1-12): '))
estacion = None
if mes == 1 or mes == 2 or mes == 12:
    estacion = 'verano'
elif mes == 3 or mes == 4 or mes == 5:
    estacion = 'otoño'
elif mes == 6 or mes == 7 or mes == 8:
    estacion = 'invierno'
elif mes == 9 or mes == 10 or mes == 11:
    estacion = 'primavera'
else:
    estacion = 'ingresa una valor valido entre 1 y 12'

print(f'Para el mes {mes} la estacion del año es: {estacion}')
