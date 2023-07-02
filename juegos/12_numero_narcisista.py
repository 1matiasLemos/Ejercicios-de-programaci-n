def amstrong(numero):

    lista = [int(i) for i in str(numero)] #pasamos los caracteres separados en una lista
    amstrong = 0 #en esta variable se guardará la potencia, y tambien se irá sumando todos las potencias
    exponente = lista.__len__() #dependiendo de la cantidad de elementos que tenga lista se usará un expo con la misma cantidad

    for i in lista: #i toma los valores de los elementos de la lista
        amstrong += i ** exponente
    if amstrong == numero:
        return 'Es un numero de amstrong'
    else:
        return 'NO es un numero de amstrong'
    
print(amstrong(153))
