def quick_sort(arr, l, r):
    if l < r:
        pos = partition(arr, l, r)
        quick_sort(arr, l, pos - 1)
        quick_sort(arr, pos + 1, r)

def partition(arr, l, r):
    x = arr[r]
    i = l - 1
    for j in range(l, r):
        if arr[j] < x:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[r] = arr[r], arr[i + 1]
    return i + 1

arr = list(map(int, input().split()))
quick_sort(arr, 0, len(arr) - 1)
print(arr)