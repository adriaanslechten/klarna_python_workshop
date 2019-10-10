import unittest

from items.backstage_ticket import BackstageTicket
from src.item import Item

class BackstageTicketUnitTest(unittest.TestCase):

    def test_update_backstage(self):
        def run_backstage_test(sellin,quantity):
            backstage_item = Item("Backstage passes to a TAFKAL80ETC concert", sellin, quantity)
            backstage_ticket= BackstageTicket()
            return backstage_ticket.update_backstageticket_quality(backstage_item)

        actual = run_backstage_test(10,10)
        assert(actual == 11)
        actual = run_backstage_test(-1,20)
        assert(actual == 0)



if __name__ == '__main__':
    unittest.main()
