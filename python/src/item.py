"""
Class containing the item. THis is used inside of the Gilded Rose code kata.
"""
class Item:
    def __init__(self, name, sell_in, quality):
        """
        Init method.
        :param name: name of the item.
        :param sell_in: days remaining that it's sond.
        :param quality: quality of the item.
        """
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        """
        Method to print it well.
        :return: string containing the printed values.
        """
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
