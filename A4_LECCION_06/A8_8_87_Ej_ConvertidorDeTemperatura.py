
def celsiusToFarenheit(gradosCelsius):
    gradosFarenheit = (gradosCelsius * 9/5) + 32
    print(f'{gradosCelsius:.2f}° celsius   --->  {gradosFarenheit:.2f}° farenheit')

celsius = float(input('Ingresa los grados celsius: '))

celsiusToFarenheit(celsius)


print('')


def farenheitToCelsius(gradosFarenheit):
    gradosCelsius = (gradosFarenheit - 32) * 5/9
    print(f'{gradosFarenheit:.2f}° farenheit   --->  {gradosCelsius:.2f}° celsius')

faren = float(input('ingresa los grados farenheit: '))

farenheitToCelsius(faren)
