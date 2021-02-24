def foo(n, a="A", b="B", c="C"):
    if n == 0:
        return

    foo(n - 1, a, c, b)
    print('Moving Disc %d from %s to %s' %(n, a, c))
    foo(n - 1, b, a, c)

n = int(input())
foo(n)