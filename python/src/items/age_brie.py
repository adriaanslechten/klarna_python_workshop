
from src.items.regular_item import RegularItem

class AgedBrie(RegularItem):

    def update_aged_brie(self, aged_brie):
        """
        Helper function to update the aged brie.
        :param aged_brie: input item. (aged brie)
        :return: updated aged brie.
        """
        aged_brie.quality = self.increase_quality(aged_brie)
        aged_brie.sell_in = aged_brie.sell_in - 1
        if aged_brie.sell_in < 0:
            aged_brie.quality = self.increase_quality(aged_brie)
        return aged_brie

