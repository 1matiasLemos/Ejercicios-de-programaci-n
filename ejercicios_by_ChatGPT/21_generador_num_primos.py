
def imprimir_numeros_primos(desde:int,hasta:int):

    #Manera 1 de encontrar numeros primos
    numeros_primos_encontrados:list = []
    
    for numero in range(desde,hasta+1):
        if numero.__abs__() in [2,3,5,7]:
            numeros_primos_encontrados.append(numero)
        elif numero.__abs__() % 2 != 0 and numero.__abs__() % 3 != 0 and numero.__abs__() % 5 != 0 and numero.__abs__() % 7 != 0:
            numeros_primos_encontrados.append(numero)

    #Manera 2 de encontrar numeros primos 
    lista_numerica = [num for num in range(desde,hasta+1) if num.__abs__() in [2,3,5,7] or num.__abs__() != 1 and num != 0]
    lista_numerica = [num for num in lista_numerica if num.__abs__() == 2 or num % 2 != 0]
    lista_numerica = [num for num in lista_numerica if num.__abs__() == 3 or num % 3 != 0]
    lista_numerica = [num for num in lista_numerica if num.__abs__() == 5 or num % 5 != 0]
    lista_numerica = [num for num in lista_numerica if num.__abs__() == 7 or num % 7 != 0]
    print(lista_numerica)
    print(numeros_primos_encontrados)

imprimir_numeros_primos(-34,100)
