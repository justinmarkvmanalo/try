import unittest
from queue import Queue

# Code from your Customer Queue Management System

priority_queue = Queue()
regular_queue = Queue()


# Adds a customer to the specified queue (VIP or regular)
# Raises a ValueError if an invalid queue type is provided
def add_customer(queue_type, customer_name):
    if queue_type == "VIP":
        priority_queue.put(customer_name)  # Add to VIP queue
    elif queue_type == "regular":
        regular_queue.put(customer_name)  # Add to regular queue
    else:
        raise ValueError("Invalid queue type! Use 'VIP' or 'regular'.")


# Removes a customer from the queues
# Priority is given to VIP customers over regular customers
# Returns the customer's name, or None if both queues are empty
def remove_customer():
    if not priority_queue.empty():
        return priority_queue.get()  # Remove from VIP queue if available
    elif not regular_queue.empty():
        return regular_queue.get()  # Remove from regular queue if VIP is empty
    else:
        return None  # Return None if both queues are empty


# Displays the current state of both queues
# Returns a dictionary with the contents of the VIP and regular queues
def display_queues():
    vip_queue = list(priority_queue.queue)  # Convert VIP queue to a list
    regular_queue_list = list(regular_queue.queue)  # Convert regular queue to a list
    return {"VIP": vip_queue, "Regular": regular_queue_list}


# Unittest class for testing the functionality of the Customer Queue Management System
class TestQueueManagementSystem(unittest.TestCase):

    # Setup method to reset the queues before each test
    def setUp(self):
        global priority_queue, regular_queue
        priority_queue = Queue()  # Reset VIP queue
        regular_queue = Queue()  # Reset regular queue

    # Test for adding a VIP customer to the VIP queue
    def test_add_customer_vip(self):
        add_customer("VIP", "Alice")
        self.assertEqual(list(priority_queue.queue), ["Alice"])

    # Test for adding a regular customer to the regular queue
    def test_add_customer_regular(self):
        add_customer("regular", "Bob")
        self.assertEqual(list(regular_queue.queue), ["Bob"])

    # Test for attempting to add a customer with an invalid queue type
    def test_add_customer_invalid(self):
        with self.assertRaises(ValueError):
            add_customer("invalid", "Charlie")

    # Test for removing a customer from the VIP queue
    def test_remove_customer_vip(self):
        add_customer("VIP", "Alice")
        add_customer("regular", "Bob")
        removed = remove_customer()
        self.assertEqual(removed, "Alice")  # Check VIP customer is removed first
        self.assertEqual(list(priority_queue.queue), [])
        self.assertEqual(list(regular_queue.queue), ["Bob"])

    # Test for removing a customer from the regular queue
    # when the VIP queue is empty
    def test_remove_customer_regular(self):
        add_customer("regular", "Bob")
        removed = remove_customer()
        self.assertEqual(removed, "Bob")
        self.assertEqual(list(regular_queue.queue), [])

    # Test for removing a customer when both queues are empty
    def test_remove_customer_empty(self):
        removed = remove_customer()
        self.assertIsNone(removed)  # Check that None is returned

    # Test for displaying the current state of both queues
    def test_display_queues(self):
        add_customer("VIP", "Alice")
        add_customer("regular", "Bob")
        queues = display_queues()
        self.assertEqual(queues, {"VIP": ["Alice"], "Regular": ["Bob"]})

    # Test for adding multiple VIP customers and checking order
    def test_multiple_vip_customers(self):
        add_customer("VIP", "Alice")
        add_customer("VIP", "Eve")
        self.assertEqual(list(priority_queue.queue), ["Alice", "Eve"])

    # Test for adding multiple regular customers and checking order
    def test_multiple_regular_customers(self):
        add_customer("regular", "Bob")
        add_customer("regular", "Charlie")
        self.assertEqual(list(regular_queue.queue), ["Bob", "Charlie"])

    # Test for removing customers in the correct priority order
    def test_remove_multiple_customers(self):
        add_customer("VIP", "Alice")
        add_customer("VIP", "Eve")
        add_customer("regular", "Bob")
        add_customer("regular", "Charlie")

        # Remove and check each customer in order of priority
        self.assertEqual(remove_customer(), "Alice")
        self.assertEqual(remove_customer(), "Eve")
        self.assertEqual(remove_customer(), "Bob")
        self.assertEqual(remove_customer(), "Charlie")

    # Test for ensuring queue consistency after operations
    def test_queue_consistency(self):
        add_customer("VIP", "Alice")
        add_customer("VIP", "Eve")
        add_customer("regular", "Bob")
        add_customer("regular", "Charlie")

        # Check initial queue state
        self.assertEqual(
            display_queues(),
            {"VIP": ["Alice", "Eve"], "Regular": ["Bob", "Charlie"]}
        )

        # Remove a VIP customer and verify updated state
        remove_customer()
        self.assertEqual(
            display_queues(),
            {"VIP": ["Eve"], "Regular": ["Bob", "Charlie"]}
        )

    # Test for adding and immediately removing customers
    def test_add_and_remove_immediate(self):
        add_customer("VIP", "Alice")
        add_customer("regular", "Bob")

        self.assertEqual(remove_customer(), "Alice")
        self.assertEqual(remove_customer(), "Bob")

    # Test for handling multiple regular customers when no VIPs exist
    def test_no_vip_multiple_regular(self):
        add_customer("regular", "Bob")
        add_customer("regular", "Charlie")

        self.assertEqual(remove_customer(), "Bob")
        self.assertEqual(remove_customer(), "Charlie")

    # Test for ensuring both queues are empty after all removals
    def test_empty_queues_after_removal(self):
        add_customer("VIP", "Alice")
        add_customer("regular", "Bob")

        remove_customer()
        remove_customer()

        self.assertEqual(display_queues(), {"VIP": [], "Regular": []})


if __name__ == "__main__":
    unittest.main()
