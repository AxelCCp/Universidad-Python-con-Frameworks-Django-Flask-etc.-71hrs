#272

var_global = 'variable global' 

def imprimir():

    global var_global                                                   #Para poder modificar la var global dentro de un metodo, hay q ponerla con global. sino se pone, solo sirve de lerctura.
    
    print(f'variable global desde función: {var_global}')

    var_local = 'variable_local'

    print(f'variable local desde función: {var_local}')

    var_global = 'nuevo valor'

    print(f'Var global modificada : {var_global}')



imprimir()