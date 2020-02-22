def partition(v, p, r):
    x = v[r]
    i = p-1
    for j in range(p, r):
        if v[j] <= x:
            i = i+1
            v[i], v[j] = v[j], v[i]

    v[i+1], v[r] = v[r], v[i+1]
    return i+1


def quick_sort2(v, p, r):
    if p < r:
        q = partition(v, p, r)
        quick_sort2(v, p, q-1)
        quick_sort2(v, q+1, r)
    return v


def quick_sort(v):
    return quick_sort2(v, 0, len(v)-1)

