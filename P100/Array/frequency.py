arr = list(map(int, input().split()))
n = len(arr)

prev = arr[0]
count = 1
for i in range(1, n):
    if arr[i] == prev:
        count += 1
    else:
        print("%d -> %d" %(prev, count))
        prev = arr[i]
        count = 1
else:
    print("%d -> %d" %(prev, count))    
