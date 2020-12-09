import pytest
from workshop.items.items import Item


def test_item():
    item_a = Item("Aged Brie", 10, 10)
    item_b = Item("Aged Brie", 10, 10)
    item_c = Item("Even more Aged Brie", 5, 5)
    assert item_a == item_b
    assert item_a != item_c
