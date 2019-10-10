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

    def test_update_aged_brie(self):
        def run_brie_test(sell_in,quality):
            aged_brie = Item("Aged Brie", sell_in, quality)
            items = [aged_brie]
            gilded_rose = GildedRose(items)
            return gilded_rose.update_aged_brie(aged_brie)

        #for positive days.
        actual = run_brie_test(10,10)
        assert(actual.quality == 11)
        #for negative days.
        actual = run_brie_test(-10,10)
        assert(actual.quality == 12)

    def test_update_backstage(self):
        def run_backstage_test(sellin,quantity):
            backstage_ticket = Item("Backstage passes to a TAFKAL80ETC concert", sellin, quantity)
            items  = [backstage_ticket]
            gilded_rose = GildedRose(items)
            return gilded_rose.update_backstageticket_quality(backstage_ticket)

        actual = run_backstage_test(10,10)
        print(actual)
        assert(actual == 11)
        actual = run_backstage_test(-1,20)
        assert(actual == 0)



if __name__ == '__main__':
    unittest.main()
