def partition(inp, p, r):
    i = p - 1
    x = inp[r]
    for j in range(p, r):
        if x >= inp[j]:
            k = inp[j]
            inp[j] = inp[i + 1]
            inp[i + 1] = k
            i += 1
    k = inp[r]
    inp[r] = inp[i + 1]
    inp[i + 1] = k
    return i + 1


def quicksort(inp, p, r):
    if p < r:
        # import pdb
        # pdb.set_trace()
        q = partition(inp, p, r)
        quicksort(inp, p, q - 1)
        quicksort(inp, q + 1, r)
    return inp



if __name__ == '__main__':
    
    inp = [5, 2, 1, 3, 4]
    print quicksort(inp, 0, len(inp) - 1)
