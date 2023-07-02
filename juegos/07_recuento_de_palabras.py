def recontador(cadena): #separá las palabras
    cadena1 = str(cadena) #en caso de enviar un tipo de dato diferente
    lista_word = []
    i1 = 0
    i2 = 0
    caracteres = cadena1.__len__()+1 #le agrego un caracter mas para que el for recorra toda la cadena hasta el final
    cantidad_de_palabras = 0

    for i in range(0,caracteres): #si se llega al final de la cadena de texto

        if i+1 == caracteres: #si i está en el ultimo caracter ej:(i=4,caracter = 5: i+1 = 5 = caracteres)
            lista_word.append(cadena1[i1:i2])
            i1 = i2 +1
            i2 += 1
            cantidad_de_palabras +=1
            #esto hará que se termine el for

        #en caso de que haya dos espacion juntos, no se cuenta como una palabra y se sigue adelante
             #espacio detectado:     #siguiente caracter que no sea un espacio: 
        elif cadena1[i2:i2+1] == ' ' and cadena1[i2+1:i2+2] != ' ':
            lista_word.append(cadena1[i1:i2]) #agregamos la palabra o cadena de texto separada a una lista

            i1 = i2 +1 #le pasamos en valor de ultimo caracter para que empiece al final de cualquier palabra encontrada
            i2 += 1 #le sumamos 1 para que se salte el espacio y empiece desde el siguiente caracter o letra
            cantidad_de_palabras +=1 #se cuenta la cantidad de palabras encontradas una en una 

        else: 
            i2 += 1 #se sigue aumentado hasta encontrar un espacio
        
    return lista_word, cantidad_de_palabras #se devuelve las palabras separadas en una lista y cuantas son en total

def comparador(lista_de_palabras):

    words, count = recontador(lista_de_palabras) #se recibe la lista de palabras y el numero total o cuantas son en total
    if count == 0 or words[0] == '': #si no se escribió nada como parametro
        print('No se envió ninguna palabra o caracter, escriba algo')
    else:
        palabras_repeat = [] #esta lista contendra cuales son las palabras repetidas para imprimir en consola
        hay_o_no = False
        for iprime in range (count): #el for se ejecutará en funcion de la cantidad de palabras que se detectaron, desde 1
            
            isecond = iprime #se usará un segundo numero que indicará el y/o los elementos siguientes
            for isecond in range(isecond+1,count): #se empezará desde el siguiente elemento a iprime ej(ip = 3, entonces ise = 3+1)
                
                if words[iprime] == words[isecond]: #se compara desde el elemento en el que se encuentre iprime hasta el final
                    palabras_repeat.append(words[iprime] + ": 1 vez") #se guarda la palabra repetida y se le agrega un contador 
                    hay_o_no = True #se da el aprobado si hay tan solo una y no se cambia

        if hay_o_no == False:
            print(f'{words}\nLas cantida de palabras o caracteres son {count}\nNo hay palabras repetidas')
        else:
            print(f'{words}\nSon {count} palabras\nLa/s palabra/s repetida/s es/son {palabras_repeat}')


comparador('')