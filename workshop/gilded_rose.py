# -*- coding: utf-8 -*-

from workshop.libs.item_helpers import (
    decrease_quality,
    decrease_sell_in,
    increase_quality,
    item_has_expired,
)
from workshop.item import Item


class GildedRose(object):
    def __init__(self, items):
        self.items = items

    def update_backstage(self, item):
        """
        Helper function to update the backstage item
        :param item: containing the backstage pass
        :return: integer, containing the backstage quality
        """

        item.quality = increase_quality(item)
        if item.sell_in < 11:
            item.quality = increase_quality(item)
        if item.sell_in < 6:
            item.quality = increase_quality(item)
        item.sell_in = decrease_sell_in(item.sell_in)
        if item_has_expired(item):
            item.quality = item.quality - item.quality
        return item.quality

    def update_aged_brie(self, item):
        """
        Helper function to update the aged_brie item
        :param item: containing the aged_brie
        :return: integer, containing the aged_brie quality
        """
        item.quality = increase_quality(item)
        item.sell_in = decrease_sell_in(item.sell_in)
        if item_has_expired(item):
            item.quality = increase_quality(item)
        return item.quality

    def update_other_items(self, item):
        """
        Helper function to update the other_items
        :param item: containing the other_items
        :return: integer, containing the other_items quality
        """
        item.quality = decrease_quality(item)
        item.sell_in = decrease_sell_in(item.sell_in)
        if item_has_expired(item):
            item.quality = decrease_quality(item)
        return item.quality

    def update_item_quality(self, item):
        """Function to update an individual item's quality."""
        if item.name == "Sulfuras, Hand of Ragnaros":
            pass
        elif item.name == "Aged Brie":
            return self.update_aged_brie(item)
        elif item.name == "Backstage passes to a TAFKAL80ETC concert":
            return self.update_backstage(item)
        else:
            return self.update_other_items(item)

    def update_quality(self):
        """Outer loop for update quality of all the items."""
        for item in self.items:
            self.item = self.update_item_quality(item)
        return self.items
