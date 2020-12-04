def decrease_quality(item):
    """
    Helper function to increase the quality.
    :param item: item which we want tod descrease
    :return: integer, containing the quality minus one
    """
    if item.quality > 0:
        return item.quality - 1
    return item.quality


def increase_quality(item):
    """
    Helper function to increase the quality.
    :param item: item which we want to increase
    :return: integer, containing the quality plus one
    """
    if item.quality < 50:
        return item.quality + 1
    return item.quality


def decrease_sell_in(sell_in):
    """
    Helper function to decrease the sell_in
    :param sell_in: sell_in param.
    :return: integer, containing the sell_in minus one.
    """
    return sell_in - 1


def item_has_expired(item):
    """
    Helper function to check if an item is expired
    :param item: item which we want to check if it's expired
    :return: bool
    """
    return True if item.sell_in < 0 else False
