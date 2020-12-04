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

    def update_quality(self):
        for item in self.items:
            if item.name == "Sulfuras, Hand of Ragnaros":
                pass

            else:
                if item.name == "Aged Brie":
                    item.quality = self.increase_quality(item)
                elif item.name == "Backstage passes to a TAFKAL80ETC concert":
                    item.quality = self.increase_quality(item)
                    if item.sell_in < 11:
                        item.quality = self.increase_quality(item)
                    if item.sell_in < 6:
                        item.quality = self.increase_quality(item)
                else:
                    item.quality = self.decrease_quality(item)
                item.sell_in = item.sell_in - 1
                if item.sell_in < 0:
                    if item.name == "Aged Brie":
                        item.quality = self.increase_quality(item)
                    elif (
                        item.name == "Backstage passes to a TAFKAL80ETC concert"
                    ):
                        item.quality = item.quality - item.quality
                    else:
                        item.quality = self.decrease_quality(item)


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
