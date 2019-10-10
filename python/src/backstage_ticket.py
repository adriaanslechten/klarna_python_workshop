
class BackstageTicket(object):

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


    def item_has_expired(self,item):
        """
        Helper funciton to check if the item is expired
        :param item: item to check
        :return: boolean, if it's expired or not.
        """
        if item.sell_in < 0:
            return True
        else:
            return False

    def update_backstageticket_quality(self, backstage_ticket):
        """
        Helper funciton to update the backstage tickets their quality.
        :param backstage_ticket: item.
        :return: updated quality
        """
        if self.item_has_expired(backstage_ticket):
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

