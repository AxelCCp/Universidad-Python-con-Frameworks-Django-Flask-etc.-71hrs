class MiClase:

    variable_clase = 'Valor variable clase'

    def __init__(self, variable_instancia):
        self.variable_instancia = variable_instancia

    #129 - LOS METODOS ESTATICOS NO PUEDEN ACCEDER A LAS VARIABLES DE INSTANCIA Y NO RECIBEN EL PARAMETRO SELF. PARA ACCEDER A LAS VARIABLES DE CLASE, HAY Q USAR EL NOMBRE DE LA CLASE PRIMERO. 
    @staticmethod
    def metodo_estatico():
        print(MiClase.variable_clase)

    #130 - METODOS DE CLASE - RECIBE EL PARAMETRO DE LA CLASE EN SI MISMO. CLS HACE REFERENCIA A CLASS.  EL CLS FUNCIONA PARECIDO AL SELF.
    @classmethod
    def metodo_de_clase(cls):
        print(cls.variable_clase)

    #131 - COMO EL METODO DE INSTANCIA SE EJECUTA DESDE EL CONTEXTO DINAMICO, SE PUEDE LLAMAR A LOS METODOS DE CLASES Y ESTATICOS.
    def metodo_de_instancia(self):
        self.metodo_de_clase()
        self.metodo_estatico()
        print(self.variable_clase)                 # TMBN SE PUEDE ACCEDER A LAS VARIABLES DE CLASE Y DE INSTANCIA, YA QUE EL METODO DE INSTANCIA SE EJECUTA DESDE EL CONTEXTO DINAMICO
        print(self.variable_instancia)             #


#DESDE LA CLASE SE ACCEDE A LA VARIABLE DE CLASE
print(MiClase.variable_clase)

miClase = MiClase('Valor variable instancia')

#DESDE LA INSTANCIA SE ACCEDE A LAS VARIABLE DE INSTACIA
print(miClase.variable_instancia)

#DESDE UN OBJ TAMBN SE PUEDE ACCEDER A UNA VARIABLE DE CLASE
print(miClase.variable_clase)

miClase2 = MiClase('otro valor de variable de instancia')

print(miClase2.variable_instancia)


print('----------------------------128 - CREACION DE VARIABLES DE CLASE AL VUELO--------------------------')

MiClase.variable_clase2 = 'valor variable clase 2'

print(MiClase.variable_clase2)

print(miClase.variable_clase2)

print(miClase2.variable_clase2)


print('----------------------------- 129. Métodos Estáticos en Python ------------------------------------')

#LLAMANDO AL METODO ESTATICO

MiClase.metodo_estatico()

print('----------------------------- 130. Métodos de Clase en Python ---------------------------------------')

MiClase.metodo_de_clase()

print('----------------------------131. Contexto Estático y Dinámico en Python---------------------------------')

miObj1 = MiClase('variable de instancia.........')
miObj1.metodo_de_clase()                            #CON EL TIPO DE OBJETO miObj1, PYTHON YA SABE EL TIPO DE CLS Q TIENE Q PASAR, POR LO TANTO NO ES NECESARIO PASAR EL CSL POR PARAMETRO CUANDO SE LLAMA AL METODO.

print('-----')

miObj1.metodo_de_instancia()