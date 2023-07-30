#233

string = 'programación con python'
print('string original: ', string)

bytes = string.encode('UTF-8')
print('bytes codificado: ', bytes)

string2 = bytes.decode('UTF-8')
print('string decodificado: ', string2)

print(string == string2)