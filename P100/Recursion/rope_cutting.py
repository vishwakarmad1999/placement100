def rc(n, a, b, c):
    if n < 0:
        return -1
    elif n == 0:
        return 0

    res = max(rc(n - a, a, b, c), rc(n - b, a, b, c), rc(n - c, a, b, c))
    if res == -1:
        return -1

    return res + 1

n, a, b, c = map(int, input().split())
print(rc(n, a, b, c))