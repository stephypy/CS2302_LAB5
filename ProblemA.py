class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None


class DLL:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    # Wil always insert at the tail
    def insert(self, val):
        if val is None:
            raise Exception('Invalid new value')
        new_node = Node(val)
        if self.head is None:
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        self.size += 1

    def delete_last(self):
        if self.size == 0:
            raise Exception('Doubly Linked List is empty')
        if self.size == 1:
            self.head = self.tail = None
            self.size = 0
            return
        new_tail = self.tail.prev
        new_tail.next = None
        self.tail = new_tail
        self.size -= 1


class LRU:
    def __init__(self, maximum):
        self.cache_values = {}
        self.cache = DLL()
        self.maximum = maximum

    def get(self, key):
        if key not in self.cache_values:
            return -1
        return self.cache_values[key]

    def put(self, key, value):
        if self.size() < self.max_capacity():
            self.cache_values[key] = value
            self.cache.insert(key)
        else:
            lru = self.cache.tail.val
            self.cache.delete_last()
            self.cache_values.pop(lru)

    def size(self):
        return self.cache.size

    def max_capacity(self):
        return self.maximum
