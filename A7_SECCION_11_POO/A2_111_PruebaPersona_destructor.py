from A0_109_Persona import Persona

print('Creacion de objetos'.center(50,'-'))
persona1 = Persona('Carla', 'Gomez', 30)
persona1.mostrarDetalle()

print('Eliminacion de objetos'.center(50,'-'))                # 111 - SE AGREGA EL MÉTODO DESTRUCTOR EN LA CLASE PERSONA

del persona1

