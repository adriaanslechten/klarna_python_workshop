"""Models for items"""
from typing import List, Optional

from workshop.items.items import Item
from workshop.libs.item_helpers import (decrease_quality, decrease_sell_in,
                                        increase_quality, item_has_expired)


class Backstage():
    """Model for Backstage items"""

    @staticmethod
    def update_backstage(item: Item) -> int:
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


class AgedBrie():
    """Model for Aged bries items"""

    @staticmethod
    def update_aged_brie(item: Item) -> int:
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


class RegularItems():
    """Model for regular items"""

    @staticmethod
    def update_regular_items(item: Item) -> int:
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


class GildedRose():
    """Class for Gilded rose"""
    def __init__(self, items: List[Item]):
        self.items = items

    def update_quality(self) -> List[Item]:
        """Outer loop for update quality of all the items."""
        for item in self.items:
            update_item_quality(item)
        return self.items

def update_item_quality(item: Item) -> Optional[int]:
    """Function to update an individual item's quality."""
    if item.name == "Sulfuras, Hand of Ragnaros":
        return None
    if item.name == "Aged Brie":
        return AgedBrie().update_aged_brie(item)
    if item.name == "Backstage passes to a TAFKAL80ETC concert":
        return Backstage().update_backstage(item)
    return RegularItems().update_regular_items(item)
