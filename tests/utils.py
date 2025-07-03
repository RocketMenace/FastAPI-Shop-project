from app.schemas.batch import Batch
from app.schemas.order_line import OrderLine
from datetime import date


def make_batch_and_line(sku: str, batch_qty: int, order_id: int, line_qty: int):
    return (
        Batch(reference="batch-001", sku=sku, available_quantity=batch_qty, eta=date.today()),
        OrderLine(order_id=order_id, sku=sku, qty=line_qty),
    )
