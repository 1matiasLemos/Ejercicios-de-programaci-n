## Mi codigo original
import re

def reversion(frase):

    ## Eliminacion de caracteres especiales y números ## 
    palabras = [re.sub(r'\W|\d','',palabra) for palabra in frase.split()]
    
    ## Inversion de la frase ## 
    frase_invertida = ' '.join(palabra[::-1] for palabra in palabras)

    ### Remplazo de vocales por numero de la secuencia Fibonacci ###
    vocales_encontradas = len(re.findall(r'[aeiouAEIOUÁÉÍÓÚáéíóú]',frase_invertida)) #contador de vocales

    a,b=0,1 #primer y segundo número para la secuencia
    fibonacci = [a,b]

    #la cantidad de números en la secuencia será igual a la cantidad de vocales dentro de la frase
    while len(fibonacci) < vocales_encontradas: 
        fibonacci.append(a+b) #vamos creando la secuencia fibonacci
        a,b = b,a+b
    index_fibonacci = 0 #el index para movernos por la lista fibonacci

    frase_modificada = '' #aqui alojaremos la frase modificada con los números de la secuencia fobonacci
    for letra in frase_invertida: #iteramos sobre todos los caracteres de la frase
        
        if re.match(r'[aeiouAEIOUÁÉÍÓÚáéíóú]',letra): #si la letra es una vocal
            frase_modificada += str(fibonacci[index_fibonacci]) #se agregará el número correspondiente de la secuencia
            index_fibonacci += 1 #incrementamos, para que pase al siguiente número de la secuencia
        else:
            frase_modificada += letra #agrega la letra a la frase

    return frase_modificada 

frase_invertida = reversion(input('Ingrese su texto o frase: \n _ '))
print(f'Su frase invertida: {frase_invertida}')


## Codigo mejorado por ChatGPT ##

def reversion(frase):
    # Eliminación de caracteres especiales y números
    palabras = [re.sub(r'[^a-zA-Z]', '', palabra) for palabra in frase.split()]
    
    # Inversión de la frase
    frase_invertida = ' '.join(palabra[::-1] for palabra in palabras)

    # Reemplazo de vocales por números de la secuencia Fibonacci
    vocales_encontradas = sum(1 for letra in frase_invertida if letra in 'aeiouAEIOUÁÉÍÓÚáéíóú')

    fibonacci = [0, 1]
    while len(fibonacci) < vocales_encontradas:
        fibonacci.append(fibonacci[-1] + fibonacci[-2])

    index_fibonacci = 0
    frase_modificada = ''
    for letra in frase_invertida:
        if letra.lower() in 'aeiouáéíóú':
            frase_modificada += str(fibonacci[index_fibonacci])
            index_fibonacci += 1
        else:
            frase_modificada += letra

    return frase_modificada 

frase_invertida = reversion(input('Ingrese su texto o frase: \n _ '))
print(f'Su frase invertida: {frase_invertida}')
