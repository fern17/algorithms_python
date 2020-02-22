def merge(v, p, q, r):
    n1 = q - p + 1
    n2 = r - q
    L = [0] * n1
    R = [0] * n2
    for i in range(0, n1):
        L[i] = v[p+i]

    for j in range(0, n2):
        R[j] = v[q+j+1]

    i = 0
    j = 0
    k = p
    while i < n1 and j < n2:
        if L[i] <= R[j]:
            v[k] = L[i]
            i = i+1
        else:
            v[k] = R[j]
            j = j+1
        k = k+1

    if i == n1:
        for jj in range(j, n2):
            v[k] = R[jj]
            k = k + 1
    if j == n2:
        for ii in range(i, n1):
            v[k] = L[ii]
            k = k + 1


def merge_sort2(v, p, r):
    if p < r:
        q = (p+r)//2
        merge_sort2(v, p, q)
        merge_sort2(v, q+1, r)
        merge(v, p, q, r)


def merge_sort(v):
    merge_sort2(v, 0, len(v)-1)
    return v
