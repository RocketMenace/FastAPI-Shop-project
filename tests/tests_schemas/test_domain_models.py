import pytest

from tests.conftest import make_order
from app.domain.models.batch import Batch
from app.domain.models.order_line import OrderLine


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
    indirect=True,
)
def test_cannot_allocate_if_available_less_than_required(make_order):
    small_batch, large_line = make_order
    assert small_batch.can_allocate(large_line) is False


@pytest.mark.parametrize(
    "make_order",
    [{"sku": "ELEGANT-LAMP", "order_id": 1, "batch_qty": 2, "line_qty": 2}],
    indirect=True,
)
def test_can_allocate_if_available_equal_required(make_order):
    batch, line = make_order
    assert batch.can_allocate(line)


def test_cannot_allocate_if_skus_do_not_match():
    batch = Batch(
        reference="batch-001",
        sku="UNCOMFORTABLE-CHAIR",
        purchased_quantity=100,
        eta=None,
        allocations=set(),
    )
    line = OrderLine(order_id=4, sku="EXPENSIVE-TOASTER", qty=10)
    assert batch.can_allocate(line) is False


@pytest.mark.parametrize(
    "make_order",
    [{"sku": "DECORATIVE-TRINKET", "order_id": 2, "batch_qty": 20, "line_qty": 2}],
    indirect=True,
)
def test_can_only_deallocate_allocated_lines(make_order):
    batch, unallocated_line = make_order
    batch.deallocate(unallocated_line)
    assert batch.available_quantity == 20


@pytest.mark.parametrize(
    "make_order",
    [{"sku": "ANGULAR-DESK", "order_id": 3, "batch_qty": 20, "line_qty": 2}],
    indirect=True,
)
def test_allocations_is_idempotent(make_order):
    batch, line = make_order
    batch.allocate(line)
    batch.allocate(line)
    assert batch.available_quantity == 18
