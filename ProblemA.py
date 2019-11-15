class LRU:
    def __init__(self, maximum):
        self.cache = {}
        self.maximum = maximum

    def get(self, key):
        if key not in self.cache:
            return -1
        return self.cache[key]

    def put(self, key, value):
        if self.size() < self.max_capacity():
            self.cache[key] = value

    def size(self):
        return len(self.cache)

    def max_capacity(self):
        return self.maximum
