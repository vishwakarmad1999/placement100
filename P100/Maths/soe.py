n = int(input())
arr = [True] * (n + 1)

p = 2
while p * p <= n:
    if arr[p]:
        i = p * p
        while i <= n:
            arr[i] = False
            i += p
    p += 1

for i in range(2, n):
    if arr[i]:
        print(i, end=' ')