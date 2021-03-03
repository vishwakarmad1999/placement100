arr = list(map(int, input().split()))
n = len(arr)

mn = 10 ** 9
mx = -10 ** 9

for i in arr:
    mn = min(mn, i)
    mx = max(mx, i)

print('Minimum: %d\nMaximum: %d' %(mn, mx))