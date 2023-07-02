## Programa que retorna true o false si la cadena es un palindromo o no ##
def sin_espacio(cadena):
    cadena2 = ''
    for i in cadena:
        if i == ' ':
            pass
        else:
            cadena2 = cadena2 + i
    return cadena2.casefold()

## esta funcion está hecha sin usar funciones del sistema (excepto la funciont len y casefold) ##
def ispalindromo(texto) -> bool:
    cadena_sin_espacios = sin_espacio(texto)
    my_bool  = bool

    indice = cadena_sin_espacios.__len__()
    for i in range(cadena_sin_espacios.__len__()):
        if cadena_sin_espacios[i:i+1] == cadena_sin_espacios[indice-1:indice]:
            my_bool = True
            indice-=1
        else:
            my_bool = False
            break

    if my_bool:
        return my_bool
    else:
        return my_bool

print(ispalindromo('saippuakivikauppias'))

## funcion que usa funciones del sistema (reversed y casefold) ##
def other_funtion(cadena):
    cadena = sin_espacio(cadena.casefold())
    cadena2 = ''
    for i in reversed(cadena):
        cadena2 = cadena2 + i

    if cadena2 == cadena:
        return True
    else:
        return False
    
print(other_funtion('saippuakivikauppias'))