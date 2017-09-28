x_1 = 12345
x_2 = 4567
lul = x_1 * x_2


def karatsuba(x_1, x_2):
    import pdb
    pdb.set_trace()
    if len(str(x_1)) != len(str(x_2)):
        ln = max(len(str(x_1)), len(str(x_2)))
        if ln % 2 != 0:
            x_1 = [0].extend(list(str(x_1)))
            x_2 = [0 for k in range(ln - len(str(x_2)) + 1)].extend(list(str(x_2)))
        else:
            x_1 = list(x_1)
            x_2 = [0 for k in range(ln - len(str(x_2)))].extend(list(str(x_2)))
        x_1 = int(''.join(x_1))
        x_2 = int(''.join(x_2))
    print x_1
    if len(str(x_1)) == 1 or len(str(x_2)) == 1:
        return int(x_1) * int(x_2)
    ln = max(len(str(x_1)), len(str(x_2)))
    lnby2 = ln / 2
    a = int(x_1) / 10 ** (lnby2)
    b = int(x_1) % 10 ** (lnby2)
    c = int(x_2) / 10 ** (lnby2)
    d = int(x_2) % 10 ** (lnby2)
    ac = karatsuba(a, c)
    bd = karatsuba(b, d)
    acbd = karatsuba((a + b), (c + d))
    return (10 ** ln) * ac + ((10 ** (ln / 2)) * (acbd - ac - bd)) + bd


if __name__ == '__main__':
    print lul
    print karatsuba(x_1, x_2)
