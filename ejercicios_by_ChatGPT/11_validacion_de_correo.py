import re

def validacion_de_estructura(correo):

    patron = r'^[\w\.-]+@[\w\.-]+\.\w+$'

    if re.match(patron,correo):
        return True
    else:
        return False
    
print(validacion_de_estructura('mat55gammagmail.com'))

'''
'^' - Este símbolo marca el inicio de la cadena. Indica que la dirección de correo debe comenzar con el patrón siguiente.

[\w\.-]+ - Esta parte del patrón coincide con uno o más caracteres alfanuméricos (\w), puntos (.) o guiones (-).
Representa el nombre de usuario en la dirección de correo.

@ - Este símbolo verifica que después del nombre de usuario haya un símbolo de arroba (@).

[\w\.-]+ - Similar a la segunda parte del patrón, coincide con uno o más caracteres alfanuméricos, puntos o guiones.
Representa el dominio de la dirección de correo.

\. - Este símbolo verifica que después del dominio haya un punto (.).

\w+ - Esta parte coincide con uno o más caracteres alfanuméricos. Representa la extensión del dominio (por ejemplo,
.com, .org, .edu, etc.).

$ - El símbolo de dólar marca el final de la cadena. Indica que la dirección de correo debe terminar después de la 
extensión del dominio.'''

print(re.findall(r'[\w]','ola'))
print(re.findall('[oh tambien los]','ola'))

