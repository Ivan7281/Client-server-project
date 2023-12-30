from typing import List, Optional

from pydantic import BaseModel, Field, UUID4, PositiveInt

class ProductCreate(BaseModel):
    name: str
    description: str
    price: float

class OrderItemCreate(BaseModel):
    product_id: UUID4
    quantity: PositiveInt

class OrderCreate(BaseModel):
    items: List[OrderItemCreate]
