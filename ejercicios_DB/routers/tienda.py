from fastapi import APIRouter, status, HTTPException
from productos.DB.models.tienda import Tienda
from productos.DB.client import db_client
from productos.DB.schema.tienda import tienda_schema, productos_schema
from bson import ObjectId


router = APIRouter(prefix='/tienda')

@router.get('/{id}')
async def product(id:str):
    return search_producto_by_id(id)

@router.get('/',response_model=list[Tienda])
async def product(): #retorna una lista con todos los productos
    return productos_schema(db_client.tienda.find())


@router.post('/',status_code=status.HTTP_201_CREATED,response_model=Tienda)
async def agregar_producto(nuevo_producto: Tienda):

    tienda_dict = dict(nuevo_producto)
    del tienda_dict['id']

    if type(search_product(tienda_dict)) == Tienda:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='El producto ya fue registrado')

    new_id = db_client.tienda.insert_one(tienda_dict).inserted_id

    new_product = tienda_schema(db_client.tienda.find_one({'_id':new_id}))

    return Tienda(**new_product)


def search_product(producto: dict):

    parametros_de_busqueda = {'nombre':producto['nombre'],'marca':producto['marca']}
    try:
        for k, v in parametros_de_busqueda.items(): #busca si el nombre, marca y tamaño existen 
            if not db_client.tienda.find_one({k:v}): #en el momento que no encuentre nada, lanza la Exception
                raise Exception

        producto_by_name = db_client.tienda.find_one({'nombre':producto['nombre']})  #si no hubo una Exception, retorna el producto 

        return Tienda(**tienda_schema(producto_by_name)) 
    
    except:
        return {'error': 'producto no encontrado'}
    

def search_producto_by_id(id:str):
    try:
        product = db_client.tienda.find_one({'_id':ObjectId(id)})
        return Tienda(**tienda_schema(product))
    except:
        return {'error':'El producto no fue encontrado'}
    

@router.put('/',status_code=status.HTTP_202_ACCEPTED, response_model=Tienda)
async def actualizar_products(producto: Tienda):

    producto_dict = dict(producto)
    del producto_dict['id']

    try:
        found = db_client.tienda.find_one_and_replace({'_id':ObjectId(producto.id)},producto_dict)
    except:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                             detail={'error':'No se ha actualizado es usuario'}) 
    
    return search_producto_by_id(producto.id)


@router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT)
async def delete(id:str):
    found = db_client.tienda.find_one_and_delete({'_id':ObjectId(id)})

    if found:
        return {'error':'no se ha eliminado el producto'}