### function reverse ###
def reverse_string(cadena):
    caracteres = function_len(cadena) #contador de caracteres de la cadena de texto
    reverse_cadena = ''
    
    for i in range(caracteres): #el for se ejecuta en funcion de la cantidad de caracteres
        
        letra = cadena[caracteres-1:caracteres] #empezamos desde el caracter final y tomamos ese caracter
        reverse_cadena = reverse_cadena + letra #guardamos el caracter o lo sumamos a la palabra al reves
        caracteres -= 1 #ponemos un decremento de -1 al la cantidad de caracteres hasta que esta llegue a 0


    return reverse_cadena
## function len ##
def function_len(cadena):

    caracteres = 0
    for i in cadena:
        caracteres += 1
    return caracteres


mensaje_espejo = 'oditrevni ejasnem nu se etse'
print(reverse_string(mensaje_espejo))

texto = 'hola me llamos matias'
print(function_len(texto)) # (21) my function 
print(texto.__len__()) # (21) system function

