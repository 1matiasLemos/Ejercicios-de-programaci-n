### Este programa solo traduce cadenas o palabras escritas en minusculas, sin numeros en medio ###
def alfabeto_morse(letra,type):

    import alfabeto_morse
    if type == 'text':
        if letra == 'a':
            letra_morse = alfabeto_morse.letra_a + ' '
            return letra_morse
        elif letra == 'b':
            letra_morse = alfabeto_morse.letra_b + ' '
            return letra_morse
        elif letra == 'c':
            letra_morse = alfabeto_morse.letra_c + ' '
            return letra_morse
        elif letra == 'd':
            letra_morse = alfabeto_morse.letra_d + ' '
            return letra_morse
        elif letra == 'e':
            letra_morse = alfabeto_morse.letra_e + ' '       
            return letra_morse
        elif letra == 'f':
            letra_morse = alfabeto_morse.letra_f + ' '
            return letra_morse
        elif letra == 'g':
            letra_morse = alfabeto_morse.letra_g + ' '
            return letra_morse
        elif letra == 'h':
            letra_morse = alfabeto_morse.letra_h + ' '
            return letra_morse
        elif letra == 'i':
            letra_morse = alfabeto_morse.letra_i + ' '
            return letra_morse
        elif letra == 'j':
            letra_morse = alfabeto_morse.letra_j + ' '
            return letra_morse
        elif letra == 'k':
            letra_morse = alfabeto_morse.letra_k + ' '
            return letra_morse
        elif letra == 'l':
            letra_morse = alfabeto_morse.letra_l + ' '
            return letra_morse
        elif letra == 'm':
            letra_morse = alfabeto_morse.letra_m + ' '
            return letra_morse
        elif letra == 'n':
            letra_morse = alfabeto_morse.letra_n + ' '
            return letra_morse
        elif letra == 'ñ':
            letra_morse = alfabeto_morse.letra_ñ + ' '
            return letra_morse
        elif letra == 'o':
            letra_morse = alfabeto_morse.letra_o + ' '
            return letra_morse
        elif letra == 'p':
            letra_morse = alfabeto_morse.letra_p + ' '
            return letra_morse
        elif letra == 'q':
            letra_morse = alfabeto_morse.letra_q + ' '
            return letra_morse
        elif letra == 'r':
            letra_morse = alfabeto_morse.letra_r + ' '
            return letra_morse
        elif letra == 's':
            letra_morse = alfabeto_morse.letra_s + ' '
            return letra_morse
        elif letra == 't':
            letra_morse = alfabeto_morse.letra_t + ' '
            return letra_morse
        elif letra == 'u':
            letra_morse = alfabeto_morse.letra_u + ' '
            return letra_morse
        elif letra == 'v':
            letra_morse = alfabeto_morse.letra_v + ' '
            return letra_morse
        elif letra == 'w':
            letra_morse = alfabeto_morse.letra_w + ' '
            return letra_morse
        elif letra == 'x':
            letra_morse = alfabeto_morse.letra_x + ' '
            return letra_morse
        elif letra == 'y':
            letra_morse = alfabeto_morse.letra_y + ' '
            return letra_morse
        elif letra == 'z': 
            letra_morse = alfabeto_morse.letra_z + ' '
            return letra_morse

    elif type == 'morse':
        if letra == alfabeto_morse.letra_a:
            letra_texto = 'a'
            return letra_texto
        if letra == alfabeto_morse.letra_b:
            letra_texto = 'b'
            return letra_texto
        elif letra == alfabeto_morse.letra_c:
            letra_texto = str('c')
            return letra_texto
        elif letra == alfabeto_morse.letra_d:
            letra_texto = str('d')
            return letra_texto
        elif letra == alfabeto_morse.letra_e:
            letra_texto = str('e')
            return letra_texto
        elif letra == alfabeto_morse.letra_f:
            letra_texto = str('f')
            return letra_texto
        elif letra == alfabeto_morse.letra_g:
            letra_texto = str('g')
            return letra_texto
        elif letra == alfabeto_morse.letra_h:
            letra_texto = str('h')
            return letra_texto
        elif letra == alfabeto_morse.letra_i:
            letra_texto = str('i')
            return letra_texto
        elif letra == alfabeto_morse.letra_j:
            letra_texto = str('j')
            return letra_texto
        elif letra == alfabeto_morse.letra_k:
            letra_texto = str('k')
            return letra_texto
        elif letra == alfabeto_morse.letra_l:
            letra_texto = str('l')
            return letra_texto
        elif letra == alfabeto_morse.letra_m:
            letra_texto = str('m')
            return letra_texto
        elif letra == alfabeto_morse.letra_n:
            letra_texto = str('n')
            return letra_texto
        elif letra == alfabeto_morse.letra_ñ:
            letra_texto = str('ñ')
            return letra_texto
        elif letra == alfabeto_morse.letra_o:
            letra_texto = str('o')
            return letra_texto
        elif letra == alfabeto_morse.letra_p:
            letra_texto = str('p')
            return letra_texto
        elif letra == alfabeto_morse.letra_q:
            letra_texto = str('q')
            return letra_texto
        elif letra == alfabeto_morse.letra_r:
            letra_texto = str('r')
            return letra_texto
        elif letra == alfabeto_morse.letra_s:
            letra_texto = str('s')
            return letra_texto
        elif letra == alfabeto_morse.letra_t:
            letra_texto = str('t')
            return letra_texto
        elif letra == alfabeto_morse.letra_u:
            letra_texto = str('u')
            return letra_texto
        elif letra == alfabeto_morse.letra_v:
            letra_texto = str('v')
            return letra_texto
        elif letra == alfabeto_morse.letra_w:
            letra_texto = str('w')
            return letra_texto
        elif letra == alfabeto_morse.letra_x:
            letra_texto = str('x')
            return letra_texto
        elif letra == alfabeto_morse.letra_y:
            letra_texto = str('y')
            return letra_texto
        elif letra == alfabeto_morse.letra_z:
            letra_texto = str('z')
            return letra_texto

def traductor_morse(cadena):

    if cadena[0:1] == '·' or cadena[0:1] == '-': #definimos el tipo de lenguaje en base a su primer caracter
        texto = ''
        tipo = 'morse' 
        i2 = 0 #estos son los contadores de caracteres que nos serviran para tomar una cadena de codigo morse, una letra
        i1 = 0
        for i in cadena: #iremos pasando por cada punto y guion de todo el codigo morse

            if i1 == cadena.__len__()-1: #en caso de estar en el penultimo caracter
                letra_str = alfabeto_morse(cadena[i2:i1+1],tipo) #tomamos la ultima letra y la enviamos 
                texto = texto + str(letra_str) #guardamos o agregamos la letra traducida a la cadena o palabra en str

            elif i == ' ': #cuando la i este situada en un espacio, significa que la letra termina ahi
                letra_str = alfabeto_morse(cadena[i2:i1],tipo)  #tomamos el codigo o letra en morse y la traducimos
                texto = texto + str(letra_str) #guardamos la letra traducida y agregamos a la palabra 
                i2 = i1 + 1  #situamos los indices al final del espacio y el comienzo de un caracter
                i1 += 1 

            elif i == '/': #cuando i sea una barra / significa que la palabra termina ahi
                letra_str2 = alfabeto_morse(cadena[i2:i1],tipo) #tomamos la ultimata letra en morse de esa palabra y la traducimos
                texto = texto + str(letra_str2)
                texto += ' ' #aqui hemos traducido una palabra de toda la cadena, por lo tanto dejamos un espacio
                i2 = i1 +1
                i1 +=1
            else: #si i aun no llega a un espacio, ni a un barra y tampoco al final de la cadena de codigo morse
                i1 +=1 #incrementamos el indice que indica el final de una letra morse
        print(texto)
                
    elif cadena[0:1] != '·' or cadena[0:1] != '-': #si no es un texto en codigo morse
        tipo = 'text'
        palabra_morse = ''
        for i in cadena:

            if i == ' ': #cuando haya un espacio entre las palabras de la cadena
                #como cada letra termina escribiendose y agregando un espacio, debemos borrar ese ultimo espacio
                palabra_morse = palabra_morse[0:palabra_morse.__len__()-1] 
                #escribimos toda la cadena a medio traducir menos en ultimo caracter que seria el espacio

                palabra_morse += '/' #escribimos lo que es equvalente a un espacio o sangria en codigo morse
            else:
                palabra_morse = palabra_morse + alfabeto_morse(i,tipo)
        print(palabra_morse)
