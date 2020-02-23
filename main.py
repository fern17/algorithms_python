from sorting.insertion_sort import *
from sorting.merge_sort import *
from sorting.bubble_sort import *
from data_structures.Heap import *
from sorting.heap_sort import *
from sorting.quick_sort import *
from sorting.counting_sort import *
from sorting.radix_sort import *
from sorting.bucket_sort import *
from tools import *


def test_sorting():
    v = rand_vector(10, 1, 100)
    vf = rand_vector_f(10, 0.0, 1.0)
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
    #print("======")
    #print("Quick Sort")
    #v5 = quick_sort(v)
    #print(v5)
    #print("======")
    #print("Counting Sort")
    #v6 = counting_sort(v)
    #print(v6)

    print("======")
    print("Radix Sort")
    v7 = radix_sort(v)
    print(v7)

    print("======")
    print("Bucket Sort")
    v8 = bucket_sort(vf)
    print(v8)

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