from fastapi import APIRouter, HTTPException, status
from ventas.venta import db_client
from ventas.DB.models.venta import Venta
from ventas.DB.schema.venta import schema_venta, schema_ventas
from routers.tienda import productos_schema
from routers.clientes import verify_format_date, schema_clientes
from bson import ObjectId

router = APIRouter(prefix='/ventas',
                   tags=['Ventas'],)

@router.get('/',response_model= list[Venta])
async def get():
    return schema_ventas(db_client.ventas.find())

@router.post('/agregar_venta', status_code=status.HTTP_201_CREATED, response_model=Venta)
async def venta(venta: Venta):

    venta_found = search_venta(dict(venta)) #si exite alguna venta con el cliente, producto  y fecha iguales, retorna esa venta como dict

    if type(venta_found) == dict:

        verify_format_date(venta.fecha_de_venta)
        actualizar_stock(venta.id_producto,venta.cantidad)

        venta_found['cantidad'] = venta_found['cantidad'] + venta.cantidad
        
        id = venta_found['id']
        del venta_found['id']

        db_client.ventas.find_one_and_replace({'_id':ObjectId(id)}, venta_found)

        return search_venta_by_id(id)

    verify_format_date(venta.fecha_de_venta)

    dict_venta = dict(venta)
    del dict_venta['id']

    actualizar_stock(dict_venta['id_producto'],dict_venta['cantidad'])
    
    id = db_client.ventas.insert_one(dict_venta).inserted_id
    new_venta = db_client.ventas.find_one({'_id':ObjectId(id)})
    

    return Venta(**schema_venta(new_venta))




def search_venta(datos: dict):

    #Consultamos en la base de datos todos los clientes y guardamos sus id
    id_clientes =  [i['id'] for i in schema_clientes(db_client.clientes.find())]
    #Lo mismo con los productos
    productos =  [i['id'] for i in productos_schema(db_client.tienda.find())]


    if datos['id_client'] in id_clientes: #si el id_client ingresado es valido
        
        if datos['id_producto'] in productos: #si el id_producto está entre las id de todos los produtos 

        
            #retorna una lista de todas las ventas registradas que contengan la misma id del producto
            ventas_by_product = schema_ventas(db_client.ventas.find({'id_producto':datos['id_producto']}))

            #filtra entre esas ventas encontradas, a las que contengn la misma id_client
            client = list(filter(lambda venta: venta['id_client'] == datos['id_client'],ventas_by_product))

            #filta entre esas ventas con el mismo id_producto e id_client a aquella unica que la fecha sea igual a la fecha ingresada
            client = list(filter(lambda venta: venta['fecha_de_venta'] == datos['fecha_de_venta'],client))

            if client == []: #si no se encontró similitudes y esta vacio
                return False        
            
            return client[0]
      
            
        else:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                                detail={'error':'id del producto no encontrada'})
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail={'error':'id del cliente no encontrada'})

def search_venta_by_id(id:str):

    try:

        venta = db_client.ventas.find_one({'_id':ObjectId(id)})
        return Venta(**schema_venta(venta))

    except:
        return {'error':'venta no encontrada'}

## Delete
@router.delete('/{id}',status_code=status.HTTP_204_NO_CONTENT)
async def delete(id:str):

    found = db_client.ventas.find_one_and_delete({'_id':ObjectId(id)})

    if found == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail= {'error':'venta no encontrada'})
    

def actualizar_stock(id_producto:str,cantidad_comprada:int):

    found_product = dict(db_client.tienda.find_one({'_id':ObjectId(id_producto)}))
    
    found_product['cantidad_de_stock'] = found_product['cantidad_de_stock'] - cantidad_comprada
    del found_product['_id']

    db_client.tienda.find_one_and_replace({'_id':ObjectId(id_producto)},found_product)