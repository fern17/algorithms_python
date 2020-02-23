def counting_sort(A):
    k = max(A)+1
    n = len(A)
    B = [0]*n
    C = [0]*k

    for j in range(0, n):
        C[A[j]] = C[A[j]]+1

    for i in range(1, k):
        C[i] += C[i-1]

    for j in range(n-1, -1, -1):
        B[C[A[j]]-1] = A[j]
        C[A[j]] = C[A[j]]-1

    return B
