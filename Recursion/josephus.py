def foo(n, k):
    if n == 1:
        return 0

    return (foo(n - 1, k) + k) % n

n, k = map(int, input().split())
print(foo(n, k))