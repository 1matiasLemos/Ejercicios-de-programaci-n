import csv

def acceder_a_lista_de_tareas():
    with open('ejercicios_by_ChatGPT/lista de tareas.csv',encoding='UTF-8') as lista_de_tareas:
        return [i.strip() for i in lista_de_tareas.readlines()] #devuelve una lista con todos los elementos de la lista 
        #cada linea es una fila de toda la lista, con el strip quito el salto de linea que tiene por defecto
        #para evitar errores en la impresion de la lista

def sobrescribir_lista_de_tareas(texto_para_sobrescribir):
    with open('ejercicios_by_ChatGPT/lista de tareas.csv','w+',encoding='UTF-8') as lista_de_tareas: #encoding para evitar errores con los acentos
        escritor = csv.writer(lista_de_tareas,lineterminator='\n') #solo da un salto de linea por cada fila creada
        #el lineterminator sirve para indicar que hacer luego de crear una fila
        for tarea in texto_para_sobrescribir: #escribe cada elemento en una nueva fila
            escritor.writerow([tarea]) #ponemos corchetes para indicar que es una fila de un elemento


def agregar_tarea(lista):#tiene como arg la lista de tareas
     
    lista.append(input('Nueva tarea: ').capitalize()) #recibe la nueva tarea para agregar a la lista
    sobrescribir_lista_de_tareas(lista) #agrega la lista con la nueva tarea
    print('---Nueva tarea agregado a la lista---') #mensaje de salida
        

def eliminar_tarea(lista): #tiene como arg la lista de tareas existente
    tarea_a_eliminar = input('Escriba el nombre de la tarea: ').capitalize() #recibe el nombre de la tarea

    if tarea_a_eliminar in lista: #busca que esa tarea exista dentro de la lista de tareas
        lista.remove(tarea_a_eliminar) #quita ese elemento de la lista
        sobrescribir_lista_de_tareas(lista) #actualiza la lista
        print('---Tarea eliminada existosamente---') #mensaje de operacion realizada 
    else:
        print('Esa tarea no existe en la lista de tareas')#mensaje de error

def menu_principal():
    print('_-_-_-_Bienvenido al Organizzador de Tareas Pendientes_-_-_-_\n')
    print('A continuación tiene las siguiente Tareas Pendientes:\n')

    dict_operaciones = {1:agregar_tarea,2:eliminar_tarea} #contiene las operaciones de agregar y eliminar tareas

    while True:
        tareas_pendientes = acceder_a_lista_de_tareas()
        index = 1 #sirve para enumerar las tareas
        for tarea in range(len(tareas_pendientes)): #imprime todas la tareas pendientes que hay
            print(f'{index}. {tareas_pendientes[tarea]}')
            index +=1
        print('\nOperaciones:\n1.Agregar nueva Tarea pendiente\t 2. Eliminar Tarea de la lista\t3. Salir del programa')

        try:
            operacion_elegida = int(input('Elija su opción: '))
            if operacion_elegida == 3: #Opción de salir
                break
            elif operacion_elegida in [1,2]: #primer y segunda opción
                dict_operaciones[operacion_elegida](tareas_pendientes)#agregar tarea/ eliminar tarea
            else:
                print('Esa opción no existe\n')

        except ValueError:
            print('Error: ingrese una opción valida\n')

        print('Tareas pendientes:\n') #esto se imprime cuando no se sale del programa

    print('El programa finalizó, ¡¡Adios!!')

menu_principal()
