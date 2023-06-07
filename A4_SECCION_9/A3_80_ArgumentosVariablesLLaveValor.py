def listarTerminos(**terminos):
    for llave, valor in terminos.items():
        print(f'{llave} {valor}')

#SE PUEDE LLAMAR SIN PARAMETROS
listarTerminos()

#CON PARAMETROS
listarTerminos(IDE='Integrated Development Environment', PK='Primary key')
listarTerminos(DBMS='Database Management System')