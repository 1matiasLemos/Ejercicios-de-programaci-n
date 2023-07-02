palabra1 = str(input("Ingresa la primera palabra: "))
palabra2 = str(input("Ingresa la segunda: "))
palabra1 = palabra1.casefold() #en caso de que esten escritas en mayusculas
palabra2 = palabra2.casefold()

if palabra1.__len__() == palabra2.__len__(): #si tienen la misma cantidad de caracteres
    
    caracteres = palabra1.__len__()
    verificador = bool
    i = 0

    while i < caracteres:

        letra = palabra1[i:i+1] #toma la primera letra de la cadena
        
        count1 = palabra1.count(letra) #comprueba que exista esa letra en ambas cadenas
        count2 = palabra2.count(letra) #se guarda el valor de la cuenta de letras iguales

        if count1 == count2: #si la cantidad de letras son las mismas en ambas cadenas
            verificador = True
            i += 1
        else:
            verificador = False #si no hay la misma cantidad de letras
            i = caracteres

    if verificador == False:
        print('No es un anagrama')
    elif verificador == True:
        print('Es un anagrama')

else:
    print('No es un anagrama')