from pydantic import BaseModel


# Define your data models here
class Item(BaseModel):
    name: str
    description: str = None
    price: float
    tax: float = None