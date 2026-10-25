class Node:
    def __init__(self, info, next_node=None):
        self.info = info
        self.next = next_node

    def get_info(self):
        return self.info

    def set_info(self, info):
        self.info = info

    def get_next(self):
        return self.next

    def set_next(self, next_node):
        self.next = next_node


class Order:
    def __init__(self, qtty, customer):
        self.customer = customer
        self.qtty = qtty

    def print(self):
        print(f"    Customer: {self.customer}")
        print(f"    Quantity: {self.qtty}")

    def get_qtty(self):
        return self.qtty

    def get_customer(self):
        return self.customer


class Queue:
    def __init__(self):
        self.top = None
        self.tail = None
        self._size = 0

    def size(self):
        return self._size

    def isEmpty(self):
        return self._size == 0

    def front(self):
        if self.isEmpty():
            return None
        return self.top.get_info()

    def enqueue(self, info):
        new_node = Node(info)
        if self.isEmpty():
            self.top = new_node
            self.tail = new_node
        else:
            self.tail.set_next(new_node)
            self.tail = new_node
        self._size += 1

    def dequeue(self):
        if self.isEmpty():
            return None
        info = self.top.get_info()
        self.top = self.top.get_next()
        self._size -= 1
        if self.top is None:
            self.tail = None
        return info

    def printInfo(self):
        print("**** QUEUE DUMP ****")
        print(f"Size: {self._size}")
        current = self.top
        index = 1
        while current is not None:
            print(f"** Element {index}")
            order = current.get_info()
            if hasattr(order, 'print'):
                order.print()
            else:
                print(f"    Info: {order}")
            current = current.get_next()
            index += 1
        print("********************\n")

    def getNth(self, pos):
        if pos < 1 or pos > self._size:
            return None
        current = self.top
        current_pos = 1
        while current is not None and current_pos < pos:
            current = current.get_next()
            current_pos += 1
        return current.get_info() if current else None


class TestQueue:
    @staticmethod
    def main():
        queue = Queue()

        order1 = Order(20, "cust1")
        order2 = Order(30, "cust2")
        order3 = Order(40, "cust3")
        order4 = Order(50, "cust3")

        queue.enqueue(order1)
        queue.enqueue(order2)
        queue.enqueue(order3)
        queue.enqueue(order4)
        queue.printInfo()

        f_elem = queue.front()
        if f_elem:
            f_elem.print()
        print()

        nth_elem = queue.getNth(3)
        if nth_elem:
            nth_elem.print()
        print()

        queue.dequeue()
        queue.printInfo()


if __name__ == "__main__":
    TestQueue.main()