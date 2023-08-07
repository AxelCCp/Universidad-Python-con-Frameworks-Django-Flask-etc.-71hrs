#266
#operaciones de conjuntos con set

#personas con diferentes caracteristicas
pelo_negro = {'juan', 'karla', 'pedro', 'maria'}
pelo_rubio = {'lorenzo', 'claudia', 'laura'}
ojos_cafe = {'karla', 'laura'}
menores_30 = {'juan', 'karla', 'maria'}

#funcion de union
#todos los elementos con color caje y pelo rubio
print(ojos_cafe.union(pelo_rubio))

#operacion conmutativa
#nvertir el orden con el mismo resultado
print(pelo_rubio.union(ojos_cafe))


# (intersection)  
# solo las personas  con ojos cage y pelo rubio
print(ojos_cafe.intersection(pelo_rubio))
#conmutativa
print(pelo_rubio.intersection(ojos_cafe))


# (difference)
#pelo negro sin ojos cafe
#personas que se encuentran en el primer set pero no en el segundo
print(pelo_negro.difference(ojos_cafe))


#diferencia simetrica
#devuelve todos los elementos menos las coincidencias entre dos set
print(pelo_negro.symmetric_difference(ojos_cafe))







