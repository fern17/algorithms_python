import math
from sorting.insertion_sort import  insertion_sort


def bucket_sort(v):
    n = len(v)
    B = []
    for i in range(0, n):
        B.append([])

    for i in range(0, n):
        idx = math.floor(n*v[i])
        B[idx].append(v[i])

    for i in range(0, n):
        B[i] = insertion_sort(B[i])

    idx = 0
    for i in range(0, n):
        for j in range(0, len(B[i])):
            v[idx] = B[i][j]
            idx += 1

    return v
