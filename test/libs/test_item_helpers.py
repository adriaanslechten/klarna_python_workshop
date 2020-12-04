import pytest
from workshop.gilded_rose import GildedRose
from workshop.items.items import Item
from workshop.libs.item_helpers import (
    decrease_quality,
    decrease_sell_in,
    increase_quality,
    item_has_expired,
)


@pytest.mark.parametrize(
    "item, result",
    [
        (Item(name="+5 Dexterity Vest", sell_in=10, quality=20), 19),
        (Item(name="+5 Dexterity Vest", sell_in=10, quality=0), 0),
    ],
)
def test_decrease_quality(item, result):
    assert decrease_quality(item) == result


@pytest.mark.parametrize(
    "item, result",
    [
        (Item(name="+5 Dexterity Vest", sell_in=10, quality=49), 50),
        (Item(name="+5 Dexterity Vest", sell_in=10, quality=50), 50),
    ],
)
def test_increase_quality_max(item, result):
    assert increase_quality(item) == result


@pytest.mark.parametrize(
    "item, result",
    [
        (Item(name="+5 Dexterity Vest", sell_in=-10, quality=50), True),
        (Item(name="+5 Dexterity Vest", sell_in=10, quality=50), False),
    ],
)
def test_item_has_expired(item, result):
    assert item_has_expired(item) == result
