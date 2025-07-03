import pytest
from tests.utils import make_batch_and_line
from pytest import FixtureRequest


@pytest.fixture()
def make_order(request: FixtureRequest):
    args = {**request.param}
    batch, order = make_batch_and_line(**args)
    return batch, order
