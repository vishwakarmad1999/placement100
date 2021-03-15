arr = list(map(int, input().split()))

m1 = arr[0]
m2 = -999999999

for i in range(1, len(arr)):
    if arr[i] > m1:
        m2 = m1
        m1 = arr[i]

print('Largest: %d\nSecond Largest: %d' %(m1, m2))

