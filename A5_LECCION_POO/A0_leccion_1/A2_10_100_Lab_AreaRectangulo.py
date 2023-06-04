
def areaRectangulo(base, altura):
    area = base * altura
    return area

base = int(input('Proporciona la base del rectangulo: '))
altura = int(input('Proporciona la altura de rectangulo: '))


print(f'El area del rectantulo es: {areaRectangulo(base, altura)}')