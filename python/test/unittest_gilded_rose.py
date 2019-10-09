import unittest

from src.gilded_rose import Item, GildedRose

class GildedRoseUnitTest(unittest.TestCase):

    def test_increase_quality(self):
        item = Item(name="+5 Dexterity Vest", sell_in=10, quality=20)
        items = [item]
        gilded_rose = GildedRose(items)
        actual  = gilded_rose.increase_quality(item)
        assert(actual == 21)

    def test_decrease_quality(self):
        item = Item(name="+5 Dexterity Vest", sell_in=10, quality=20)
        items = [item]
        gilded_rose = GildedRose(items)
        actual  = gilded_rose.decrease_quality(item)
        assert(actual == 19)

    def test_decrease_quality_leq_0(self):
        item = Item(name="+5 Dexterity Vest", sell_in=10, quality=0)
        items = [item]
        gilded_rose = GildedRose(items)
        actual  = gilded_rose.decrease_quality(item)
        assert(actual == 0)

    def test_decrease_quality_geq_50(self):
        item = Item(name="+5 Dexterity Vest", sell_in=10, quality=50)
        items = [item]
        gilded_rose = GildedRose(items)
        actual  = gilded_rose.increase_quality(item)
        assert(actual == 50)



if __name__ == '__main__':
    unittest.main()
