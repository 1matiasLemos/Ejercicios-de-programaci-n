
def schema_venta(venta:dict):
    return {
        'id': str(venta['_id']),
        'id_client': venta['id_client'],
        'id_producto':venta['id_producto'],
        'fecha_de_venta':venta['fecha_de_venta'],
        'cantidad': venta['cantidad']
    }
def schema_ventas(ventas):
    
    return [schema_venta(venta) for venta in ventas]