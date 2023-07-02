## Esta funcion se encarga de retorna un cadena de texto, poniendo la primera letra de cada palabra en mayúscula ##
## Teniendo en cuenta los signos de puntuacion y acentos ##
abc = 'abcdefghijklmnñopqrstuvwxyzABCDEFGHIJKLMNÑOPQRSTUVWXYZáéíóúÁÉÍÓÚ'

def corrector_mayuscula(texto: str) -> str:
    palabra_correcta = ''
    indice = 0

    for i in texto:
        
        # esta parte solo se ejecutará una vez, es cuando no hay nada antes de la primer palabra, ni espacio
        if indice == 0 and i != ' ': 
            palabra_correcta += i.upper()
            indice +=1

        #si el caracter anterior a i no está dentro del abc, indica que empieza una palabra nueva
        elif texto[indice-1:indice] not in abc and i != ' ': 
            palabra_correcta += i.upper()
            indice +=1
        else: 
            palabra_correcta += i
            indice +=1

    return palabra_correcta

print(corrector_mayuscula('¿hola qué tal estás?'))
print(corrector_mayuscula('¿hola         qué tal estás?'))
print(corrector_mayuscula('El niño ñoño'))