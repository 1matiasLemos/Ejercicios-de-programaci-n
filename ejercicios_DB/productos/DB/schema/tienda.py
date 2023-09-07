def tienda_schema(producto) -> dict:    
    return {
        'id':str(producto['_id']),
        'nombre': producto['nombre'],
        'precio':producto['precio'],
        'cantidad_de_stock':producto['cantidad_de_stock'],
        'marca': producto['marca']
    }


def productos_schema(productos) -> list:

     return [tienda_schema(producto) for producto in productos]