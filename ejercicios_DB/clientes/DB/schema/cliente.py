
def schema_cliente(cliente: dict):
    return {
        'id': str(cliente['_id']),
        'name': cliente['name'],
        'email':cliente['email'],
        'registration_date':cliente['registration_date']
    }

def schema_clientes(clientes)-> list:
     return [schema_cliente(client) for client in clientes]