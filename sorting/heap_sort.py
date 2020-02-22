from data_structures.Heap import Heap

def heap_sort(v):
    h = Heap(v)
    sz = h.get_heap_size()-1

    for i in range(sz, 0, -1):
        h.swap(i)
        h.decrease_heap_size()
        h.max_heapify(0)

    return h.get_data()

