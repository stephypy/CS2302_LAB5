class LRU:
    def __init__(self):
        self.cache = {}

    def get(self, key):
        if key not in self.cache:
            return -1
        return self.cache[key]

    def put(self, key, value):
        print('insert/replace')

    def size(self):
       print('size')

    def max_capacity(self):
        print('max')
