
def counting_sort_exp(A, e):
    n = len(A)

    B = [0] * n
    C = [0] * 10

    for j in range(0, n):
        idx = A[j]//e
        C[idx % 10] += 1

    for i in range(1, 10):
        C[i] += C[i - 1]

    j = n-1
    while j >= 0:
        idx = A[j]//e
        B[C[idx % 10] - 1] = A[j]
        C[idx % 10] -= 1
        j -= 1
    return B

def radix_sort(v):
    maxi = max(v)
    e = 1
    while maxi//e > 0:
        v = counting_sort_exp(v, e)
        e *= 10
    return v
