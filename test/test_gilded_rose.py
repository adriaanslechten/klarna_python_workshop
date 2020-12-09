import pytest
from workshop.gilded_rose import AgedBrie, Backstage, GildedRose
from workshop.items.items import Item
from workshop.libs.item_helpers import (decrease_quality, decrease_sell_in,
                                        increase_quality, item_has_expired)


@pytest.mark.parametrize(
    "sell_in, quality, result",
    [
        (10, 10, 11),
        (-10, 10, 12),
    ],
)
def test_update_aged_brie(sell_in, quality, result):
    aged_brie = Item("Aged Brie", sell_in, quality)
    assert AgedBrie().update_aged_brie(aged_brie) == result


@pytest.mark.parametrize(
    "sell_in, quality, result",
    [
        (10, 10, 12),
        (-1, 20, 0),
    ],
)
def test_update_backstage(sell_in, quality, result):
    backstage_ticket = Item(
        "Backstage passes to a TAFKAL80ETC concert", sell_in, quality
    )

    assert Backstage().update_backstage(backstage_ticket) == result

def test_gildedrose():
    items_a = [Item("Aged Brie", 10, 10), Item("Even more Aged Brie", 5, 5)]
    items_b = [Item("Aged Brie", 10, 10), Item("Even more Aged Brie", 5, 5)]
    items_c = [Item("Ragnaros", 2, 2), Item("Backstage", 4, 4)]
    assert items_a == items_b
    assert items_a != items_c
