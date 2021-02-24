def odd_appearing(arr):
    xor = n1 = n2 = 0
    for i in arr:
        xor ^= i

    rm = xor & ~(xor - 1)

    for i in arr:
        if i & rm:
            n1 ^= i
        else:
            n2 ^= i
        
    return (n1, n2)

arr = list(map(int, input().split()))
print(odd_appearing(arr))