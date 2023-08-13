#274
#alcance de variables   -   non local


def externa():

    var_local_externa = 'var local externa'

    def funcion_anidada():
        
        variable_local_anidada = 'variable local anidada'

        nonlocal var_local_externa                                          #de esta forma podemos trabajar con la variable decarada fuera de la funcion anidada y sin crear una nueva variable dentro de la funcion_anidada. esto se usa por es que queremos modificar la variable.

        var_local_externa = 'nuevo valor variable local anidada'
    
    funcion_anidada()

    print(f'variable local anidada : {var_local_externa}')


externa()



