import math


class MaxHeap:
    def __init__(self):
        self.tree = []
        self.word_dict = {}

    def left_child(self, i):
        left = 2 * i + 1
        if left >= len(self.tree):
            self.word_dict[-math.inf] = -math.inf
            return -math.inf
        return self.tree[left]

    def right_child(self, i):
        right = 2 * i + 2
        if right >= len(self.tree):
            self.word_dict[-math.inf] = -math.inf
            return -math.inf
        return self.tree[right]

    # Parameter: a list, adds all the contents of the list
    def insert(self, li):
        li.sort()
        for word in li:
            self._insert(word)

    # Parameter: one word. adds it to the heap
    def _insert(self, word):
        if word in self.tree:
            self.word_dict[word] += 1
            i = self.tree.index(word)
            self.percolate_up(len(self.tree) - 1)
        else:
            self.tree.append(word)
            self.word_dict[word] = 1
            self.percolate_up(len(self.tree) - 1)

    # Returns True if the first word goes after the second word. False otherwise
    def lower_alphabetic(self, first, second):
        li = [first, second]
        li.sort()
        return first == li[1]

    def percolate_up(self, i):
        if i == 0:
            return
        parent_index = (i - 1) // 2
        parent = self.word_dict[self.tree[parent_index]]
        curr = self.word_dict[self.tree[i]]

        if parent < curr or ((parent == curr) and (self.lower_alphabetic(self.tree[i], self.tree[parent_index]))):
            self.tree[i], self.tree[parent_index] = self.tree[parent_index], self.tree[i]
        else:
            # Checking between siblings
            if i % 2 == 0:
                left = self.tree[i-1]
                right = self.tree[i]
                if self.word_dict[right] > self.word_dict[left] or ((self.word_dict[left] == self.word_dict[right]) and (self.lower_alphabetic(self.tree[i], self.tree[i-1]))):
                    self.tree[i], self.tree[i-1] = self.tree[i-1], self.tree[i]
        self.percolate_up(parent_index)

    def print_list(self):
        for i in range(0, len(self.tree)):
            print(self.tree[i], ':', self.word_dict[self.tree[i]])


def main():
    li = ['sweet', 'dog', 'umbrella', 'sweet', 'hot', 'hat', 'paper', 'gadget', 'paper', 'paper', 'hot', 'dog', 'hat']
    heap = MaxHeap()
    heap.insert(li)
    heap.print_list()


main()
