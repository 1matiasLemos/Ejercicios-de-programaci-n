from pydantic import BaseModel

class Venta(BaseModel):

    id: str | None
    id_client: str
    id_producto: str
    fecha_de_venta: str
    cantidad: int