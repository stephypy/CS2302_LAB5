import math


class MaxHeap:
    def __init__(self):
        self.tree = []
        self.word_dict = {}

    def is_empty(self):
        return len(self.tree) == 0

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

    def extract(self):
        if len(self.tree) < 1:
            return None
        if len(self.tree) == 1:
            self.word_dict.pop(self.tree[0])
            return self.tree.pop()

        root = self.tree[0]
        self.tree[0] = self.tree.pop()

        self.percolate_down(0)
        self.word_dict.pop(root)

        return root

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
            self.percolate_up(i)
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


        #if parent == curr and self.lower_alphabetic(self.tree[parent_index], self.tree[i]):
         #   self.tree[i], self.tree[parent_index] = self.tree[parent_index], self.tree[i]
        else:
            if i % 2 == 0:
                left = self.tree[i-1]
                right = self.tree[i]
                if self.word_dict[right] > self.word_dict[left] or ((self.word_dict[left] == self.word_dict[right]) and (self.lower_alphabetic(self.tree[i], self.tree[i-1]))):
                    self.tree[i], self.tree[i-1] = self.tree[i-1], self.tree[i]
            

        #left = 2 * parent_index + 1
        #right = 2 * parent_index + 2
        #if len(self.tree) % 2 == 1 and self.word_dict[self.tree[left]] == self.word_dict[self.tree[right]]:
         #   if self.lower_alphabetic(self.tree[left], self.tree[right]):
          #      self.tree[left], self.tree[right] = self.tree[right], self.tree[left]
        self.print_list()
        print('')
        self.percolate_up(parent_index)


    def percolate_down(self, i):
        curr = self.tree[i]
        left = self.left_child(i)
        right = self.right_child(i)
        if self.word_dict[curr] > max(self.word_dict[left], self.word_dict[right]):
            return
        elif self.word_dict[curr] == max(self.word_dict[left], self.word_dict[right]) and self.lower_alphabetic(
                self.tree[i], left):
            return
        else:
            max_child_index = 2 * i + 1 if self.word_dict[left] > self.word_dict[right] else 2 * i + 2

            self.tree[i], self.tree[max_child_index] = self.tree[max_child_index], self.tree[i]
            self.percolate_down(max_child_index)

    def heap_sort(self, li):
        heap_copy = MaxHeap()
        heap_copy.insert(li)
        i = len(li) - 1
        while not heap_copy.is_empty():
            li[i] = heap_copy.extract()
            i -= 1

    def print_list(self):
        #self.heap_sort(self.tree)
        for i in range(0, len(self.tree)):
            print(self.tree[i], ':', self.word_dict[self.tree[i]])


def main():
    li = ['sweet', 'dog', 'umbrella', 'sweet', 'hot', 'hat', 'paper', 'gadget', 'paper', 'paper', 'hot', 'dog', 'hat']
    heap = MaxHeap()
    heap.insert(li)
    print('end')
    heap.print_list()


main()
