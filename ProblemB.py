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
        li.sort(reverse = True)
        self.populate_dict(li)
        print(self.word_dict)
        for word in self.word_dict:
            self._inserting(word)

    def _inserting(self, word):
        self.tree.append(word)
        self.percolate_up(len(self.tree) - 1)

    # Populates the dictionary
    def populate_dict(self, li):
        for word in li:
            if word in self.word_dict:
                self.word_dict[word] += 1
            else:
                self.word_dict[word] = 1

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

        if len(self.tree) % 2 == 1 and len(self.tree) > 1:
            left_child = self.left_child(parent_index)
            right_child = self.right_child(parent_index)
            left = self.word_dict[left_child]
            right = self.word_dict[right_child]
            if right > left or ((right == left) and (self.lower_alphabetic(right_child, left_child))):
                left = 2 * parent_index + 1
                right = 2 * parent_index + 2
                self.tree[left], self.tree[right] = self.tree[right], self.tree[left]

        self.print_list()
        self.percolate_up(parent_index)

    def print_list(self):
        for i in range(0, len(self.tree)):
            print(self.tree[i], ':', self.word_dict[self.tree[i]])
        print()


def main():
    li = ['sweet', 'dog', 'umbrella', 'sweet', 'hot', 'hat', 'paper', 'gadget', 'paper', 'paper', 'hot', 'dog', 'hat']
    heap = MaxHeap()
    heap.insert(li)
    print('======')
    heap.print_list()


main()
