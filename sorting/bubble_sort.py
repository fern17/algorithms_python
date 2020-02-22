
def bubble_sort(v):
    for i in range(0, len(v)):
        for j in range(i+1, len(v)):
            if v[i] > v[j]:
                v[i], v[j] = v[j], v[i]

    return v
