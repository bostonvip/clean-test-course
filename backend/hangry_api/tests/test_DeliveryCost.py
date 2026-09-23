from types import SimpleNamespace

import pytest

from api.controllers import Delivery


def make_order(*quantities):
    """Create order items with only the attribute Delivery needs."""
    return [SimpleNamespace(quantity=quantity) for quantity in quantities]


@pytest.mark.parametrize(
    ("quantities", "distance", "expected_cost"),
    [
        pytest.param((), 10, 4.0, id="empty-order"),
        pytest.param((3, 1), 2, 4.0, id="small-order"),
        pytest.param((3, 3), 4, 5, id="medium-order"),
        pytest.param((5, 6), 6, 7.5, id="large-order"),
        pytest.param((0,), 6, 4.0, id="zero-quantity"),
        pytest.param((5, 6), 0, 4.0, id="zero-distance"),
        pytest.param((5,), 6, 4.0, id="long-distance-small-order"),
        pytest.param((5, 6), 3, 4.0, id="large-order-short-distance"),
        pytest.param((5,), 4, 4.0, id="medium-quantity-boundary"),
        pytest.param((3, 3), 3, 4.0, id="medium-distance-boundary"),
        pytest.param((4, 6), 6, 5, id="large-quantity-boundary"),
        pytest.param((5, 6), 5, 5, id="large-distance-boundary"),
    ],
)
def test_calculate_returns_expected_delivery_cost(
    quantities, distance, expected_cost
):
    order = make_order(*quantities)

    assert Delivery.calculate(order, distance) == expected_cost


def test_calculate_uses_the_sum_of_item_quantities():
    order = make_order(2, 2, 2)

    assert Delivery.calculate(order, 4) == 5
