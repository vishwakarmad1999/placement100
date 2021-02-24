def foo(n):
    n = bin(n)[2:]
    if len(n) % 2 != 0:
        n = '0' + n
    n = list(n)
    for i in range(0, len(n) - 1, 2):
        n[i], n[i + 1] = n[i + 1], n[i]

    return int(''.join(n), 2)

n = int(input())
print(foo(n))