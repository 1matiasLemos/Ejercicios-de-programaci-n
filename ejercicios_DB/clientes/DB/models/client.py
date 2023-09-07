from pydantic import BaseModel

class Client(BaseModel):

    id: str | None
    name: str
    email: str
    registration_date: str