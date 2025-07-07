from pydantic import BaseModel, Field, computed_field
from typing import Optional, Set
from datetime import date
from app.api.schemas.order_line import OrderLine


class Batch(BaseModel):
    reference: str = Field(default=..., title="reference")
    sku: str = Field(default=..., title="sku")
    eta: Optional[date] = Field(default=..., title="eta")
    purchased_quantity: int = Field(default=..., title="purchased_quantity")
    allocations: Set[OrderLine] = Field(default=..., title="allocations")
