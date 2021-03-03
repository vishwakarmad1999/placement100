def foo(arr, n):
    i = -1
    for j in range(n):
        if arr[j] < 0:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

arr = list(map(int, input().split()))
foo(arr, len(arr))

print(arr)

