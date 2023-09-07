from pydantic import BaseModel

class Tienda(BaseModel):
    
    id : str | None
    nombre: str
    precio: int
    cantidad_de_stock: int
    marca: str
