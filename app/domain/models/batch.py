from dataclasses import dataclass
from typing import Optional, Set
from datetime import date
from .order_line import OrderLine


@dataclass(frozen=True)
class Batch:
    reference: str
    sku: str
    eta: Optional[date]
    purchased_quantity: int
    allocations: Set[OrderLine]

    def allocate(self, line: OrderLine) -> None:
        if self.can_allocate(line):
            self.allocations.add(line)

    def deallocate(self, line: OrderLine):
        if line in self.allocations:
            self.allocations.remove(line)

    @property
    def allocated_quantity(self) -> int:
        return sum(line.qty for line in self.allocations)

    @property
    def available_quantity(self) -> int:
        return self.purchased_quantity - self.allocated_quantity

    def can_allocate(self, line: OrderLine) -> bool:
        return self.sku == line.sku and self.purchased_quantity >= line.qty
