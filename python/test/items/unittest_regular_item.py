import unittest

from items.regular_item import RegularItem
from src.item import Item

class RegularItemUnitTest(unittest.TestCase):

    def test_increase_quality(self):
        item = Item(name="+5 Dexterity Vest", sell_in=10, quality=20)
        regular_item = RegularItem()
        actual  = regular_item._increase_quality(item)
        assert(actual == 21)

    def test_decrease_quality(self):
        item = Item(name="+5 Dexterity Vest", sell_in=10, quality=20)
        regular_item = RegularItem()
        actual  = regular_item._decrease_quality(item)
        assert(actual == 19)

    def test_decrease_quality_leq_0(self):
        item = Item(name="+5 Dexterity Vest", sell_in=10, quality=0)
        regular_item = RegularItem()
        actual  = regular_item._decrease_quality(item)
        assert(actual == 0)

    def test_decrease_quality_geq_50(self):
        item = Item(name="+5 Dexterity Vest", sell_in=10, quality=50)
        regular_item = RegularItem()
        actual  = regular_item._increase_quality(item)
        assert(actual == 50)

    def test_run_regular_item(self):

        def run_regular_item(item):
            regular_item = RegularItem()
            return regular_item.update(item)

        #Run
        item1 = Item(name="+5 Dexterity Vest", sell_in=10, quality=20)
        actual = run_regular_item(item1)
        assert(actual.sell_in == 9)
        assert(actual.quality== 19)

        #Run for a second item. You can put this in a seperate test if you would prefer this.
        item2 = Item(name="Elixir of the Mongoose", sell_in=5, quality=7)
        actual = run_regular_item(item2)
        assert(actual.sell_in == 4)
        assert(actual.quality == 6)

if __name__ == '__main__':
    unittest.main()
