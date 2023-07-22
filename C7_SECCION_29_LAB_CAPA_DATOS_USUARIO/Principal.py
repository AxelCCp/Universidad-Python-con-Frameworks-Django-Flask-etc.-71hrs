from UsuarioDao import UsuarioDao
from MyLogger import log
from Usuario import Usuario


op = int(input('''Menú de gestión de usuarios
            
            Selecciona una opción:
            
                        1. listar usuarios.
                        2. agregar usuarios.
                        3. modificar usuario.
                        4. eliminar usuario.
                        5. salir.

            Escribe tu opción del 1 al 5: '''))

cont = 0

while op != 5:

    if cont != 0:
        op = int(input('''Menú de gestión de usuarios
                
                Selecciona una opción:
                
                            1. listar usuarios.
                            2. agregar usuarios.
                            3. modificar usuario.
                            4. eliminar usuario.
                            5. salir.

                Escribe tu opción del 1 al 5: '''))
    cont+=1

    if op == 1:
        print('Listado de usuarios:')
        usuarios = UsuarioDao.seleccionar()
        for u in usuarios:
            log.debug(u)
            
    elif op == 2:
        print('\nAgregando usuario...\nIngresa los siguientes datos del nuevo usuario:')
        newUsername = input('Username: ')
        newPassword = input('Password: ')    
        usuario = Usuario(username = newUsername, password = newPassword)
        UsuarioDao.insertar(usuario)

    elif op == 3:
        print('\nActualizando usuario...\nIngresa los siguientes datos para actualizar a un usuario:')
        idUser = int(input('Id_usuario: '))
        newUsername = input('Username: ')
        newPassword = input('Password: ')
        usuario = Usuario(id_usuario=idUser, username=newUsername, password=newPassword)
        UsuarioDao.actualizar(usuario)

    elif op == 4:
        print('\nEliminando usuario...\nIngresa el id del usuario que quieres elimminar:')
        idUser = int(input('Id_usuario: '))
        usuario = Usuario(id_usuario=idUser)
        UsuarioDao.eliminar(usuario)
    elif op == 5:
        break
    else:
        print('Escoge una opción válida entre 1 y 5')