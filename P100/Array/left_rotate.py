arr = list(map(int, input().split()))
n = len(arr)

first = arr[0]

for i in range(n - 1):
    arr[i] = arr[i + 1]

arr[-1] = first

print(arr)