'''import urllib.request

url = input('Ingrese su enlace: ') #se ingresa el link por 
                                                                        #terminacion .jpg, .png, .webp...
ubicacion = f"C:/Users/Matias/Desktop/{input('Nombre del archivo: ')}.{input('tipo de archivo: ')}"


try:
    urllib.request.urlretrieve(url, ubicacion)
    print("Descarga exitosa")
except urllib.error.URLError as e: #errores como 404,403, etc.
    print("Error al descargar el archivo:", e)
'''

## codigo por ChatGPT

import urllib.request

def descargar_archivo_desde_url(url, ruta_guardado):
    try:
        urllib.request.urlretrieve(url, ruta_guardado)
        print("Descarga exitosa. El archivo se ha guardado en:", ruta_guardado)
    except urllib.error.URLError as e:
        print("Error al descargar el archivo:", e)
    except Exception as e:
        print("Error inesperado:", e)

# Ejemplo de uso
url_usuario = input("Ingresa la URL del archivo a descargar: ")
ruta_guardado_usuario = input("Ingresa la ubicación donde deseas guardar el archivo: ")

descargar_archivo_desde_url(url_usuario, ruta_guardado_usuario)
