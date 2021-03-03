def sort012(arr,n):
    zero = 0
    ones = 0
    
    for i in arr:
        if i == 0:
            zero += 1
        elif i == 1:
            ones += 1
    
    i = 0
    while i < zero:
        arr[i] = 0
        i += 1

    while i < zero + ones:
        arr[i] = 1
        i += 1
        
    while i < n:
        arr[i] = 2
        i += 1
                
    return arr

arr = list(map(int, input().split()))
n = len(arr)

sort012(arr, n)
print(arr)
