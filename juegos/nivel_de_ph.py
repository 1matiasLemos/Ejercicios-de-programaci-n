print("De un valor entre 0 y 14")
nivel_ph = int(input())

if nivel_ph > 7 and nivel_ph <= 14:
    print("El nivel de ph es Basico")
elif nivel_ph < 7 and nivel_ph > 0:
    print("El nivel de ph es Acido")
else:
    print("El ph es neutral")