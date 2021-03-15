# arr = [2, 3, 10, 6, 4, 8, 1]
arr = list(map(int, input().split()))
n = len(arr)
pfix = [arr[0]]

for i in range(1, n):
    pfix.append(min(pfix[i - 1], arr[i]))

mx = arr[1] - pfix[0]
for i in range(2, n):
    mx = max(arr[i] - pfix[i - 1], mx)

print(mx)