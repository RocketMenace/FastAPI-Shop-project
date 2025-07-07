from pydantic import BaseModel, Field, computed_field
from typing import Optional
from datetime import date
from app.schemas.order_line import OrderLine


class Batch(BaseModel):
    reference: str = Field(default=..., title="reference")
    sku: str = Field(default=..., title="sku")
    eta: Optional[date] = Field(default=..., title="eta")
    available_quantity: int = Field(default=..., title="available_quantity")
    purchased_quantity: int = Field(default=..., title="purchased_quantity")
    allocations: set[OrderLine] = Field(default=..., title="allocations")

    def allocate(self, line: OrderLine) -> None:
        if self.can_allocate(line):
            self.allocations.add(line)

    def deallocate(self, line: OrderLine):
        if line in self.allocations:
            self.allocations.remove(line)

    @computed_field
    @property
    def allocated_quantity(self):
        return sum(line.qty for line in self.allocations)

    @computed_field
    @property
    def available_quantity(self):
        return self.purchased_quantity - self.allocated_quantity

    def can_allocate(self, line: OrderLine) -> bool:
        return self.sku == line.sku and self.available_quantity >= line.qty
