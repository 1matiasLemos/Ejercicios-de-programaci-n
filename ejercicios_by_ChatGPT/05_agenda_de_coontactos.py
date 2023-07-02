## Codigo de ChatGPT, pero el codigo no maneja excepciones
agenda = []

def agregar_contacto(nombre, telefono, direccion):
    # Crea un diccionario con la información del contacto
    contacto = {
        'nombre': nombre,
        'telefono': telefono,
        'direccion': direccion
    }
    # Agrega el contacto a la lista de contactos
    agenda.append(contacto)
    print(f'Contacto {nombre} agregado correctamente.')

def eliminar_contacto(nombre):
    for contacto in agenda:
        if contacto['nombre'] == nombre:
            agenda.remove(contacto)
            print(f'Contacto {nombre} eliminado correctamente.')
            return
    print(f'Contacto {nombre} no encontrado.')

def buscar_contacto(nombre):
    for contacto in agenda:
        if contacto['nombre'] == nombre:
            print('Información del contacto:')
            print(f'Nombre: {contacto["nombre"]}')
            print(f'Teléfono: {contacto["telefono"]}')
            print(f'Dirección: {contacto["direccion"]}')
            return
    print(f'Contacto {nombre} no encontrado.')

def mostrar_agenda():
    if len(agenda) == 0:
        print('La agenda de contactos está vacía.')
    else:
        print('Lista de contactos:')
        for contacto in agenda:
            print(f'Nombre: {contacto["nombre"]}')
            print(f'Teléfono: {contacto["telefono"]}')
            print(f'Dirección: {contacto["direccion"]}')
            print('---')

while True:
    print('--- Agenda de Contactos ---')
    print('1. Agregar contacto')
    print('2. Eliminar contacto')
    print('3. Buscar contacto')
    print('4. Mostrar agenda')
    print('0. Salir')
    opcion = input('Seleccione una opción: ')

    if opcion == '1':
        nombre = input('Ingrese el nombre del contacto: ')
        telefono = input('Ingrese el teléfono del contacto: ')
        direccion = input('Ingrese la dirección del contacto: ')
        agregar_contacto(nombre, telefono, direccion)
    elif opcion == '2':
        nombre = input('Ingrese el nombre del contacto a eliminar: ')
        eliminar_contacto(nombre)
    elif opcion == '3':
        nombre = input('Ingrese el nombre del contacto a buscar: ')
        buscar_contacto(nombre)
    elif opcion == '4':
        mostrar_agenda()
    elif opcion == '0':
        break
    else:
        print('Opción inválida. Intente nuevamente.')

print('Programa finalizado.')
