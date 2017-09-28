def mergesort(inp):
    if len(inp) == 1:
        return inp
    middle = int(len(inp) / 2)
    left = mergesort(inp[:middle])
    right = mergesort(inp[middle:])
    return merge(left, right)


def merge(left, right):
    i, j = 0, 0
    result = []
    while i < len(left) and j < len(right):
        if left[i] > right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    for l in range(i, len(left)):
        result.append(left[l])
    for l in range(j, len(right)):
        result.append(right[l])
    return result


if __name__ == '__main__':
    print mergesort([3, 4, 8, 0, 6, 7, 4, 2, 1, 9, 4, 5])