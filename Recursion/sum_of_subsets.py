def foo(arr, n, s):
    if n == 0:
        if s == 0:
            return 1
        return 0

    return foo(arr, n - 1, s) + foo(arr, n - 1, s - arr[n - 1])

arr = list(map(int, input().split()))
s = int(input())

print(foo(arr, len(arr), s))