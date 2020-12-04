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
