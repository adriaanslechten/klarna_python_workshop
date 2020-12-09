"""Helper functions for items"""

from workshop.items.items import Item


def decrease_quality(item: Item) -> int:
    """
    Helper function to increase the quality.
    :param item: item which we want tod descrease
    :return: integer, containing the quality minus one
    """
    if item.quality > 0:
        return item.quality - 1
    return item.quality


def increase_quality(item: Item) -> int:
    """
    Helper function to increase the quality.
    :param item: item which we want to increase
    :return: integer, containing the quality plus one
    """
    if item.quality < 50:
        return item.quality + 1
    return item.quality


def decrease_sell_in(sell_in: int) -> int:
    """
    Helper function to decrease the sell_in
    :param sell_in: sell_in param.
    :return: integer, containing the sell_in minus one.
    """
    return sell_in - 1


def item_has_expired(item: Item) -> bool:
    """
    Helper function to check if an item is expired
    :param item: item which we want to check if it's expired
    :return: bool
    """
    return item.sell_in < 0
