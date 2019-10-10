import unittest

from items.backstage_ticket import BackstageTicket
from src.item import Item
class BackstageTicketUnitTest(unittest.TestCase):


    def test_update_backstage_quality(self):
        def update_quality_wrapper(sellin, quantity):
            backstage_item = Item("Backstage passes to a TAFKAL80ETC concert", sellin, quantity)
            backstage_ticket = BackstageTicket()
            updated_ticket = backstage_ticket.update_backstageticket_quality(backstage_item)
            return updated_ticket

        actual = update_quality_wrapper(10,10)
        assert(actual == 11)
        actual = update_quality_wrapper(-1,20)
        assert(actual == 0)

    def test_update(self):
        def update_wrapper(sellin, quantity):
            backstage_item = Item("Backstage passes to a TAFKAL80ETC concert", sellin, quantity)
            backstage_ticket = BackstageTicket()
            updated_ticket = backstage_ticket.update(backstage_item)
            return updated_ticket

        #run first test.
        actual = update_wrapper(10,10)
        assert(actual.sell_in == 9)
        assert(actual.quality == 12)

        #running second test, can refactor this to a seperate test.
        actual = update_wrapper(-1,20)
        assert(actual.sell_in== -2)
        assert(actual.quality == 0)



if __name__ == '__main__':
    unittest.main()
