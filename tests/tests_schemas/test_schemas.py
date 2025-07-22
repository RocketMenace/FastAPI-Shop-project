import pytest
from tests.conftest import make_order
from app.schemas.batch import Batch
from app.schemas.order_line import OrderLine


@pytest.mark.parametrize(
    "make_order",
    [{"sku": "ELEGANT-LAMP", "order_id": 1, "batch_qty": 20, "line_qty": 2}],
    indirect=True,
)
def test_can_allocate_if_available_smaller_than_required(make_order):
    large_batch, small_line = make_order
    assert large_batch.can_allocate(small_line)

@pytest.mark.parametrize(
    "make_order",
    [{"sku": "ELEGANT-LAMP", "order_id": 1, "batch_qty": 2, "line_qty": 20}],
    indirect=True
)
def test_cannot_allocate_if_available_less_than_required(make_order):
    small_batch, large_line = make_order
    assert small_batch.can_allocate(large_line) is False

@pytest.mark.parametrize(
    "make_order",
    [{"sku":"ELEGANT-LAMP", "order_id": 1, "batch_qty": 2, "line_qty": 2}],
    indirect=True
)
def test_can_allocate_if_available_equal_required(make_order):
    batch, line = make_order
    assert batch.can_allocate(line)


def test_cannot_allocate_if_skus_do_not_match():
    batch = Batch(reference="batch-001", sku="UNCOMFORTABLE-CHAIR", available_quantity=100, eta=None)
    line = OrderLine(order_id=4, sku="EXPENSIVE-TOASTER",   qty=10)
    assert batch.can_allocate(line) is False