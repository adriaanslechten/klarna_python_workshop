from src.items.aged_brie import  AgedBrie
from src.items.backstage_ticket import BackstageTicket
from src.items.regular_item import RegularItem

class GildedRose(object):

    def __init__(self, items):
        self.items = items


    def update_items(self, item):
        """
        Wrapper function to update all the items, we match on name.
        :param item: item which we should update.
        :return: updated item.
        """
        if item.name == "Sulfuras, Hand of Ragnaros":
            pass
        elif item.name == "Aged Brie":
            aged_brie = AgedBrie()
            return aged_brie.update(item)
        elif item.name == "Backstage passes to a TAFKAL80ETC concert":
            backstage_ticket = BackstageTicket()
            return backstage_ticket.update(item)
        else:
            regular_item = RegularItem()
            return regular_item.update(item)

    def update_quality(self):
        """
        Wrapper funciton to update all the items.
        :return: updated items.
        """
        for item in self.items:
            self.item = self.update_items(item)
        return self.items


