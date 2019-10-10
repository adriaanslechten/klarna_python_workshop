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

    def update_backstageticket_quality(self, backstage_ticket):
        """
        Helper funciton to update the backstage tickets their quality.
        :param backstage_ticket: item.
        :return: updated quality
        """
        if backstage_ticket.sell_in < 0:
            return 0
        elif backstage_ticket.sell_in < 11:
            return self.increase_quality(backstage_ticket)
        else:
            return backstage_ticket.quality

    def update_backstage_ticket(self, backstage_ticket):
        """
        Helper funciton to update the backstage ticket.
        :param backstage_ticket: input item (backstage ticket)
        :return: updated ticket.
        """
        backstage_ticket.quality = self.increase_quality(backstage_ticket)
        backstage_ticket.quality = self.update_backstageticket_quality(backstage_ticket)
        backstage_ticket.sell_in = backstage_ticket.sell_in - 1
        if backstage_ticket.sell_in < 0:
            return self.update_backstageticket_quality(backstage_ticket)
        else:
            return backstage_ticket.quality

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

    def update_other_items(self, item):
        """
        Helper function to update the other items
        :param item: input item.
        :return: updated item.
        """
        item.quality = self.decrease_quality(item)
        item.sell_in = item.sell_in - 1
        if item.sell_in < 0:
            item.quality = self.decrease_quality(item)
        return item

    def update_items(self, item):
        """
        Wrapper function to update all the items, we match on name.
        :param item: item which we should update.
        :return: updated item.
        """
        if item.name == "Sulfuras, Hand of Ragnaros":
            pass
        elif item.name == "Aged Brie":
            return self.update_aged_brie(item)
        elif item.name == "Backstage passes to a TAFKAL80ETC concert":
            return self.update_backstage_ticket(item)
        else:
            return self.update_other_items(item)

    def update_quality(self):
        """
        Wrapper funciton to update all the items.
        :return: updated items.
        """
        for item in self.items:
            self.item = self.update_items(item)
        return self.items


class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)

    def __eq__(self, other):
        """
        Needed for equality method. Comparing self with other.
        :param other: other item we want to compare with
        :return: true or false
        """
        return self.name == other.name and \
               self.sell_in == other.sell_in and \
               self.quality == other.quality

    def __hash__(self):
        """
        necessary for instances to behave sanely in dicts and sets.
        :retrun: hashed string.
        """
        return hash((self.name, self.sell_in, self.quality))
