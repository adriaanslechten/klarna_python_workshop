from src.items.regular_item import RegularItem

class BackstageTicket(RegularItem):


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

