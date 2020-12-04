import pytest
from workshop.gilded_rose import GildedRose, Item
from workshop.libs.item_helpers import (
    decrease_quality,
    decrease_sell_in,
    increase_quality,
    item_has_expired,
)


def test_decrease_quality():
    item = Item(name="+5 Dexterity Vest", sell_in=10, quality=20)
    items = [item]
    gilded_rose = GildedRose(items)
    actual = decrease_quality(item)
    assert actual == 19


def test_increase_quality_max():
    item = Item(name="+5 Dexterity Vest", sell_in=10, quality=50)
    items = [item]
    gilded_rose = GildedRose(items)
    actual = increase_quality(item)
    assert actual == 50


def test_decrease_quality_zero_condition():
    item = Item(name="+5 Dexterity Vest", sell_in=10, quality=0)
    items = [item]
    gilded_rose = GildedRose(items)
    actual = decrease_quality(item)
    assert actual == 0
