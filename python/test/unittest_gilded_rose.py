import unittest

from src.gilded_rose import GildedRose
from src.item import Item

class GildedRoseUnitTest(unittest.TestCase):

    def test_update_items(self):
        item = Item(name="+5 Dexterity Vest", sell_in=10, quality=20)
        items = [item]
        gilded_rose = GildedRose(items)
        actual  = gilded_rose.update_items(item)
        assert(actual.quality == 19)
        assert(actual.sell_in== 9)

    def test_update_quality(self):
        item = Item(name="+5 Dexterity Vest", sell_in=10, quality=20)
        items = [item]
        gilded_rose = GildedRose(items)
        output_list = gilded_rose.update_quality()
        #bit dirty, but we know we have only one element, so we just take it.
        actual = output_list[0]
        assert(actual.quality == 19)
        assert(actual.sell_in== 9)

if __name__ == '__main__':
    unittest.main()
