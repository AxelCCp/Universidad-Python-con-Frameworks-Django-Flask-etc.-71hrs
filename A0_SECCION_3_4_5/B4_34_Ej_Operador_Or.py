#MI SOLUCION

vacasiones = input('¿Estas de vacasiones? (responde si o no): ')
diaDescanso = input('¿Estas en tus días de descanso? (responde si o no): ')

if vacasiones == 'si':
    vacasiones = True
else:
    vacasiones = False

if diaDescanso == 'si':
    diaDescanso = True
else: 
    diaDescanso = False

if(vacasiones or diaDescanso):
    print('puedes ir a ver el partido')
else:
    print('no puedes ir a ver el partido')


#SOLUCION PROFESOR

vacasiones2 = True
diaDescanso2 = False

if vacasiones2 or diaDescanso2:
    print('Puede asistir al juego')
else:
    print('Tiene deberes por hacer')