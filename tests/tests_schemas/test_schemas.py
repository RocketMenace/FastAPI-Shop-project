import pytest
from tests.conftest import make_order


@pytest.mark.parametrize(
    "make_order",
    [{"sku": "ELEGANT-LAMP", "order_id": 1, "batch_qty": 20, "line_qty": 2}],
    indirect=True,
)
def test_can_allocate_if_available_smaller_than_required(make_order):
    large_batch, small_line = make_order
    assert large_batch.can_allocate(small_line)
