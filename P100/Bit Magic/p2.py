def binsort(cls, n, org)
    arr = list(map(lambda x: x[2:], list(map(bin, org))))

    mx = len(bin(max(org))[2:])

    arr = list(map(lambda x: x.rjust(mx, '0'), arr))
    res = list(map(lambda x: int(x, 2), sorted(arr)[::-1]))

    return res