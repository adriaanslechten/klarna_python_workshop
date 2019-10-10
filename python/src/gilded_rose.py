from src.item_factory import ItemFactory

"""
Main run function.
"""
class GildedRose(object):

    def __init__(self, items):
        self.items = items


    def update_items(self, item):
        """
        Wrapper function to update all the items, we match on name.
        :param item: item which we should update.
        :return: updated item.
        """
        itemfactory = ItemFactory()
        if item.name == "Sulfuras, Hand of Ragnaros":
            pass
        else:
            type_item = itemfactory.createItemType(item)
            return type_item.update(item)

    def update_quality(self):
        """
        Wrapper funciton to update all the items.
        :return: updated items.
        """
        for item in self.items:
            self.item = self.update_items(item)
        return self.items


