import unittest

from src.gilded_rose import AgedBrie
from src.item import Item

class AgedBrieUnitTest(unittest.TestCase):

    def test_update_aged_brie(self):
        def run_brie_test(sell_in,quality):
            aged_brie_item = Item("Aged Brie", sell_in, quality)
            aged_brie = AgedBrie()
            return aged_brie.update(aged_brie_item)

        #for positive days.
        actual = run_brie_test(10,10)
        assert(actual.quality == 11)
        #for negative days.
        actual = run_brie_test(-10,10)
        assert(actual.quality == 12)



if __name__ == '__main__':
    unittest.main()
