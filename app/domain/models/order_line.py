from dataclasses import dataclass


@dataclass(frozen=True)
class OrderLine:
    order_id: int
    sku: str
    qty: int
