cadena = "cadena"
nueva = cadena.center(21) #01234567cadena45678901
#esta funcion centra la cadena, sumando la cantidad de caracteres que tiene la cadena
# + el resto que le agregamos  

print(nueva)
print(nueva.__len__()) #21 caracteres en total
print("01234567cadena45678901") #los numeros son la cantidad de espacios

cadena2 = "     hola     mundo     cruel "
print(cadena2)
cadena3 = cadena2.strip()
print(cadena3)

from 06_function_reverse import function_len,reverse_string

print(reverse_string('im as like'))