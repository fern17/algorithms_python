from sorting.insertion_sort import *
from sorting.merge_sort import *
from sorting.bubble_sort import *
from data_structures.Heap import *
from sorting.heap_sort import *
from sorting.quick_sort import *


def test_sorting():
    v = [10, 5, 2, 3, 4, 7, 11]
    print("Original vector")
    print(v)
    print("======")
    # print("Insertion Sort")
    #     # v1 = insertion_sort(v)
    #     # print(v1)
    #     # print("======")
    #     # print("Merge Sort")
    #     # v2 = merge_sort(v)
    #     # print(v2)
    #     # print("======")
    #     # print("Bubble Sort")
    #     # v3 = bubble_sort(v)
    #     # print(v3)
    #     # print("======")
    #     # print("Heap Sort")
    #     # v4 = heap_sort(v)
    #     # print(v4)
    print("======")
    print("Quick Sort")
    v5 = quick_sort(v)
    print(v5)
    print("======")


def test_data_structures():
    v = [10, 5, 3, 2, 6, 9, 1]
    h = Heap(v)
    h.print()


def main():
    test_sorting()
    #test_data_structures()


if __name__ == '__main__':
    main()