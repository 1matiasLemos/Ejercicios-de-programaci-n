import random, string

def generar_contraseña_segura(longitud):
    caracteres = string.ascii_letters + string.digits + string.punctuation
    contraseña = []

    # Agregar al menos un caracter de cada tipo
    contraseña.append(random.choice(string.ascii_uppercase))
    contraseña.append(random.choice(string.ascii_lowercase))
    contraseña.append(random.choice(string.digits))
    contraseña.append(random.choice(string.punctuation))

    # Generar caracteres restantes
    for _ in range(longitud - 4):

        while True: #asegura que no se repita ningun caracter
            caracter = random.choice(caracteres)
            if caracter not in contraseña:
                contraseña.append(caracter)
                break

    # Mezclar los caracteres de la contraseña
    random.shuffle(contraseña)

    # Convertir la lista de caracteres en una cadena
    contraseña = ''.join(contraseña)

    return contraseña

try:
    # Solicitar al usuario la longitud deseada de la contraseña
    longitud = int(input("Ingrese la longitud deseada de la contraseña: "))
    # Generar y mostrar la contraseña segura
    contraseña_segura = generar_contraseña_segura(longitud)
    print("Contraseña generada:", contraseña_segura)
except ValueError:
    print('Error: ingrese un número entero')



