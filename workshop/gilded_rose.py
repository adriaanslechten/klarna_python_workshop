# -*- coding: utf-8 -*-
class GildedRose(object):
    def __init__(self, items):
        self.items = items

    def decrease_quality(self, item):
        """
        Helper function to increase the quality.
        :param item: item which we want tod descrease
        :return: integer, containing the quality minus one
        """
        if item.quality > 0:
            return item.quality - 1
        return item.quality

    def increase_quality(self, item):
        """
        Helper function to increase the quality.
        :param item: item which we want to increase
        :return: integer, containing the quality plus one
        """
        if item.quality < 50:
            return item.quality + 1
        return item.quality

    def decrease_sell_in(self, sell_in):
        """
        Helper function to decrease the sell_in
        :param sell_in: sell_in param.
        :return: integer, containing the sell_in minus one.
        """
        return sell_in - 1

    def item_has_expired(self, item):
        """
        Helper function to check if an item is expired
        :param item: item which we want to check if it's expired
        :return: bool
        """
        return True if item.sell_in < 0 else False

    def update_backstage(self, item):
        """
        Helper function to update the backstage item
        :param item: containing the backstage pass
        :return: integer, containing the backstage quality
        """

        item.quality = self.increase_quality(item)
        if item.sell_in < 11:
            item.quality = self.increase_quality(item)
        if item.sell_in < 6:
            item.quality = self.increase_quality(item)
        item.sell_in = self.decrease_sell_in(item.sell_in)
        if self.item_has_expired(item):
            item.quality = item.quality - item.quality
        return item.quality

    def update_aged_brie(self, item):
        """
        Helper function to update the aged_brie item
        :param item: containing the aged_brie
        :return: integer, containing the aged_brie quality
        """
        item.quality = self.increase_quality(item)
        item.sell_in = self.decrease_sell_in(item.sell_in)
        if self.item_has_expired(item):
            item.quality = self.increase_quality(item)
        return item.quality

    def update_other_items(self, item):
        """
        Helper function to update the other_items
        :param item: containing the other_items
        :return: integer, containing the other_items quality
        """
        item.quality = self.decrease_quality(item)
        item.sell_in = self.decrease_sell_in(item.sell_in)
        if self.item_has_expired(item):
            item.quality = self.decrease_quality(item)
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


class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __eq__(self, other):
        return (
            self.name == other.name
            and self.sell_in == other.sell_in
            and self.quality == other.quality
        )

    def __hash__(self):
        # necessary for instances to behave sanely in dicts and sets.
        return hash((self.name, self.sell_in, self.quality))

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)
