from src.item_factory import ItemFactory

"""
Main run function.
"""


class GildedRose(object):

    SULFURAS = "Sulfuras, Hand of Ragnaros"

    def __init__(self, items):
        self.items = items

    def _update_items(self,item):
        """
        Wrapper function to update all the items, we match on name.
        :param item: item which we should update.
        :return: updated item.
        """
        itemfactory = ItemFactory()
        if item.name == self.SULFURAS:
            pass
        else:
            type_item = itemfactory.create_item_type(item)
            return type_item.update(item)

    def update_quality(self):
        """
        Wrapper function to update all the items.
        :return: updated items.
        """
        for item in self.items:
            self.item = self._update_items(item)
        return self.items


