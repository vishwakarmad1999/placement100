arr = list(map(int, input().split()))
n = len(arr)

i, j = 0, 1
while j < n:
    if arr[i] != arr[j]:
        i += 1
        arr[i] = arr[j]
    j += 1

i += 1
while i < n:
    arr[i] = -1
    i += 1

print(arr)