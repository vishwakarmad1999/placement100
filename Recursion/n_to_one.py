def foo(n):
    if n == 0:
        return

    print(n)
    foo(n - 1)

n = int(input())
foo(n)