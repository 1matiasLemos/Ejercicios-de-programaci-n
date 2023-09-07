from fastapi import FastAPI
from routers import tienda, clientes, prueba, ventas

app = FastAPI()

app.include_router(tienda.router)
app.include_router(clientes.router)
app.include_router(prueba.router)
app.include_router(ventas.router)


@app.get('/')
async def inicio():
    return 'Ruta por defecto de los ejecicios DB'


