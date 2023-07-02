print("**Welcome to the Ciclone** \nEnter your dates for ride \n")

person = [0, 0, ""]
person[0] = int(input("Enter your height: "))
person[1] = int(input('What´s your credits?: '))

if person[0] >= 137:  # si la persona mide 137 o mas

    if person[1] >= 10:  # si sus creditos son 10 o mas
        print('¡Disfruta el viaje!')
    else:
        print('No tienes suficientes creditos')

elif person[0] < 137 and person[0] >= 100:  # si la persona mide menos que 137

    person[2] = input('Are you with a taller person? (yes/no) ')

    if person[2] == "yes":
        person[2] = True
    elif person[2] == "no":
        person[2] = False

    if person[2] == True and person[1] >= 10:  # si esta con una persona alta y tiene creditos
        print('¡Disfrute el viaje!')
    else:
        print('No puede subir a la montaña rusa')
else:
    print("No eres lo suficientemente alto para subir")