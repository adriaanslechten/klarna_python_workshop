from src.items.parent_item import ParentItem


class RegularItem(ParentItem):

    @staticmethod
    def _decrease_quality(item):
        """
        Helper function to increase the quality.
        :param item: item which we want tod descrease
        :return: integer, containing the quality minus one
        """
        if item.quality > 0:
            return item.quality - 1
        else:
            return item.quality

    @staticmethod
    def _increase_quality(item):
        """
        Helper function to increase the quality.
        :param item: item which we want to increase
        :return: integer, containing the quality plus one
        """
        if item.quality < 50:
            return item.quality + 1
        else:
            return item.quality

    @staticmethod
    def _item_has_expired(item):
        """
        Helper funciton to check if the item is expired
        :param item: item to check
        :return: boolean, if it's expired or not.
        """
        if item.sell_in < 0:
            return True
        else:
            return False

    def update(self, item):
        """
        Helper function to update the other items
        :param item: input item.
        :return: updated item.
        """
        item.quality = self._decrease_quality(item)
        item.sell_in = item.sell_in - 1
        if self._item_has_expired(item):
            item.quality = self._decrease_quality(item)
        return item
