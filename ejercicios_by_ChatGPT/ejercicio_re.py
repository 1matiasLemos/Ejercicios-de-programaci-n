import re

def extraer_numeros(cadena):
    # Escribir el patrón de expresión regular aquí
    patron = r"[-+]?\d+(?:\.\d+)?"
    
    # Utilizar el método findall() de re para extraer los números
    print(re.findall(patron,cadena))
# Solicitar la cadena de texto al usuario
    cadena_ingresada = input("Ingresa una cadena de texto: ")

# Llamar a la función de extracción de números3fnf4j88f2j9f
# extraer_numeros(cadena_ingresada)

'''
[-+]? indica que el número puede tener un signo positivo (+) o negativo (-) opcional al comienzo.
\d+ coincide con una o más ocurrencias de dígitos del 0 al 9.
(?:\.\d+)? indica que puede haber un punto decimal (.) seguido de una o más ocurrencias de dígitos del 0 al 9,
y el ? indica que esta parte es opcional.'''

## usamos el patron para aprender

talvez_patron = r'[gh]?\d+' #[gh]? sirve para decir, "puede que contenga una g o h antes del decimal"
# si pones [\w]?\d+ esto indica que puede que haya una letra antes del decimal (patron: letra_opcional-decimal,ej r245, t455)
print(re.findall(talvez_patron,'asdh23holag83')) #['h23','g83']


otro_patron_opcional = r'\d+[a-k]?(?:[q-z]+)?' 
'''\d+ (decimal hasta donde termine el numero) 
[a-k]? (puede que haya una letra de la "a" a la "k" seguido del decimal), 
(?:[q-z]+)?sino puede que haya, en su lugar, letras de la "q" hasta la "z" '''
                                                 #\d+[a-k]?  \d+[q-z]+?
print(re.findall(otro_patron_opcional,'15d12qt')) #['15d',    '12qt']