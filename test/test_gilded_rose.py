import pytest
from workshop.gilded_rose import Item, GildedRose


def test_foo():
    items = [Item("foo", 0, 0)]
    gilded_rose = GildedRose(items)
    gilded_rose.update_quality()
    assert "foo" == items[0].name


def test_increase_quality():
    item = Item(name="+5 Dexterity Vest", sell_in=10, quality=20)
    items = [item]
    gilded_rose = GildedRose(items)
    actual = gilded_rose.increase_quality(item)
    assert actual == 21


def test_increase_quality_max():
    item = Item(name="+5 Dexterity Vest", sell_in=10, quality=50)
    items = [item]
    gilded_rose = GildedRose(items)
    actual = gilded_rose.increase_quality(item)
    assert actual == 50


def test_decrease_quality():
    item = Item(name="+5 Dexterity Vest", sell_in=10, quality=20)
    items = [item]
    gilded_rose = GildedRose(items)
    actual = gilded_rose.decrease_quality(item)
    assert actual == 19


def test_decrease_quality_zero_condition():
    item = Item(name="+5 Dexterity Vest", sell_in=10, quality=0)
    items = [item]
    gilded_rose = GildedRose(items)
    actual = gilded_rose.decrease_quality(item)
    assert actual == 0


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
