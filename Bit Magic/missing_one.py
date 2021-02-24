n = int(input())
arr = list(map(int, input().split()))

org = 0
for i in range(1, n + 1):
    org ^= i

act = 0
for i in arr:
    act ^= i

print(org ^ act)