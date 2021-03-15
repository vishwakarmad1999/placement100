def foo(a, b, c, n):
    if n == 1:
        return a
    elif n == 2:
        return b
    elif n == 3:
        return c

    return foo(a, b, c, n - 1) + foo(a, b, c, n - 2) + foo(a, b, c, n - 3)


t = int(input())
for i in range(t):
    a, b, c, n = map(int, input().split())
    print(foo(a, b, c, n))

