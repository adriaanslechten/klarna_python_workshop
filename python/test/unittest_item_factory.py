import unittest

from src.item_factory import ItemFactory
from src.item import Item
from src.items.regular_item import RegularItem
from src.items.aged_brie import AgedBrie

class ItemFactoryUnitTest(unittest.TestCase):

    def test_create_regular_item(self):
        item = Item(name="+5 Dexterity Vest", sell_in=10, quality=20)
        item_factory = ItemFactory()
        outcome = item_factory.create_item_type(item)
        assert(isinstance(outcome,RegularItem))

    def test_create_regular_item(self):
        item = Item(name="Aged Brie", sell_in=2, quality=0)
        item_factory = ItemFactory()
        outcome = item_factory.create_item_type(item)
        assert(isinstance(outcome,AgedBrie))


if __name__ == '__main__':
    unittest.main()
