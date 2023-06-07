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

if(not vacasiones or not diaDescanso):
   print('no puedes ir a ver el partido')
else:
     print('puedes ir a ver el partido')

#SOLUCION PROFESOR

vacasiones2 = True
diaDescanso2 = False

if not(vacasiones2 or diaDescanso2):
    print('Tiene deberes por hacer')
else:
    
    print('Puede asistir al juego')
