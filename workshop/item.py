
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
