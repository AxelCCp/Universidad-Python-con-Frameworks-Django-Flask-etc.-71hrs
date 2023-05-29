# EL SET NO TIENE INDICES , POR LO TANTO NO TIENE ORDEN, EL ORDEN ES VARIABLE, NO PERMITE MODIFICAR LOS ELEMENTOS UNA VEZ AGREGADOS AL SET, 
#..SI PERMITE AGREGAR Y ELIMINAR ELEMENTOS. NO PERMITE ELEMENTOS DUPLICADOS.

planetas = {'Marte', 'Jupiter', 'Venus'}
print(planetas)

#LARGO
print(len(planetas))
#VER SI UN ELEMENTO ESTÁ PRESENTE
print('Marte' in planetas)
#AGREGAR ELEMENTOS
planetas.add('Tierra')
print(planetas)
#NO PERMITE DUPLICADOS
planetas.add('Tierra')
print(planetas)
#ELIMINAR ELEMENTO ... PUEDE ARROJAR ERROR SI NO ENCUENTRA EL ELEMENTO
planetas.remove('Tierra')
print(planetas)

#ELIMINAR ELEMENTO ... NO ARROJA ERROR SI NO ENCUENTRA EL ELEMENTO
planetas.discard('TierraX')
print(planetas)

#LIMPIAR ELEMENTOS DEL SET
planetas.clear()
print(planetas)

#ELIMINAR EL SET
del planetas

#DARÁ ERROR X X X
print(planetas)
