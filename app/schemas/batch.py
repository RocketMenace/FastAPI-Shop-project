from pydantic import BaseModel, Field, computed_field
from typing import Optional
from datetime import date
from app.schemas.order_line import OrderLine


class Batch(BaseModel):
    reference: str = Field(default=..., title="reference")
    sku: str = Field(default=..., title="sku")
    eta: Optional[date] = Field(default=..., title="eta")
    available_quantity: int = Field(default=..., title="available_quantity")

    def allocate(self, line: OrderLine) -> int:
        self.available_quantity -= line.qty
        return self.available_quantity


if __name__ == "__main__":
    batch = Batch(reference="q", sku="q", available_quantity=4)
    print(batch)
