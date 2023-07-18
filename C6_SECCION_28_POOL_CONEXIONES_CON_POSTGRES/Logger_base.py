import logging as log


# DEBUG : ESTO CONFIGURA EL NIVEL DESDE DONDE LOS LOGS Q SE VAN A MOSTRAR.
# FORMAT : FORMATO DE MENSAJE.  %(asctime)s = TIEMPO. / %(levelname)s [%(filename)s: %(lineno)s] = NIVEL DEL MENSAJE CON NOMBRE DEL ARCHIVO Q LANZÓ EL MENSAJE. / %(message)s = NOMBRE DEL MENSAJE.
# FORMATO DE LA FECHA: HORA-MINUTO-SEGUNDO,  AM O PM.
# SE CONFIGURA Q SE VA A MANDAR LA INFO A UN ARCHIVO.  / TAMBN SE AGREGA LA CONSOLA.
log.basicConfig(level=log.DEBUG, 
                format='%(asctime)s: %(levelname)s [%(filename)s: %(lineno)s] %(message)s', 
                datefmt='%I:%M:%S %p', 
                handlers=[log.FileHandler('capa_datos.log'), log.StreamHandler()])   




if __name__ ==  '__main__':

    log.debug('Mensaje a nivel de debug')

    log.info('Mensaje a nivel de info')

    log.warning('Mensaje a nivel de warning')

    log.error('Mensaje a nivel de error')

    log.critical('Mensaje a nivel crítico')

