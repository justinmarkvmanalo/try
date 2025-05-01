import unittest
from queue import Queue

# Code from your Customer Queue Management System

priority_queue = Queue()
regular_queue = Queue()


def add_customer(queue_type, customer_name):
    if queue_type == "VIP":
        priority_queue.put(customer_name)
    elif queue_type == "regular":
        regular_queue.put(customer_name)
    else:
        raise ValueError("Invalid queue type! Use 'VIP' or 'regular'.")


def remove_customer():
    if not priority_queue.empty():
        return priority_queue.get()
    elif not regular_queue.empty():
        return regular_queue.get()
    else:
        return None


def display_queues():
    vip_queue = list(priority_queue.queue)
    regular_queue_list = list(regular_queue.queue)
    return {"VIP": vip_queue, "Regular": regular_queue_list}


# Unittest class
class TestQueueManagementSystem(unittest.TestCase):

    def setUp(self):
        # Clear the queues before each test
        global priority_queue, regular_queue
        priority_queue = Queue()
        regular_queue = Queue()

    def test_add_customer_vip(self):
        add_customer("VIP", "Alice")
        self.assertEqual(list(priority_queue.queue), ["Alice"])

    def test_add_customer_regular(self):
        add_customer("regular", "Bob")
        self.assertEqual(list(regular_queue.queue), ["Bob"])

    def test_add_customer_invalid(self):
        with self.assertRaises(ValueError):
            add_customer("invalid", "Charlie")

    def test_remove_customer_vip(self):
        add_customer("VIP", "Alice")
        add_customer("regular", "Bob")
        removed = remove_customer()
        self.assertEqual(removed, "Alice")
        self.assertEqual(list(priority_queue.queue), [])
        self.assertEqual(list(regular_queue.queue), ["Bob"])

    def test_remove_customer_regular(self):
        add_customer("regular", "Bob")
        removed = remove_customer()
        self.assertEqual(removed, "Bob")
        self.assertEqual(list(regular_queue.queue), [])

    def test_remove_customer_empty(self):
        removed = remove_customer()
        self.assertIsNone(removed)

    def test_display_queues(self):
        add_customer("VIP", "Alice")
        add_customer("regular", "Bob")
        queues = display_queues()
        self.assertEqual(queues, {"VIP": ["Alice"], "Regular": ["Bob"]})


if __name__ == "__main__":
    unittest.main()
    