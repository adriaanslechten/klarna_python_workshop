from workshop.gilded_rose import GildedRose, Item
import pytest


@pytest.fixture()
def items_day_zero():
    return [
        Item(name="+5 Dexterity Vest", sell_in=10, quality=20),
        Item(name="Aged Brie", sell_in=2, quality=0),
        Item(name="Elixir of the Mongoose", sell_in=5, quality=7),
        Item(name="Sulfuras, Hand of Ragnaros", sell_in=0, quality=80),
        Item(name="Sulfuras, Hand of Ragnaros", sell_in=-1, quality=80),
        Item(
            name="Backstage passes to a TAFKAL80ETC concert",
            sell_in=15,
            quality=20,
        ),
        Item(
            name="Backstage passes to a TAFKAL80ETC concert",
            sell_in=10,
            quality=49,
        ),
        Item(
            name="Backstage passes to a TAFKAL80ETC concert",
            sell_in=5,
            quality=49,
        ),
        Item(name="Conjured Mana Cake", sell_in=3, quality=6),
    ]


def update_quality_wrapper(day, gilded_rose):
    for day in range(0, day):
        gilded_rose.update_quality()


def test_day_one(items_day_zero):
    gilded_rose = GildedRose(items_day_zero)
    update_quality_wrapper(1, gilded_rose)
    assert gilded_rose.items == [
        Item(name="+5 Dexterity Vest", sell_in=9, quality=19),
        Item(name="Aged Brie", sell_in=1, quality=1),
        Item(name="Elixir of the Mongoose", sell_in=4, quality=6),
        Item(name="Sulfuras, Hand of Ragnaros", sell_in=0, quality=80),
        Item(name="Sulfuras, Hand of Ragnaros", sell_in=-1, quality=80),
        Item(
            name="Backstage passes to a TAFKAL80ETC concert",
            sell_in=14,
            quality=21,
        ),
        Item(
            name="Backstage passes to a TAFKAL80ETC concert",
            sell_in=9,
            quality=50,
        ),
        Item(
            name="Backstage passes to a TAFKAL80ETC concert",
            sell_in=4,
            quality=50,
        ),
        Item(name="Conjured Mana Cake", sell_in=2, quality=4),
    ]


def test_day_two(items_day_zero):
    gilded_rose = GildedRose(items_day_zero)
    update_quality_wrapper(2, gilded_rose)
    assert gilded_rose.items == [
        Item(name="+5 Dexterity Vest", sell_in=8, quality=18),
        Item(name="Aged Brie", sell_in=0, quality=2),
        Item(name="Elixir of the Mongoose", sell_in=3, quality=5),
        Item(name="Sulfuras, Hand of Ragnaros", sell_in=0, quality=80),
        Item(name="Sulfuras, Hand of Ragnaros", sell_in=-1, quality=80),
        Item(
            name="Backstage passes to a TAFKAL80ETC concert",
            sell_in=13,
            quality=22,
        ),
        Item(
            name="Backstage passes to a TAFKAL80ETC concert",
            sell_in=8,
            quality=50,
        ),
        Item(
            name="Backstage passes to a TAFKAL80ETC concert",
            sell_in=3,
            quality=50,
        ),
        Item(name="Conjured Mana Cake", sell_in=1, quality=2),
    ]


def test_day_ten(items_day_zero):
    gilded_rose = GildedRose(items_day_zero)
    update_quality_wrapper(10, gilded_rose)
    assert gilded_rose.items == [
        Item(name="+5 Dexterity Vest", sell_in=0, quality=10),
        Item(name="Aged Brie", sell_in=-8, quality=18),
        Item(name="Elixir of the Mongoose", sell_in=-5, quality=0),
        Item(name="Sulfuras, Hand of Ragnaros", sell_in=0, quality=80),
        Item(name="Sulfuras, Hand of Ragnaros", sell_in=-1, quality=80),
        Item(
            name="Backstage passes to a TAFKAL80ETC concert",
            sell_in=5,
            quality=35,
        ),
        Item(
            name="Backstage passes to a TAFKAL80ETC concert",
            sell_in=0,
            quality=50,
        ),
        Item(
            name="Backstage passes to a TAFKAL80ETC concert",
            sell_in=-5,
            quality=0,
        ),
        Item(name="Conjured Mana Cake", sell_in=-7, quality=0),
    ]


def test_day_twentyitems_day_zero(items_day_zero):
    gilded_rose = GildedRose(items_day_zero)
    update_quality_wrapper(20, gilded_rose)
    assert gilded_rose.items == [
        Item(name="+5 Dexterity Vest", sell_in=-10, quality=0),
        Item(name="Aged Brie", sell_in=-18, quality=38),
        Item(name="Elixir of the Mongoose", sell_in=-15, quality=0),
        Item(name="Sulfuras, Hand of Ragnaros", sell_in=0, quality=80),
        Item(name="Sulfuras, Hand of Ragnaros", sell_in=-1, quality=80),
        Item(
            name="Backstage passes to a TAFKAL80ETC concert",
            sell_in=-5,
            quality=0,
        ),
        Item(
            name="Backstage passes to a TAFKAL80ETC concert",
            sell_in=-10,
            quality=0,
        ),
        Item(
            name="Backstage passes to a TAFKAL80ETC concert",
            sell_in=-15,
            quality=0,
        ),
        Item(name="Conjured Mana Cake", sell_in=-17, quality=0),
    ]
