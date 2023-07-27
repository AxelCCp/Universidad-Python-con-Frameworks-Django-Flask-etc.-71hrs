cursos = 'Java python javascript angular excel'
lista_cursos = cursos.split()
print(lista_cursos)


cursos_separados_por_coma = 'Java,python,javascript,angular,excel'
lista_cursos = cursos_separados_por_coma.split(',')
print(lista_cursos)


cursos_separados_por_coma = 'Java,python,javascript,angular,excel'
lista_cursos = cursos_separados_por_coma.split(',',2)                       #DETERMINA A PARTIR DE QUE  "," VA A DEJAR DE SEPARAR LAS PALABRAS.
print(lista_cursos)