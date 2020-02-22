
class Heap:
    def __init__(self, data):
        self.data = data
        self.heap_size = len(self.data)
        self.build_max_heap()

    def parent(self, i):
        return i//2

    def left(self, i):
        return 2*i

    def right(self, i):
        return 2*i+1

    def print(self):
        print(self.data)
        print(self.heap_size)

    def max_heapify(self, i):
        l = self.left(i)
        r = self.right(i)
        largest = i
        if l < self.heap_size and self.data[l] > self.data[i]:
            largest = l

        if r < self.heap_size and self.data[r] > self.data[largest]:
            largest = r

        if largest != i:
            self.data[i], self.data[largest] = self.data[largest], self.data[i]
            self.max_heapify(largest)

    def build_max_heap(self):
        self.heap_size = len(self.data)
        start = self.heap_size//2
        for i in range(start, -1, -1):
            self.max_heapify(i)

    def swap(self, i):
        if i < self.heap_size:
            self.data[i], self.data[0] = self.data[0], self.data[i]

    def decrease_heap_size(self):
        self.heap_size = max(self.heap_size-1, 0)

    def get_heap_size(self):
        return self.heap_size

    def get_data(self):
        return self.data
