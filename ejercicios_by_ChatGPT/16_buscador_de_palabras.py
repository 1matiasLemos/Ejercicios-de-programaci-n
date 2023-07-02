import re

def acceder_archivo(nombre_del_archivo, all_file = False, line_file = False): 
    
    with open(f'ejercicios_by_ChatGPT/{nombre_del_archivo}.txt', 'r', encoding='UTF-8') as file_text:

        if all_file: #si se escojió leer todo el archivo
            if opcion_up_or_case == 'M':
                return file_text.read().upper() #devuelve todo el contenido del archivo en mayusculas
            else:
                return file_text.read().casefold() #devuelve todo el contenido del archivo en minusculas
                
        elif line_file: #si se escojió leer una linea especifica

            #quita los saltos de linea para que quede mas acorde al tetxo original
            if opcion_up_or_case == 'M':
                texto_en_lineas = [lineas.strip().upper() for lineas in file_text.readlines()]
                return texto_en_lineas #se retorna el archivo separado en lineas
            else:
                texto_en_lineas = [lineas.strip().casefold() for lineas in file_text.readlines()]
                return texto_en_lineas #se retorna el archivo separado en lineas


def opciones_de_lectura(): #retorna una opción como True y un False, dos opciones de lectura
    while True:
        print('Escoja una opción\n  1. Leer todo el archivo y buscar\n  2. Leer lineas especificas y buscar')
        try:
            opcion = int(input(''))
            if opcion == 1:
                return True, False #opcion escogida: leer todo el archivo
            elif opcion == 2:
                return False, True #opción escogida: leer lineas especificas
            else:
                print('Opción no válida\n')

        except ValueError:
            print('Opción no válida\n')


def buscador_global(name_file,word):
    
    while True: #se asegura de que el nombre del archivo este correcto
        try: #utiliza un findall para hacer una lista con el arg word como expresion, luego pasa por un len
            if opcion_up_or_case == 'M':
                word = word.upper()
            else:
                word = word.casefold()

            veces_repetidas = len(re.findall(word,acceder_archivo(name_file,True)))
            break
        except FileNotFoundError: #da error si el nombre del archivo no es encontrado dentro de la carpeta
            print('Error: el nombre del archivo no existe dentro de la carpeta')
            name_file = input('Ingrese el nombre del archivo: ')

    if veces_repetidas == 1:
        print(f'\nLa palabra "{word}" buscada en el archivo se repite {veces_repetidas} vez')
        print(marcar_posicion_de_palabras(name_file, word))
    elif veces_repetidas > 1:
        print(f'\nLa palabra "{word}" buscada en el archivo se repite {veces_repetidas} veces')
        print(marcar_posicion_de_palabras(name_file, word))
    else:
        print(f'\nLa palabra "{word}" no se encontró')


def buscador_por_lineas(name_file,word):

    def texto_a_lineas(name_file): #devuelde el contenido del archivo en una lista, donde cada elemento es una linea
        while True: #se asegura de que el nombre del archivo exista
            try:
                return acceder_archivo(name_file,line_file=True)
                break
            except FileNotFoundError: #si no existe lo pide de nuevo
                print('Error: el nombre del archivo no existe dentro de la carpeta\n')
                name_file = input('Ingrese el nombre del archivo: ')  

    def separador_y_contador_de_lineas(texto,num_line): #busca el numero de las lineas y las separa

        lineas_especificas = [texto[linea-1] for linea in num_line if linea <= len(texto)]
        veces_repetidas = 0

        for revisor in lineas_especificas: #cuenta cuantas veces se repite el arg word dentro de cada linea
            veces_repetidas += len(re.findall(word,revisor,re.IGNORECASE))        
        return veces_repetidas
    
    #pide el numero de las lineas
    print('\nDebe escribir el o los números de las lineas especificas en donde desea buscar')
    print('Puede ser 1 3 4 o 1,3,4.')
    # utiliza una expresion regular que solo reconoce números, asi no da errores
    num_line = [int(numero) for numero in re.findall(r'\d+',(input('Linea número _ ')))]            
    texto_en_lineas = texto_a_lineas(name_file)

    if opcion_up_or_case == 'M':
        word = word.upper()
    else:
        word = word.casefold()
        
    palabra_repetida_cantidad = separador_y_contador_de_lineas(texto_en_lineas,num_line)

    if palabra_repetida_cantidad == 1:
        print(f'\nLa palabra "{word}" buscada en la/s linea/s {num_line} se repite {palabra_repetida_cantidad} vez')

    elif palabra_repetida_cantidad > 1:
        print(f'\nLa palabra "{word}" buscada en la/s linea/s {num_line} se repite {palabra_repetida_cantidad} veces')
    else:
        print(f'\nLa palabra "{word}" no se encontró dentro de la/s linea/s {num_line}')


def ingresar_datos(): #pide el nombre del archivo y la palabra a buscar
    
    name_file = input('\nIngrese el nombre del archivo: ')
    word = input('Ingrese la palabra que desea buscar: ')
    return name_file, word


def marcar_posicion_de_palabras(name_file, word): #devuelve el numero de las lineas en donde se encontró la palabra

    with open(f'ejercicios_by_ChatGPT\{name_file}.txt','r+',encoding='UTF-8') as texto:
        marcador_de_linea = [] #guardará el numero de las lineas
        linea  = 1 #indice para ir de 1 hasta el final de las lineas

        for i in texto.readlines(): #irá linea por linea
            if re.search(word,i,re.IGNORECASE): #busca la palabra
                marcador_de_linea.append(linea) #marca en que linea se encontró la palabra
            linea+=1 #se incrementa para hacer referencia a que pasa a la siguiente linea

        return f'En la/s linea/s: '+ ', '.join(str(linea) for linea in marcador_de_linea)


def capitalize_or_casefold():

    print('¿Desea Buscar en mayusculas o minusculas?')
    while True:
        global opcion_up_or_case
        opcion_up_or_case = input('Escoja: M (mayuscula)/ m (minuscula) ')
        
        if opcion_up_or_case == 'm' or opcion_up_or_case == 'M':
            break
        else:
            print('Opción no Válida')


def inicio():

    print('Bienvenido al Contador de Palabras')
    while True:
        global word
        name_file, word = ingresar_datos() #solicita el nombre del archivo y la palabra a buscar

        while True:
            all_file,line_file = opciones_de_lectura() #si desea buscar en todo el archivo o solo en lineas especificas
            capitalize_or_casefold() #solicita si debe buscar en minusculas o mayusculas
            if all_file:  #busca en todo el archivo
                buscador_global(name_file,word) 
            elif line_file: #busca en las lineas ingresadas
                buscador_por_lineas(name_file,word)

            if input('\n¿Salir? 1(si)/Enter(no)'): #si se escribe algo es un True, sino es un False
                break
            if input('¿Cambiar de archivo? 1(si)/Enter(no)'):
                name_file, word = ingresar_datos()
            else: #sigue buscando en el mismo archivo hasta que salga del programa o seleccione para cambiar archivo
                word = input('Ingrese la palabra que desea buscar: ')
        break
    print('\nEl programa finalizó')


## Codigo por ChatGPT

def buscar_palabra_avanzado():
    archivo = input("Ingrese el nombre del archivo: ")  # Solicitar el nombre del archivo
    palabra = input("Ingrese la palabra a buscar: ")  # Solicitar la palabra a buscar
    opcion_mayusculas = input("¿Desea buscar en mayúsculas? (s/n): ")  # Opción de buscar en mayúsculas o minúsculas
    opcion_lineas = input("¿Desea buscar en todas las líneas del archivo? (s/n): ")  # Opción de buscar en todas las líneas o en líneas específicas

    if opcion_mayusculas.lower() == 'n':
        palabra = palabra.lower()  # Convertir la palabra a minúsculas si se elige buscar en minúsculas

    with open(f'ejercicios_by_ChatGPT/{archivo}.txt', 'r', encoding='UTF-8') as archivo_txt:  # Abrir el archivo en modo de lectura
        lineas = archivo_txt.readlines()  # Leer todas las líneas del archivo

        if opcion_lineas.lower() == 's':
            lineas_busqueda = lineas  # Usar todas las líneas del archivo para la búsqueda
        else:
            num_lineas = len(lineas)
            linea_inicio = int(input(f"Ingrese el número de línea de inicio (1-{num_lineas}): "))  # Solicitar el número de línea de inicio
            linea_fin = int(input(f"Ingrese el número de línea de fin (1-{num_lineas}): "))  # Solicitar el número de línea de fin
            lineas_busqueda = lineas[linea_inicio - 1:linea_fin]  # Usar las líneas específicas para la búsqueda

        contador_ocurrencias = 0

        for i, linea in enumerate(lineas_busqueda):  # Iterar sobre las líneas de búsqueda
            palabras_linea = linea.split()  # Separar las palabras de la línea
            for j, palabra_linea in enumerate(palabras_linea):  # Iterar sobre las palabras de la línea
                if palabra == palabra_linea:  # Comparar la palabra buscada con la palabra actual
                    contador_ocurrencias += 1  # Incrementar el contador de ocurrencias
                    if opcion_lineas.lower() == 's':
                        posicion = f"Línea {i + 1}, Palabra {j + 1}"  # Calcular la posición de la ocurrencia en todas las líneas
                    else:
                        posicion = f"Línea {linea_inicio + i}, Palabra {j + 1}"  # Calcular la posición de la ocurrencia en líneas específicas
                    print(f"Ocurrencia encontrada: {posicion}")  # Mostrar la posición de la ocurrencia

    print(f"Total de ocurrencias encontradas: {contador_ocurrencias}")  # Mostrar el total de ocurrencias encontradas

buscar_palabra_avanzado()