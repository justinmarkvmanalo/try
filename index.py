import queue

# Initialize the priority queue and regular queue
priority_queue = queue.Queue()
regular_queue = queue.Queue()

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