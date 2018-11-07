import unittest
from order_verify import check_order_status_delivered, add_new_order, check_order_status_pending, check_none_existent_order, change_order_status

class TestOrders(unittest.TestCase):
    def test_delivered_order(self):
        self.assertEqual(check_order_status_delivered(3), True)

    def test_pending_order(self):
        self.assertEqual(check_order_status_pending(8), True)

    def test_pending_order(self):
        self.assertFalse(check_order_status_pending(3))

    def test_existent_order(self):
        self.assertEqual(check_none_existent_order(4), True)

    def test_non_existent_order(self):
        self.assertFalse(check_none_existent_order(14))

    def test_mark_order_delivered(self):
        self.assertEqual(change_order_status(9), True)

    def test_add_new_order(self):
        self.assertEqual(add_new_order(10), True)

    def test_orderid_is_integer(self):
        self.assertEqual(add_new_order("p"), False)

    def test_orders_added_to_list(self):
        pass
