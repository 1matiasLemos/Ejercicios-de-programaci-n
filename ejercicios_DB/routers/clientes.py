from fastapi import APIRouter, HTTPException, status
from clientes.DB.models.client import Client
from clientes.client import db_client
from clientes.DB.schema.cliente import schema_cliente, schema_clientes
from bson import ObjectId
from datetime import date, datetime, timedelta
from re import match, findall

router = APIRouter(prefix='/clientes',
                    tags=['clientes'],
                    responses={status.HTTP_404_NOT_FOUND:{'message':'No encontrado'}})


@router.get('/',response_model=list[Client]) #devuelve una lista
async def client():
    return schema_clientes(db_client.clientes.find()) #find busca y retorna todo; users_schema 

#ultimos 30 dias
@router.get('/last_30_days',response_model=list[Client])
async def client():

    list_30_days: list = []
    convertir_to_date = lambda date_str: [int(i) for i in findall(r'\d+', date_str['registration_date'])]

    for client in schema_clientes(db_client.clientes.find()) :
        y, m, d = convertir_to_date(client) #retorna year, month y day como int
        date_:date = date(y,m,d) 
        
        if (datetime.now().date() - date_).days < 30: #resta la fecha actual con la fecha de client
            list_30_days.append(client) #si la diferencia de dias entre fechas fue de 30 dias o menos, la agregamos el client a la lista
    
    return list_30_days #retorna la lista de clientes que se registraron entre la fecha actual a 30 dias atrás
 

#Path
@router.get('/{id}')
async def client(id:str):     
    return search_client('_id',ObjectId(id)) 

#Query
@router.get('/client/') #http://127.0.0.1:8000/userquery/?id=3
async def user(id:str): 
    return search_client('_id',ObjectId(id))


#POST: agrega nuevos datos

@router.post('/',status_code=status.HTTP_201_CREATED, response_model=Client)
async def user(cliente: Client): 

    exception = HTTPException(status_code=status.HTTP_406_NOT_ACCEPTABLE,
                                detail='formato de fecha inválido')

    if type(search_client('email',cliente.email)) == Client: 
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='este usuario ya existe')
        
    verify_format_date(cliente.registration_date)
        
    cliente_dict = dict(cliente)
    del cliente_dict['id']

    id = db_client.clientes.insert_one(cliente_dict).inserted_id #asigna un id
    new_client = schema_cliente(db_client.clientes.find_one({'_id':ObjectId(id)})) #busca por la id creada

    return Client(**new_client) #retorna el Client
  

def verify_format_date(fecha_str:str):
        
        exception = HTTPException(status_code=status.HTTP_406_NOT_ACCEPTABLE,
                                detail='formato de fecha inválido')
        
        if match(r'^\d{4}\-\d{1,2}\-\d{1,2}$', fecha_str): #verifica que la fecha esté bien estructurada y sea anterior

            y, m, d = [int(i) for i in findall(r'\d+', fecha_str)] #separa el ano, mes y dia
            
            try:
                fecha = date(y,m,d)

                if fecha > datetime.now().date(): #verifica que la fecha sea anterior a la actual
                    raise exception
                
                return True
            except:
                raise exception
        else:
            raise exception


def search_client(field:str, key): #busca de manera generica 

    try:
        cliente = db_client.clientes.find_one({field:key}) #busca en la base de datos usando los args y retorna el usuario

        return Client(**schema_cliente(cliente)) #convertimos el user en un dict con el esquema que contien user_schema; lo retorna como un obj User
    
    except:
        return {'error':'No se ha encontrado el usuario'}


#PUT: actualiza datos 

@router.put('/',status_code=status.HTTP_202_ACCEPTED,response_model=Client)
async def client(cliente: Client): #arg: json

    cliente_dict = dict(cliente) 
    del cliente_dict['id'] #eliminamos el id porque no lo vamos a reemplazar

    try:
        found = db_client.clientes.find_one_and_replace({'_id':ObjectId(cliente.id)},cliente_dict)
    except:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail={'error':'No se ha actualizado es usuario'})
    
    return search_client('_id',ObjectId(cliente.id))



# Delete: elimina datos
@router.delete('/{id}',status_code=status.HTTP_204_NO_CONTENT)
async def delete(id:str):

    found = db_client.clientes.find_one_and_delete({'_id':ObjectId(id)})

    if found:
        return {'error':'no se ha eliminado el usuario'}

