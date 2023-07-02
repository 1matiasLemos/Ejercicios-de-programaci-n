
print("Hasta donde quieres que se ejecute la secuencia?")
fin = int(input())

num_sec = 0
a = 0
b = 1

while num_sec <= fin:

    print(num_sec, end=", ") #sirve para imprimir en una linea, sin salto de linea en cada impresion

    a = b
    b = num_sec
    num_sec = a + b
    