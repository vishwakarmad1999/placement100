arr = list(map(int, input().split()))
n = len(arr)

mx = arr[-1]
output = [mx]
for i in range(n - 2, -1, -1):
    if arr[i] > mx:
        output.append(arr[i])
        mx = arr[i]

print(output[::-1])