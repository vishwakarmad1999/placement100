arr = list(map(int, input().split()))
n = len(arr)

j = 0
i = 0
while j < n:
    if arr[j] != 0:
        arr[i], arr[j] = arr[j], arr[i]
        i += 1
    j += 1

print(arr)