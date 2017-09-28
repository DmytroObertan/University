def insertion(inp):
    for i in range(1, len(inp)):
        # import pdb
        # pdb.set_trace()
        key = inp[i]
        j = i - 1
        while j >= 0 and key < inp[j]:
            inp[j + 1] = inp[j]
            j -= 1
        inp[j + 1] = key
    return inp


if __name__ == '__main__':
    print insertion([6, 5, 4, 3, 2, 7, 1])
