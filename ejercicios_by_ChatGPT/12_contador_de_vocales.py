import re

def contador_de_vocales(cadena_de_texto):

    # Definición de las vocales y las vocales acentuadas
    letras = 'aeiouáéíóú'
    vocales = {i: 0 for i  in letras+letras.upper()}

    # Conteo de las vocales en la cadena de texto
    for caracter in cadena_de_texto:
        if caracter in vocales.keys():
            vocales[caracter] += 1

    # Búsqueda de dígrafos de vocales utilizando una expresión regular
    patron = '[aeiouáéíóú][aeiouáéíóú]'
    digrafos = re.findall(patron, cadena_de_texto, re.I)

    # Separación de las vocales que sí aparecieron de las que no aparecieron
    vocales_acentuadas = {key: value for key, value in vocales.items() if key in 'áéíóúÁÉÍÓÚ' and value > 0}
    vocales = {key: value for key, value in vocales.items() if key in 'aeiouAEIU' and value > 0}

    # Impresión de los resultados
    print(f'Cantidad de vocales que aparecen en la cadena: {vocales}')
    print(f'Cantidad de vocales acentuadas que aparecen en la cadena: {vocales_acentuadas}')
    print(f'Cantidad de dígrafos que aparecen: {digrafos}')

contador_de_vocales('Contar dígrafos de vocales: En lugar de contar cada vocal individualmente,'+
                    'puedes contar dígrafos de vocales, es decir, dos vocales seguidas. Por ejemplo,'+
                    'contar "ai", "ou", "ei", etc. Esto requerirá un enfoque más complejo para analizar'+
                    'la cadena de texto y encontrar los dígrafos.')
