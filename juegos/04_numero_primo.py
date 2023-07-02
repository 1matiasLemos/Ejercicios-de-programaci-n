num = 1
lista = [num]

for num in range(2,101):

    if num == 2 or num == 3 or num == 5 or num == 7: #solo que sean estos numeros, se agregaran a la lista
        lista.append(num)
    #si el numero se puede dividir entre 2,3,5,o 7, no hacer nada
    elif num % 2 == 0 or num % 3 == 0 or num % 5 == 0 or num % 7 == 0: 
        pass
    else: #en cambio, sino es asi, agregar ese numero a la lista
        lista.append(num)

print(lista)