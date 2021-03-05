import pytest
from workshop.gilded_rose import GildedRose
from workshop.item import  Item
from workshop.libs.item_helpers import (
    decrease_quality,
    decrease_sell_in,
    increase_quality,
    item_has_expired,
)


@pytest.mark.parametrize(
    "sell_in, quality, result",
    [
        (10, 10, 11),
        (-10, 10, 12),
    ],
)
def test_update_aged_brie(sell_in, quality, result):
    aged_brie = Item("Aged Brie", sell_in, quality)
    gilded_rose = GildedRose([aged_brie])
    assert gilded_rose.update_aged_brie(aged_brie) == result


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
    gilded_rose = GildedRose([backstage_ticket])
    assert gilded_rose.update_backstage(backstage_ticket) == result
