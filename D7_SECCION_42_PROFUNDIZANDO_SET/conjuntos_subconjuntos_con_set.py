#268
#subset - superset - disjoint

pelo_negro = {'juan', 'karla', 'pedro', 'maria'}
pelo_rubio = {'lorenzo', 'claudia', 'laura'}
ojos_cafe = {'karla', 'laura'}
menores_30 = {'juan', 'karla', 'maria'}


#subset
#preguntas si un set esta contenido en otro 
#revisamos si los elementos del primer set  estan contenidos en el segundo set
print(menores_30.issubset(pelo_negro)) 


#superset
#preguntas si un set contiene los elementos de otro set
#revisar si los elementos del primer set estan contenidos en el segundo set
print(menores_30.issuperset(pelo_negro))                                                    #da false pq no estan todos dentro.


#disjoint
#pregunta si los de pelo negro no tienen pelo rubio
print(pelo_negro.isdisjoint(pelo_rubio))                    #true : no tienen  elementos en comun.