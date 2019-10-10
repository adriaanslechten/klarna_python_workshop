from src.items.aged_brie import AgedBrie
from src.items.backstage_ticket import BackstageTicket
from src.items.regular_item import RegularItem

"""
Factory method.
"""


class ItemFactory(object):

    AGED_BRIE = "Aged Brie"
    BACKSTAGE_PASS = "Backstage passes to a TAFKAL80ETC concert"

    def create_item_type(self, item):
        """
        Wrapper function to update all the items, we match on name.
        :param item: item which we should update.
        :return: updated item.
        """
        if item.name == self.AGED_BRIE:
            return AgedBrie()
        elif item.name == self.BACKSTAGE_PASS:
            return BackstageTicket()
        else:
            return RegularItem()
