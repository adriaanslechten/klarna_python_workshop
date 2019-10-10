
class AgedBrie(object):

    def decrease_quality(self, item):
        """
        Helper function to increase the quality.
        :param item: item which we want tod descrease
        :return: integer, containing the quality minus one
        """
        if item.quality > 0:
            return item.quality - 1
        else:
            return item.quality

    def increase_quality(self, item):
        """
        Helper function to increase the quality.
        :param item: item which we want to increase
        :return: integer, containing the quality plus one
        """
        if item.quality < 50:
            return item.quality + 1
        else:
            return item.quality


    def item_has_expired(self,item):
        """
        Helper funciton to check if the item is expired
        :param item: item to check
        :return: boolean, if it's expired or not.
        """
        if item.sell_in < 0:
            return True
        else:
            return False

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

