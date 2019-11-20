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
            self.head.prev = new_node
            new_node.next = self.head
            self.head = new_node
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
            self.cache_values[key] = value
            self.cache.insert(key)

    def size(self):
        return self.cache.size

    def max_capacity(self):
        return self.maximum

    def print_lru(self):
        curr = self.cache.head
        while curr is not None:
            print('key: ', curr.val, 'val: ', self.get(curr.val))
            curr = curr.next


def main():
    lru = LRU(5)
    for i in range(1, 5):
        lru.put(i, i*2)
        lru.print_lru()
        print('')
    lru.print_lru()
    lru.put(5, 10)
    print('')
    lru.print_lru()
    lru.put(6, 12)
    print('')
    lru.print_lru()


main()
