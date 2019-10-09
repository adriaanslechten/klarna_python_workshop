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




if __name__ == '__main__':
    unittest.main()
